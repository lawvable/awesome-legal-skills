from __future__ import annotations

import builtins
import json
import os
import subprocess
import sys
from pathlib import Path


def _raise_oserror(*args, **kwargs):
    raise OSError("simulated read-only filesystem: %r %r" % (args, kwargs))

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import first_run as fr  # pyright: ignore[reportMissingImports]

FIRST_RUN = ROOT / "first_run.py"

ENV_VAR = "LEGAL_DIAGRAM_STATE"


def _run(args: list[str], env_override: dict | None = None) -> tuple[int, dict]:
    env = dict(os.environ)
    env.pop(ENV_VAR, None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    if env_override:
        env.update(env_override)
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(FIRST_RUN)] + args,
        text=True,
        capture_output=True,
        env=env,
        timeout=15,
    )
    return proc.returncode, json.loads(proc.stdout)


# ---------------------------------------------------------------------------
# STATE PATH RESOLUTION
# ---------------------------------------------------------------------------

def test_state_path_uses_env_var_when_set(tmp_path, monkeypatch):
    custom = str(tmp_path / "custom_state.json")
    monkeypatch.setenv(ENV_VAR, custom)
    code, result = _run([], env_override={ENV_VAR: custom})
    assert code == 0
    assert result["state_path"] == custom


def test_state_path_defaults_to_home_when_env_absent():
    expected = str(Path("~/.legal-diagram/state.json").expanduser())
    code, result = _run([])
    assert code == 0
    # state_path may be the default or null (if unwritable); when set it must equal expected
    if result["state_path"] is not None:
        assert result["state_path"] == expected


# ---------------------------------------------------------------------------
# DETECT — marker present → returning
# ---------------------------------------------------------------------------

def test_detect_returns_returning_when_marker_present(tmp_path):
    state_file = tmp_path / "state.json"
    state_file.write_text(json.dumps({"tutorial_offered": True}))
    code, result = _run([], env_override={ENV_VAR: str(state_file)})
    assert code == 0
    assert result["state"] == "returning"
    assert result["state_path"] == str(state_file)


# ---------------------------------------------------------------------------
# DETECT — no marker, writable location → first_run
# ---------------------------------------------------------------------------

def test_detect_returns_first_run_when_no_marker_writable(tmp_path):
    state_file = tmp_path / "state.json"
    # file does not exist yet, but parent is writable
    code, result = _run([], env_override={ENV_VAR: str(state_file)})
    assert code == 0
    assert result["state"] == "first_run"
    assert result["state_path"] == str(state_file)


# ---------------------------------------------------------------------------
# DETECT — corrupt marker, writable location → first_run (no crash)
# ---------------------------------------------------------------------------

def test_detect_corrupt_marker_returns_first_run_no_crash(tmp_path):
    state_file = tmp_path / "state.json"
    state_file.write_text("NOT{valid}JSON!!!")
    code, result = _run([], env_override={ENV_VAR: str(state_file)})
    assert code == 0
    assert result["state"] == "first_run"


# ---------------------------------------------------------------------------
# DETECT — no writable location → unknown
# ---------------------------------------------------------------------------

def test_detect_returns_unknown_when_no_writable_location(tmp_path, monkeypatch):
    """Simulate unwritable filesystem by monkeypatching Path.mkdir and open."""
    import importlib

    state_file = tmp_path / "no_write" / "state.json"
    monkeypatch.setenv(ENV_VAR, str(state_file))

    monkeypatch.setattr(Path, "mkdir", _raise_oserror)
    monkeypatch.setattr(builtins, "open", _raise_oserror)

    # Run via subprocess so the monkeypatch to builtins.open can't affect it;
    # instead run inline using importlib reload to test the library API directly.
    importlib.reload(fr)

    result = fr.detect(state_file)
    assert result["state"] == "unknown"
    assert result["state_path"] is None


# ---------------------------------------------------------------------------
# MARK — success: creates file, subsequent detect returns returning
# ---------------------------------------------------------------------------

def test_mark_creates_state_file(tmp_path):
    state_file = tmp_path / "subdir" / "state.json"
    code, result = _run(["--mark"], env_override={ENV_VAR: str(state_file)})
    assert code == 0
    assert result["state"] == "returning"
    assert result["marked"] is True
    assert result["state_path"] == str(state_file)
    data = json.loads(state_file.read_text())
    assert data["tutorial_offered"] is True


def test_mark_then_detect_returns_returning(tmp_path):
    state_file = tmp_path / "state.json"
    _run(["--mark"], env_override={ENV_VAR: str(state_file)})
    code, result = _run([], env_override={ENV_VAR: str(state_file)})
    assert code == 0
    assert result["state"] == "returning"


# ---------------------------------------------------------------------------
# MARK — failure: OSError → unknown, marked=false, no exception
# ---------------------------------------------------------------------------

def test_mark_failure_returns_unknown_no_exception(tmp_path, monkeypatch):
    import importlib
    importlib.reload(fr)

    state_file = tmp_path / "readonly_dir" / "state.json"

    monkeypatch.setattr(Path, "mkdir", _raise_oserror)

    result = fr.mark(state_file)
    assert result["state"] == "unknown"
    assert result["marked"] is False
    assert result["state_path"] is None


# ---------------------------------------------------------------------------
# ENV OVERRIDE: --mark writes to custom path, detect reads it back
# ---------------------------------------------------------------------------

def test_env_override_mark_and_detect_roundtrip(tmp_path):
    custom = tmp_path / "custom.json"
    _run(["--mark"], env_override={ENV_VAR: str(custom)})
    assert custom.exists()
    code, result = _run([], env_override={ENV_VAR: str(custom)})
    assert code == 0
    assert result["state"] == "returning"
    assert result["state_path"] == str(custom)


# ---------------------------------------------------------------------------
# OUTPUT DISCIPLINE: every path emits exactly one valid JSON object, exit 0
# ---------------------------------------------------------------------------

def test_output_discipline_detect(tmp_path):
    state_file = tmp_path / "state.json"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(FIRST_RUN)],
        text=True,
        capture_output=True,
        env={**os.environ, ENV_VAR: str(state_file), "PYTHONDONTWRITEBYTECODE": "1"},
        timeout=15,
    )
    assert proc.returncode == 0
    lines = [l for l in proc.stdout.strip().splitlines() if l.strip()]
    assert len(lines) >= 1
    parsed = json.loads(proc.stdout)
    assert isinstance(parsed, dict)
    assert proc.stderr == "" or "PYTHONDONTWRITEBYTECODE" not in proc.stderr


def test_output_discipline_mark(tmp_path):
    state_file = tmp_path / "state.json"
    proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
        [sys.executable, str(FIRST_RUN), "--mark"],
        text=True,
        capture_output=True,
        env={**os.environ, ENV_VAR: str(state_file), "PYTHONDONTWRITEBYTECODE": "1"},
        timeout=15,
    )
    assert proc.returncode == 0
    parsed = json.loads(proc.stdout)
    assert isinstance(parsed, dict)


# ---------------------------------------------------------------------------
# UNWRITABLE TEST: monkeypatch dir-create + open to raise OSError
# ---------------------------------------------------------------------------

def test_unwritable_monkeypatch_detect_returns_unknown(tmp_path, monkeypatch):
    import importlib
    importlib.reload(fr)

    state_file = tmp_path / "new_dir" / "state.json"

    monkeypatch.setattr(Path, "mkdir", _raise_oserror)
    monkeypatch.setattr(builtins, "open", _raise_oserror)

    result = fr.detect(state_file)
    assert result["state"] == "unknown"
    assert result["state_path"] is None


def test_unwritable_monkeypatch_mark_returns_unknown_marked_false(tmp_path, monkeypatch):
    import importlib
    importlib.reload(fr)

    state_file = tmp_path / "new_dir" / "state.json"

    monkeypatch.setattr(Path, "mkdir", _raise_oserror)

    result = fr.mark(state_file)
    assert result["state"] == "unknown"
    assert result["marked"] is False
    assert result["state_path"] is None
