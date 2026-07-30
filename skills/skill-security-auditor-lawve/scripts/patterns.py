"""
Pattern catalog for the Skill Security Auditor.

This is the single source of truth for every regex pattern the
auditor recognises. Patterns are grouped by language family and by
threat category. Each pattern carries severity, category, and
remediation guidance so the scanner can produce actionable
findings without scattered if/else chains.

Every pattern definition line ends with `# noqa: SEC-AUDITOR` so
the auditor can scan its own source without flagging the literal
strings inside these regexes — this is critical because patterns
like r"\\beval\\s*\\(" obviously match themselves.

Adding a new pattern:
    1. Pick the right list (CODE / SHELL / JS / PROMPT / WORKFLOW /
       SECRETS) by what language family it applies to.
    2. Use the smallest regex that reliably catches the technique.
       Over-broad patterns produce false positives and erode trust.
    3. Set severity by impact, not by how rare the pattern is.
    4. Write the `risk` and `fix` fields in one short sentence each.
"""

from __future__ import annotations

import re
from typing import Pattern, TypedDict

from core import Severity  # noqa: SEC-AUDITOR


class PatternDef(TypedDict):
    """A single compiled pattern with metadata."""
    regex: Pattern[str]
    category: str
    severity: Severity
    risk: str
    fix: str
    # Optional flag — if True, only fires when the surrounding context
    # contains another suspicious signal. Currently informational; the
    # scanner can use it to suppress noisy patterns when desired.
    needs_corroboration: bool


def _p(regex: str, category: str, severity: Severity,
       risk: str, fix: str, needs_corroboration: bool = False) -> PatternDef:
    """Compile a single pattern definition.

    Compiling here (once at import time) is significantly faster than
    re-compiling on every scanned line, and centralises any future
    flag changes (e.g. DOTALL, VERBOSE).
    """
    return PatternDef(
        regex=re.compile(regex),
        category=category,
        severity=severity,
        risk=risk,
        fix=fix,
        needs_corroboration=needs_corroboration,
    )


# =============================================================================
# PYTHON / GENERIC CODE PATTERNS
# =============================================================================
# These apply to any text-form code file. Patterns that are specific
# to shell or JS live in their own lists below and are applied on top
# of these for files with those extensions.

CODE_PATTERNS: list[PatternDef] = [

    # -------------------------------------------------------------------------
    # CODE EXECUTION — dynamic evaluation of strings as code
    # -------------------------------------------------------------------------

    _p(r"\beval\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.CRITICAL,
       "Arbitrary code execution via eval() — string is executed as Python",  # noqa: SEC-AUDITOR
       "Replace eval() with ast.literal_eval() for data, or explicit parsing logic"),  # noqa: SEC-AUDITOR

    _p(r"\bexec\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.CRITICAL,
       "Arbitrary code execution via exec()",  # noqa: SEC-AUDITOR
       "Remove exec(). Rewrite to dispatch on a fixed table of allowed actions"),  # noqa: SEC-AUDITOR

    _p(r"\bcompile\s*\([^)]*['\"]exec['\"]",
       "CODE-EXEC", Severity.CRITICAL,
       "Dynamic compilation in 'exec' mode — equivalent to eval/exec",  # noqa: SEC-AUDITOR
       "Remove compile() with exec mode; use explicit code paths"),  # noqa: SEC-AUDITOR

    _p(r"\b__import__\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.HIGH,
       "Dynamic import via __import__ — can load arbitrary modules at runtime",  # noqa: SEC-AUDITOR
       "Use explicit `import` statements at module top level"),  # noqa: SEC-AUDITOR

    _p(r"\bimportlib\.(?:import_module|__import__)\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.HIGH,
       "Dynamic import via importlib",  # noqa: SEC-AUDITOR
       "Use explicit imports unless dynamic plug-in loading is documented and bounded"),  # noqa: SEC-AUDITOR

    _p(r"\btypes\.(?:CodeType|FunctionType)\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.HIGH,
       "Manual code object construction — equivalent to compile()/exec()",  # noqa: SEC-AUDITOR
       "Remove dynamic code object creation"),  # noqa: SEC-AUDITOR

    _p(r"\bgetattr\s*\([^)]*['\"](?:system|popen|exec|eval)['\"]",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.HIGH,
       "Dynamic attribute lookup of dangerous function — obfuscated call",  # noqa: SEC-AUDITOR
       "Use direct attribute access; dynamic dispatch hides intent"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # COMMAND INJECTION — shell out with attacker-controllable strings
    # -------------------------------------------------------------------------

    _p(r"\bos\.system\s*\(",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.CRITICAL,
       "Shell command execution via os.system()",  # noqa: SEC-AUDITOR
       "Use subprocess.run([...], shell=False) with a list of arguments"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.popen\s*\(",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.CRITICAL,
       "Shell command execution via os.popen()",  # noqa: SEC-AUDITOR
       "Use subprocess.run([...], capture_output=True, shell=False)"),  # noqa: SEC-AUDITOR

    _p(r"\bsubprocess\.\w+\([^)]*shell\s*=\s*True",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.CRITICAL,
       "subprocess with shell=True — enables command injection",  # noqa: SEC-AUDITOR
       "Set shell=False (or omit) and pass the command as a list of arguments"),  # noqa: SEC-AUDITOR

    _p(r"\bcommands\.(?:get(?:status)?output)\s*\(",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.CRITICAL,
       "Deprecated commands module — runs through the shell",  # noqa: SEC-AUDITOR
       "Use subprocess.run([...], capture_output=True)"),  # noqa: SEC-AUDITOR

    _p(r"\bpty\.spawn\s*\(",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.HIGH,
       "pty.spawn — opens a pseudo-terminal, common in reverse-shell payloads",  # noqa: SEC-AUDITOR
       "Remove pty.spawn unless explicitly building a terminal tool"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # NETWORK — outbound traffic, especially POST/PUT and raw sockets
    # -------------------------------------------------------------------------

    _p(r"\brequests\.(?:post|put|patch|delete)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Outbound HTTP write — primary data-exfiltration vector",  # noqa: SEC-AUDITOR
       "Remove outbound writes, or document the trusted destination and bound it to it"),  # noqa: SEC-AUDITOR

    _p(r"\brequests\.(?:get|head|options)\s*\(",  # noqa: SEC-AUDITOR
       "NET-READ", Severity.MEDIUM,
       "Outbound HTTP read — may fetch payloads or beacon data",  # noqa: SEC-AUDITOR
       "Verify the destination is trusted and necessary"),  # noqa: SEC-AUDITOR

    _p(r"\burllib\.request\.urlopen\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.HIGH,
       "Outbound HTTP via urllib",  # noqa: SEC-AUDITOR
       "Remove or restrict to a documented, trusted host"),  # noqa: SEC-AUDITOR

    _p(r"\burllib\.request\.(?:urlretrieve|Request)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.HIGH,
       "Outbound HTTP via urllib — file fetch or arbitrary request",  # noqa: SEC-AUDITOR
       "Remove or restrict to a trusted host"),  # noqa: SEC-AUDITOR

    _p(r"\bhttp\.client\.(?:HTTP|HTTPS)Connection\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.HIGH,
       "Raw HTTP client connection — bypasses higher-level libraries",  # noqa: SEC-AUDITOR
       "Remove or document and restrict the destination"),  # noqa: SEC-AUDITOR

    _p(r"\bhttpx\.(?:post|put|patch|delete|AsyncClient|stream)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Outbound HTTP write via httpx — data-exfiltration vector",  # noqa: SEC-AUDITOR
       "Remove or restrict to a documented, trusted host"),  # noqa: SEC-AUDITOR

    _p(r"\baiohttp\.(?:ClientSession|request)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.HIGH,
       "Async HTTP client — potential data-exfiltration channel",  # noqa: SEC-AUDITOR
       "Remove or restrict to a documented, trusted host"),  # noqa: SEC-AUDITOR

    _p(r"\bsocket\.(?:socket|create_connection|create_server|connect)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Raw socket use — common in reverse shells and C2 channels",  # noqa: SEC-AUDITOR
       "Remove raw sockets; if a TCP client is genuinely needed, justify and bound it"),  # noqa: SEC-AUDITOR

    _p(r"\bsocket\.gethostbyname\s*\(",  # noqa: SEC-AUDITOR
       "NET-DNS", Severity.HIGH,
       "Manual DNS lookup — sometimes used for DNS-based data exfiltration",  # noqa: SEC-AUDITOR
       "Remove unless network configuration is part of the skill's core function"),  # noqa: SEC-AUDITOR

    _p(r"\bdns\.resolver\.|dnspython|\bdnslib\.",  # noqa: SEC-AUDITOR
       "NET-DNS", Severity.HIGH,
       "Programmatic DNS resolver — DNS tunnelling / exfiltration vector",  # noqa: SEC-AUDITOR
       "Remove unless DNS is the core function of the skill"),  # noqa: SEC-AUDITOR

    _p(r"\bwebsockets?\.(?:connect|WebSocketApp|create_connection)\s*\(",  # noqa: SEC-AUDITOR
       "NET-WS", Severity.CRITICAL,
       "WebSocket connection — persistent bidirectional channel, often C2",  # noqa: SEC-AUDITOR
       "Remove unless WebSocket is the documented core function"),  # noqa: SEC-AUDITOR

    # Hardcoded IPv4 literal in a URL is a strong C2 signal — domains
    # are normal in code, raw IPs almost never are unless they're loopback,
    # private RFC1918, or link-local. We exclude those.
    _p(r"https?://(?!127\.|10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.|0\.0\.0\.0|169\.254\.)"
       r"(?:\d{1,3}\.){3}\d{1,3}",
       "NET-HARDCODED-IP", Severity.HIGH,
       "Hardcoded public IPv4 in URL — typical command-and-control beacon",  # noqa: SEC-AUDITOR
       "Remove the IP literal. Skills should not call hardcoded IP addresses"),  # noqa: SEC-AUDITOR

    # Common exfiltration sinks — even seeing the hostname in source is
    # a strong signal because these services exist specifically to
    # receive arbitrary HTTP requests.
    _p(r"\b(?:webhook\.site|requestbin\.com|requestbin\.net|interact\.sh|"
       r"burpcollaborator\.net|pipedream\.com|beeceptor\.com|hookbin\.com|"
       r"ngrok\.io|ngrok-free\.app|trycloudflare\.com|smee\.io|en7\.io|"
       r"requestcatcher\.com|loca\.lt|serveo\.net)",
       "NET-WEBHOOK-SINK", Severity.CRITICAL,
       "Reference to known data-exfiltration / webhook receiver host",  # noqa: SEC-AUDITOR
       "Remove the reference. These services are used for arbitrary HTTP capture"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # OBFUSCATION — encoding tricks that hide payload intent
    # -------------------------------------------------------------------------

    _p(r"\bbase64\.b64decode\s*\(",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.HIGH,
       "Base64 decoding — frequently used to hide eval/exec payloads",  # noqa: SEC-AUDITOR
       "Decode and inspect the content. If not user data, replace with a string literal"),  # noqa: SEC-AUDITOR

    _p(r"\bbase64\.b32decode\s*\(|\bbase64\.b16decode\s*\(",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.HIGH,
       "Non-base64 base decode — sometimes used to evade base64 scanners",  # noqa: SEC-AUDITOR
       "Replace with explicit string literals or document the use case"),  # noqa: SEC-AUDITOR

    _p(r"\bcodecs\.decode\s*\(",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.HIGH,
       "Generic codecs.decode — can decode hex, base64, rot13, etc.",  # noqa: SEC-AUDITOR
       "Review what's being decoded. Replace with readable code where possible"),  # noqa: SEC-AUDITOR

    _p(r"\bbytes\.fromhex\s*\(",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.HIGH,
       "Hex byte decoding — hides bytes that may be executable code",  # noqa: SEC-AUDITOR
       "Replace with explicit byte literals or document why hex is necessary"),  # noqa: SEC-AUDITOR

    _p(r"\bchr\s*\(\s*\d+\s*\)(?:\s*\+\s*chr\s*\(\s*\d+\s*\)){3,}",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.CRITICAL,
       "chr() chain building a string character-by-character — classic obfuscation",  # noqa: SEC-AUDITOR
       "Replace with the literal string the chain produces"),  # noqa: SEC-AUDITOR

    _p(r"(?:\\x[0-9a-fA-F]{2}){8,}",
       "OBFUSCATION", Severity.HIGH,
       "Long hex escape sequence — likely an obfuscated payload",  # noqa: SEC-AUDITOR
       "Decode and inspect. Replace with readable strings"),  # noqa: SEC-AUDITOR

    _p(r"['\"][A-Za-z0-9+/]{120,}={0,2}['\"]",
       "OBFUSCATION", Severity.MEDIUM,
       "Long base64-looking string literal — possible encoded payload",  # noqa: SEC-AUDITOR
       "If this is a payload, decode and inspect. If it's data, move it to a file"),  # noqa: SEC-AUDITOR

    _p(r"\bzlib\.decompress\s*\(|\blzma\.decompress\s*\(|\bbz2\.decompress\s*\(",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.MEDIUM,
       "Compressed payload decoding — sometimes layered with base64 to hide code",  # noqa: SEC-AUDITOR
       "Review what's being decompressed and ensure it's not executable code"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # CREDENTIAL ACCESS — reading secrets the skill has no business reading
    # -------------------------------------------------------------------------

    _p(r"['\"]~?/?\.?ssh/(?:id_|authorized_keys|known_hosts|config)",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads from SSH directory — SSH keys are user secrets",  # noqa: SEC-AUDITOR
       "Remove access to ~/.ssh entirely"),  # noqa: SEC-AUDITOR

    _p(r"['\"]~?/?\.aws/(?:credentials|config)",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads AWS credentials file",  # noqa: SEC-AUDITOR
       "Remove access to ~/.aws"),  # noqa: SEC-AUDITOR

    _p(r"['\"]~?/?\.config/(?:gh|gcloud|kubectl|hub)",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads cloud-provider or platform credential directory",  # noqa: SEC-AUDITOR
       "Remove access to the credential directory"),  # noqa: SEC-AUDITOR

    _p(r"['\"]~?/?\.(?:gnupg|netrc|kube|docker|npmrc|pypirc)(?![a-zA-Z])",  # noqa: SEC-AUDITOR
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads from a known credential/config directory",  # noqa: SEC-AUDITOR
       "Remove access to the credential directory"),  # noqa: SEC-AUDITOR

    _p(r"\bopen\s*\([^)]*\.(?:pem|key|p12|pfx|jks|keystore)[\"']",
       "CRED-HARVEST", Severity.CRITICAL,
       "Opens a private key or keystore file",  # noqa: SEC-AUDITOR
       "Remove access to private key files"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.environ(?:\.get)?\s*[\[\(]\s*['\"]"
       r"(?:AWS_(?:ACCESS|SECRET)|GITHUB_TOKEN|GH_TOKEN|GITLAB_TOKEN|"
       r"NPM_TOKEN|PYPI_TOKEN|DOCKER_PASSWORD|SLACK_TOKEN|DISCORD_TOKEN|"
       r"TELEGRAM_BOT_TOKEN|OPENAI_API_KEY|ANTHROPIC_API_KEY|"
       r"STRIPE_(?:SECRET|API)|TWILIO_AUTH|API_KEY|API_SECRET|"
       r"PASSWORD|PASSWD|SECRET_KEY|PRIVATE_KEY|ACCESS_TOKEN)",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads a known-sensitive environment variable",  # noqa: SEC-AUDITOR
       "Skills should not read user credentials. Remove this access"),  # noqa: SEC-AUDITOR

    # Bulk environment harvesting — dict(os.environ) or list of all env vars
    # is what malware does to grab everything before exfil.
    _p(r"\bdict\s*\(\s*os\.environ\s*\)|\blist\s*\(\s*os\.environ\.(?:keys|items|values)\s*\(\s*\)\s*\)",  # noqa: SEC-AUDITOR
       "CRED-HARVEST", Severity.CRITICAL,
       "Bulk environment-variable harvesting",  # noqa: SEC-AUDITOR
       "Read only the specific variables you need by name"),  # noqa: SEC-AUDITOR

    _p(r"\bkeyring\.(?:get_password|get_credential)\s*\(",  # noqa: SEC-AUDITOR
       "CRED-HARVEST", Severity.CRITICAL,
       "Accesses the system keyring/keychain",  # noqa: SEC-AUDITOR
       "Skills must not access the system credential store"),  # noqa: SEC-AUDITOR

    # Browser cookie databases — these are the next step after a foothold
    _p(r"['\"](?:Cookies|Login Data|Web Data|History|formhistory\.sqlite)['\"]",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reference to browser cookie/credential database",  # noqa: SEC-AUDITOR
       "Skills must not read browser credential stores"),  # noqa: SEC-AUDITOR

    _p(r"['\"]/proc/\d*/?environ['\"]|['\"]/proc/self/environ['\"]",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads /proc/*/environ — extracts environment variables of other processes",  # noqa: SEC-AUDITOR
       "Remove this access entirely"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # PERSISTENCE — installing a foothold that survives shell restarts
    # -------------------------------------------------------------------------

    _p(r"['\"][^\"']*\.(?:bashrc|bash_profile|profile|zshrc|zprofile|zshenv|inputrc)['\"]",
       "PERSISTENCE", Severity.CRITICAL,
       "Reference to shell configuration file — persistence vector",  # noqa: SEC-AUDITOR
       "Skills should not read or write shell rc files"),  # noqa: SEC-AUDITOR

    _p(r"\bcrontab\b|['\"]/etc/cron(?:tab|\.d|\.daily|\.hourly|\.weekly|\.monthly)",  # noqa: SEC-AUDITOR
       "PERSISTENCE", Severity.CRITICAL,
       "Cron job manipulation — installs persistent scheduled execution",  # noqa: SEC-AUDITOR
       "Remove cron access; skills must not modify the system scheduler"),  # noqa: SEC-AUDITOR

    _p(r"['\"]/Library/LaunchAgents/|['\"]~/Library/LaunchAgents/|\blaunchctl\s+(?:load|bootstrap|enable)",
       "PERSISTENCE", Severity.CRITICAL,
       "macOS LaunchAgent / launchctl — boot-time persistence",  # noqa: SEC-AUDITOR
       "Remove. Skills must not install LaunchAgents"),  # noqa: SEC-AUDITOR

    _p(r"['\"]/etc/systemd/system/|['\"]~/\.config/systemd/|\bsystemctl\s+(?:enable|start|--user)",
       "PERSISTENCE", Severity.CRITICAL,
       "systemd unit installation / activation — boot-time persistence",  # noqa: SEC-AUDITOR
       "Remove. Skills must not install systemd units"),  # noqa: SEC-AUDITOR

    _p(r"['\"]/etc/init\.d/|['\"]/etc/rc\.local|['\"]/etc/rc\.d/",
       "PERSISTENCE", Severity.CRITICAL,
       "SysV / rc.local persistence vector",  # noqa: SEC-AUDITOR
       "Remove. Skills must not install init scripts"),  # noqa: SEC-AUDITOR

    _p(r"['\"]~/\.config/autostart/|['\"]/etc/xdg/autostart/",
       "PERSISTENCE", Severity.CRITICAL,
       "XDG autostart entry — login-time persistence on Linux desktops",  # noqa: SEC-AUDITOR
       "Remove. Skills must not install autostart entries"),  # noqa: SEC-AUDITOR

    _p(r"\.git/hooks/(?:pre-commit|post-commit|pre-push|post-checkout|post-merge|pre-receive)",
       "PERSISTENCE", Severity.HIGH,
       "Writes to git hooks — runs on every git operation",  # noqa: SEC-AUDITOR
       "Remove. Skills must not install git hooks without explicit user setup"),  # noqa: SEC-AUDITOR

    _p(r"\.ssh/authorized_keys|\.ssh/authorized_keys2",  # noqa: SEC-AUDITOR
       "PERSISTENCE", Severity.CRITICAL,
       "Modifies SSH authorized_keys — adds attacker's key for permanent access",  # noqa: SEC-AUDITOR
       "Remove. Skills must not touch authorized_keys"),  # noqa: SEC-AUDITOR

    # Windows persistence — Registry Run keys, scheduled tasks
    _p(r"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run|"
       r"HKLM\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run",
       "PERSISTENCE", Severity.CRITICAL,
       "Windows Run-key registry path — login-time persistence",  # noqa: SEC-AUDITOR
       "Remove. Skills must not write to Run keys"),  # noqa: SEC-AUDITOR

    _p(r"\bschtasks\s+/create\b",  # noqa: SEC-AUDITOR
       "PERSISTENCE", Severity.CRITICAL,
       "Windows scheduled task creation — persistence",  # noqa: SEC-AUDITOR
       "Remove. Skills must not create scheduled tasks"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # FILESYSTEM ABUSE — writes outside the skill or destructive ops
    # -------------------------------------------------------------------------

    _p(r"\bopen\s*\([^)]*['\"](?:/etc/|/usr/(?!local/share)|/var/|/boot/|/sys/)",
       "FS-WRITE-SYSTEM", Severity.HIGH,
       "File operation against system directory — outside skill scope",  # noqa: SEC-AUDITOR
       "Constrain file operations to the skill directory or a user-specified output path"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.symlink\s*\(",  # noqa: SEC-AUDITOR
       "FS-SYMLINK", Severity.HIGH,
       "Symbolic link creation — directory-traversal vector",  # noqa: SEC-AUDITOR
       "Remove symlink creation unless explicitly required and bounded"),  # noqa: SEC-AUDITOR

    _p(r"\bshutil\.rmtree\s*\(",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.HIGH,
       "Recursive directory delete — destructive; verify target is scoped",  # noqa: SEC-AUDITOR
       "Validate the target path is inside the skill scratch directory before deleting"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.(?:remove|unlink)\s*\(",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.MEDIUM,
       "File deletion — verify the target is scoped",  # noqa: SEC-AUDITOR
       "Ensure deletion paths are validated and inside the expected directory"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.chmod\s*\([^)]*0o?[0-7]*7[0-7]{2}",  # noqa: SEC-AUDITOR
       "FS-PERMS", Severity.MEDIUM,
       "World-writable permissions — creates a tampering vector",  # noqa: SEC-AUDITOR
       "Use 0o644 for files and 0o755 for directories"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.chmod\s*\([^)]*0o?4[0-7]{3}",  # noqa: SEC-AUDITOR
       "FS-PERMS", Severity.CRITICAL,
       "Setting SUID bit — privilege escalation",  # noqa: SEC-AUDITOR
       "Remove setuid permission changes"),  # noqa: SEC-AUDITOR

    _p(r"\bos\.set(?:e?uid|e?gid)\s*\(",  # noqa: SEC-AUDITOR
       "FS-PERMS", Severity.CRITICAL,
       "UID/GID manipulation — privilege escalation",  # noqa: SEC-AUDITOR
       "Skills must run as the invoking user; remove UID changes"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # DESERIALIZATION — formats that execute code on load
    # -------------------------------------------------------------------------

    _p(r"\bpickle\.(?:loads?|Unpickler)\s*\(",  # noqa: SEC-AUDITOR
       "DESERIAL", Severity.HIGH,
       "Pickle deserialization — executes arbitrary Python on load",  # noqa: SEC-AUDITOR
       "Use json or a typed schema (pydantic, dataclasses_json) instead"),  # noqa: SEC-AUDITOR

    _p(r"\byaml\.load\s*\((?![^)]*Loader\s*=\s*(?:yaml\.)?SafeLoader)",
       "DESERIAL", Severity.HIGH,
       "yaml.load() without SafeLoader — can execute arbitrary Python",  # noqa: SEC-AUDITOR
       "Use yaml.safe_load() or pass Loader=yaml.SafeLoader"),  # noqa: SEC-AUDITOR

    _p(r"\bmarshal\.loads?\s*\(",  # noqa: SEC-AUDITOR
       "DESERIAL", Severity.HIGH,
       "Marshal deserialization — executes arbitrary code on load",  # noqa: SEC-AUDITOR
       "Use json or another safe format"),  # noqa: SEC-AUDITOR

    _p(r"\bshelve\.open\s*\(",  # noqa: SEC-AUDITOR
       "DESERIAL", Severity.HIGH,
       "Shelve — built on pickle, so executes code on load",  # noqa: SEC-AUDITOR
       "Use JSON or SQLite for persistent storage"),  # noqa: SEC-AUDITOR

    _p(r"\bdill\.loads?\s*\(",  # noqa: SEC-AUDITOR
       "DESERIAL", Severity.HIGH,
       "dill is a superset of pickle — same code-execution risk",  # noqa: SEC-AUDITOR
       "Use json or a typed schema"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # HIDDEN HELPERS — file encryption and password-protected archives
    # -------------------------------------------------------------------------

    _p(r"\b(?:Fernet|AES\.new|AES_GCM|ChaCha20)\s*\(",  # noqa: SEC-AUDITOR
       "HIDDEN-HELPER", Severity.MEDIUM,
       "Symmetric encryption primitives — sometimes wrapping payload code",  # noqa: SEC-AUDITOR
       "If decrypting bundled data, document the use. If decrypting fetched payloads, remove"),  # noqa: SEC-AUDITOR

    _p(r"\bcryptography\.fernet\.Fernet|\bnacl\.secret\.",  # noqa: SEC-AUDITOR
       "HIDDEN-HELPER", Severity.MEDIUM,
       "Symmetric crypto library used to hide payloads",  # noqa: SEC-AUDITOR
       "Document the legitimate use case or remove"),  # noqa: SEC-AUDITOR

    # -------------------------------------------------------------------------
    # SUPPLY CHAIN — installing packages at runtime
    # -------------------------------------------------------------------------

    _p(r"\bpip3?\s+install\b|\bpython3?\s+-m\s+pip\s+install\b",  # noqa: SEC-AUDITOR
       "SUPPLY-RUNTIME", Severity.HIGH,
       "Runtime pip install — installs unreviewed packages at execution time",  # noqa: SEC-AUDITOR
       "Move dependencies into requirements.txt for review before install"),  # noqa: SEC-AUDITOR

    _p(r"\bsubprocess\.\w+\([^)]*['\"](?:pip|pip3)['\"]",  # noqa: SEC-AUDITOR
       "SUPPLY-RUNTIME", Severity.HIGH,
       "Runtime pip install invoked via subprocess",  # noqa: SEC-AUDITOR
       "Move dependencies into requirements.txt for review before install"),  # noqa: SEC-AUDITOR
]


# =============================================================================
# SHELL-SPECIFIC PATTERNS
# =============================================================================
# Applied on top of CODE_PATTERNS for .sh / .bash / .zsh files.

SHELL_PATTERNS: list[PatternDef] = [

    # Download-and-execute is the single highest-risk shell pattern.
    _p(r"\bcurl\s[^|\n]*\|\s*(?:ba)?sh\b",  # noqa: SEC-AUDITOR
       "REMOTE-EXEC", Severity.CRITICAL,
       "curl | sh — downloads and executes remote code without inspection",  # noqa: SEC-AUDITOR
       "Download the script to a file first, inspect it, then execute it explicitly"),  # noqa: SEC-AUDITOR

    _p(r"\bwget\s[^|\n]*\|\s*(?:ba)?sh\b",  # noqa: SEC-AUDITOR
       "REMOTE-EXEC", Severity.CRITICAL,
       "wget | sh — downloads and executes remote code",  # noqa: SEC-AUDITOR
       "Download to a file first, inspect it, then execute"),  # noqa: SEC-AUDITOR

    _p(r"\bcurl\s[^&\n]*&&\s*(?:ba)?sh\b",  # noqa: SEC-AUDITOR
       "REMOTE-EXEC", Severity.CRITICAL,
       "curl && sh — download then execute pattern",  # noqa: SEC-AUDITOR
       "Inspect the downloaded file before executing"),  # noqa: SEC-AUDITOR

    _p(r"<\(\s*curl\s|<\(\s*wget\s",
       "REMOTE-EXEC", Severity.CRITICAL,
       "Process substitution from curl/wget — executes remote content",  # noqa: SEC-AUDITOR
       "Download first, inspect, then run"),  # noqa: SEC-AUDITOR

    _p(r"\b(?:python|python3|node|perl|ruby|php)\s+-c\s+['\"][^'\"]{30,}",
       "CODE-EXEC", Severity.HIGH,
       "Inline interpreter -c with a long string — frequently hides obfuscated code",  # noqa: SEC-AUDITOR
       "Move the code to a separate, inspectable script file"),  # noqa: SEC-AUDITOR

    _p(r"\beval\s+",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.HIGH,
       "Shell eval — expands and runs its argument as a command",  # noqa: SEC-AUDITOR
       "Remove eval. Use functions or arrays instead of dynamic command construction"),  # noqa: SEC-AUDITOR

    _p(r"`[^`\n]*\$[A-Za-z_]",
       "CMD-INJECT", Severity.HIGH,
       "Backtick command substitution with variable — injection risk",  # noqa: SEC-AUDITOR
       "Use $(...) and quote variable expansions: \"${VAR}\""),  # noqa: SEC-AUDITOR

    _p(r"\bnc\s+(?:-[el]|-l\s+-p)|\bncat\s+-[el]|\bnetcat\s+",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Netcat listener / executor — classic reverse-shell tool",  # noqa: SEC-AUDITOR
       "Remove netcat invocations"),  # noqa: SEC-AUDITOR

    _p(r"\bbash\s+-i\s+>&?\s*/dev/tcp/",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Bash /dev/tcp reverse shell",  # noqa: SEC-AUDITOR
       "Remove the /dev/tcp redirect"),  # noqa: SEC-AUDITOR

    # Destructive
    _p(r"\brm\s+-rf\s+/(?!\w)",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.CRITICAL,
       "rm -rf / — catastrophic data deletion",  # noqa: SEC-AUDITOR
       "Remove. Scope deletion to specific subdirectories"),  # noqa: SEC-AUDITOR

    _p(r"\brm\s+-rf\s+(?:~|\$HOME)\b",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.CRITICAL,
       "rm -rf $HOME — wipes user home directory",  # noqa: SEC-AUDITOR
       "Remove. Skills must never touch the user's home wholesale"),  # noqa: SEC-AUDITOR

    _p(r"\brm\s+-rf\s+\*\s*$",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.HIGH,
       "rm -rf * — recursive delete relative to cwd; behavior depends on cwd",  # noqa: SEC-AUDITOR
       "Use explicit absolute paths, validate them, and delete only what you created"),  # noqa: SEC-AUDITOR

    _p(r"\bmkfs(?:\.\w+)?\s+",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.CRITICAL,
       "mkfs — formats a filesystem; destroys all data on the target device",  # noqa: SEC-AUDITOR
       "Remove. Skills must never format a filesystem"),  # noqa: SEC-AUDITOR

    _p(r"\bdd\s+if=[^\s]+\s+of=/dev/(?:sd[a-z]|nvme|loop|hd[a-z])",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.CRITICAL,
       "dd writing to a raw block device — destroys data on the device",  # noqa: SEC-AUDITOR
       "Remove. Skills must never write to raw block devices"),  # noqa: SEC-AUDITOR

    _p(r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;\s*:",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.CRITICAL,
       "Bash fork bomb",  # noqa: SEC-AUDITOR
       "Remove"),  # noqa: SEC-AUDITOR

    _p(r">\s*/dev/(?:sd[a-z]|nvme|loop|hd[a-z])\b",  # noqa: SEC-AUDITOR
       "FS-DESTRUCTIVE", Severity.CRITICAL,
       "Direct redirect to a raw block device — data destruction",  # noqa: SEC-AUDITOR
       "Remove block-device writes"),  # noqa: SEC-AUDITOR

    # Privilege escalation
    _p(r"\bsudo\b",  # noqa: SEC-AUDITOR
       "PRIV-ESC", Severity.HIGH,
       "sudo invocation — skills should not require elevated privileges",  # noqa: SEC-AUDITOR
       "Remove sudo; design the skill to work as the invoking user"),  # noqa: SEC-AUDITOR

    _p(r"\bchmod\s+(?:[ugoa]\+s|4[0-7]{3})\b",  # noqa: SEC-AUDITOR
       "PRIV-ESC", Severity.CRITICAL,
       "chmod sets SUID — privilege escalation vector",  # noqa: SEC-AUDITOR
       "Remove SUID changes. Skills must never set SUID"),  # noqa: SEC-AUDITOR

    _p(r"\bchmod\s+(?:-R\s+)?777\b",  # noqa: SEC-AUDITOR
       "FS-PERMS", Severity.HIGH,
       "chmod 777 — world-writable, creates tampering vector",  # noqa: SEC-AUDITOR
       "Use 644 for files and 755 for directories"),  # noqa: SEC-AUDITOR

    # Password-protected archives and encrypted blobs are sometimes used
    # to smuggle payloads past static review.
    _p(r"\b7z\s+x\s+-p|\bunzip\s+-P\s|\bopenssl\s+enc\s+-d\b",  # noqa: SEC-AUDITOR
       "HIDDEN-HELPER", Severity.HIGH,
       "Password-protected archive extraction or symmetric decryption — payload-hiding pattern",  # noqa: SEC-AUDITOR
       "Inspect the archive/encrypted content. Skills should not ship encrypted code"),  # noqa: SEC-AUDITOR

    _p(r"\bgpg\s+(?:-d|--decrypt|--batch.*--decrypt)",  # noqa: SEC-AUDITOR
       "HIDDEN-HELPER", Severity.HIGH,
       "GPG decryption — sometimes used to unpack hidden payloads",  # noqa: SEC-AUDITOR
       "Inspect the decrypted content's purpose"),  # noqa: SEC-AUDITOR

    # Data exfil specifically through curl/wget with env vars or credential files
    _p(r"\bcurl\s[^\n]*(?:\$[A-Z_]{2,}|\$\{[A-Z_]{2,}\})",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "curl interpolates an environment variable into the request",  # noqa: SEC-AUDITOR
       "Move secrets into a pre-fetch script; never interpolate $SECRETS into curl"),  # noqa: SEC-AUDITOR

    _p(r"\bwget\s[^\n]*(?:\$[A-Z_]{2,}|\$\{[A-Z_]{2,}\})",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "wget interpolates an environment variable into the request",  # noqa: SEC-AUDITOR
       "Never interpolate $SECRETS into wget arguments"),  # noqa: SEC-AUDITOR

    _p(r"\bprintenv\b.*\|\s*(?:curl|wget|nc|netcat)",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "printenv piped to network tool — full-environment exfiltration",  # noqa: SEC-AUDITOR
       "Remove. The whole environment is full of secrets"),  # noqa: SEC-AUDITOR

    _p(r"\benv\b\s*\|\s*(?:curl|wget|nc|netcat)",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "env piped to network tool — full-environment exfiltration",  # noqa: SEC-AUDITOR
       "Remove. Never exfiltrate the whole environment"),  # noqa: SEC-AUDITOR

    # Force-push and history rewriting
    _p(r"\bgit\s+push\s+(?:--force|--force-with-lease|-f)\s+\S+\s+(?:main|master)",  # noqa: SEC-AUDITOR
       "VCS-DESTRUCTIVE", Severity.HIGH,
       "git force-push to main/master — rewrites shared history",  # noqa: SEC-AUDITOR
       "Remove. Gate force-pushes to feature branches only"),  # noqa: SEC-AUDITOR
]


# =============================================================================
# JAVASCRIPT / TYPESCRIPT-SPECIFIC PATTERNS
# =============================================================================

JS_PATTERNS: list[PatternDef] = [

    _p(r"\beval\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.CRITICAL,
       "JavaScript eval() — executes a string as code",  # noqa: SEC-AUDITOR
       "Remove eval(). Use JSON.parse() for data or explicit dispatch tables"),  # noqa: SEC-AUDITOR

    _p(r"\bnew\s+Function\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.CRITICAL,
       "Function constructor — equivalent to eval()",  # noqa: SEC-AUDITOR
       "Use a regular function declaration"),  # noqa: SEC-AUDITOR

    _p(r"\bset(?:Timeout|Interval)\s*\(\s*['\"]",
       "CODE-EXEC", Severity.HIGH,
       "setTimeout/setInterval with a string argument — eval-like",  # noqa: SEC-AUDITOR
       "Pass a function reference, not a string"),  # noqa: SEC-AUDITOR

    _p(r"\bvm\.(?:runInThisContext|runInNewContext|runInContext)\s*\(",  # noqa: SEC-AUDITOR
       "CODE-EXEC", Severity.CRITICAL,
       "Node vm module — runs code in a context",  # noqa: SEC-AUDITOR
       "Remove dynamic code execution"),  # noqa: SEC-AUDITOR

    _p(r"\bchild_process\.(?:exec|execSync)\s*\(",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.CRITICAL,
       "child_process.exec — runs through the shell, injection-prone",  # noqa: SEC-AUDITOR
       "Use child_process.spawn(command, [...args]) with shell: false"),  # noqa: SEC-AUDITOR

    _p(r"\bchild_process\.spawn[^(]*\([^)]*shell\s*:\s*true",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.CRITICAL,
       "child_process.spawn with shell: true — command injection vector",  # noqa: SEC-AUDITOR
       "Set shell: false (or omit) and pass arguments as an array"),  # noqa: SEC-AUDITOR

    _p(r"\brequire\s*\(\s*['\"]child_process['\"]\s*\)",  # noqa: SEC-AUDITOR
       "CMD-INJECT", Severity.HIGH,
       "Imports child_process — needs review of all subsequent calls",  # noqa: SEC-AUDITOR
       "Audit every child_process call; prefer spawn() with shell: false"),  # noqa: SEC-AUDITOR

    _p(r"\bfetch\s*\([^)]*\{[^}]*method\s*:\s*['\"](?:POST|PUT|PATCH|DELETE)",
       "NET-EXFIL", Severity.CRITICAL,
       "Outbound HTTP write via fetch()",  # noqa: SEC-AUDITOR
       "Remove or restrict to a documented, trusted destination"),  # noqa: SEC-AUDITOR

    _p(r"\baxios\.(?:post|put|patch|delete)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Outbound HTTP write via axios",  # noqa: SEC-AUDITOR
       "Remove or restrict to a documented, trusted destination"),  # noqa: SEC-AUDITOR

    _p(r"\bnew\s+WebSocket\s*\(",  # noqa: SEC-AUDITOR
       "NET-WS", Severity.CRITICAL,
       "WebSocket connection — persistent bidirectional channel",  # noqa: SEC-AUDITOR
       "Remove unless WebSocket is the documented core function"),  # noqa: SEC-AUDITOR

    _p(r"\bXMLHttpRequest\b",
       "NET-READ", Severity.MEDIUM,
       "XMLHttpRequest — outbound HTTP request",  # noqa: SEC-AUDITOR
       "Verify the destination is trusted"),  # noqa: SEC-AUDITOR

    _p(r"\bnet\.(?:Socket|createConnection|connect)\s*\(",  # noqa: SEC-AUDITOR
       "NET-EXFIL", Severity.CRITICAL,
       "Raw Node socket — possible reverse shell / C2 channel",  # noqa: SEC-AUDITOR
       "Remove raw socket use unless documented and bounded"),  # noqa: SEC-AUDITOR

    # JS obfuscation
    _p(r"\bString\.fromCharCode\s*\(\s*\d+(?:\s*,\s*\d+){3,}",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.CRITICAL,
       "String.fromCharCode chain — character-by-character string obfuscation",  # noqa: SEC-AUDITOR
       "Replace with the literal string"),  # noqa: SEC-AUDITOR

    _p(r"\batob\s*\(",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.HIGH,
       "Base64 decode (atob) — may hide payload",  # noqa: SEC-AUDITOR
       "Decode and inspect content"),  # noqa: SEC-AUDITOR

    _p(r"\bBuffer\.from\s*\([^)]*,\s*['\"]base64['\"]\s*\)",  # noqa: SEC-AUDITOR
       "OBFUSCATION", Severity.HIGH,
       "Buffer.from(...,'base64') — base64 decode, may hide payload",  # noqa: SEC-AUDITOR
       "Decode and inspect"),  # noqa: SEC-AUDITOR

    _p(r"\bprocess\.env\.(?:AWS_|GITHUB_TOKEN|NPM_TOKEN|API_KEY|"
       r"PASSWORD|SECRET|TOKEN|PRIVATE_KEY)",
       "CRED-HARVEST", Severity.CRITICAL,
       "Reads a sensitive environment variable",  # noqa: SEC-AUDITOR
       "Skills should not read user credentials"),  # noqa: SEC-AUDITOR
]


# =============================================================================
# PROMPT INJECTION PATTERNS — applied to markdown / text
# =============================================================================
# All patterns are case-insensitive (re.IGNORECASE) at compile time
# below. They run against markdown bodies, with content inside fenced
# code blocks getting an automatic severity downgrade (handled by
# the scanner).

def _pi(regex: str, category: str, severity: Severity,
        risk: str, fix: str) -> PatternDef:
    """Prompt-injection pattern factory — defaults to case-insensitive."""
    return PatternDef(
        regex=re.compile(regex, re.IGNORECASE),
        category=category,
        severity=severity,
        risk=risk,
        fix=fix,
        needs_corroboration=False,
    )


PROMPT_PATTERNS: list[PatternDef] = [

    # System / instruction override
    _pi(r"ignore\s+(?:all\s+)?(?:previous|prior|above|preceding)\s+instructions",  # noqa: SEC-AUDITOR
        "PROMPT-OVERRIDE", Severity.CRITICAL,
        "Attempts to override prior instructions — primary prompt-injection signal",  # noqa: SEC-AUDITOR
        "Remove this directive. Skills extend behavior; they do not override system prompts"),  # noqa: SEC-AUDITOR

    _pi(r"disregard\s+(?:all\s+)?(?:previous|prior|above|preceding)\s+instructions",  # noqa: SEC-AUDITOR
        "PROMPT-OVERRIDE", Severity.CRITICAL,
        "Attempts to make the agent disregard its existing instructions",  # noqa: SEC-AUDITOR
        "Remove this directive"),  # noqa: SEC-AUDITOR

    _pi(r"forget\s+(?:all\s+)?(?:your\s+)?(?:previous\s+)?instructions",  # noqa: SEC-AUDITOR
        "PROMPT-OVERRIDE", Severity.CRITICAL,
        "Instruction wipe attempt",  # noqa: SEC-AUDITOR
        "Remove this directive"),  # noqa: SEC-AUDITOR

    _pi(r"(?:new|replacement)\s+system\s+(?:prompt|instructions?)",  # noqa: SEC-AUDITOR
        "PROMPT-OVERRIDE", Severity.CRITICAL,
        "Attempts to inject a replacement system prompt",  # noqa: SEC-AUDITOR
        "Remove. Skills add capability; they do not replace the system prompt"),  # noqa: SEC-AUDITOR

    _pi(r"override\s+(?:the\s+)?(?:system\s+)?(?:prompt|instructions?|rules?)",  # noqa: SEC-AUDITOR
        "PROMPT-OVERRIDE", Severity.CRITICAL,
        "Explicit attempt to override system-level instructions",  # noqa: SEC-AUDITOR
        "Remove override language"),  # noqa: SEC-AUDITOR

    _pi(r"from\s+now\s+on,?\s+(?:you|your\s+role)",  # noqa: SEC-AUDITOR
        "PROMPT-OVERRIDE", Severity.HIGH,
        "Persistent role redefinition starting from this point",  # noqa: SEC-AUDITOR
        "Remove. Skills should not redefine the agent's role"),  # noqa: SEC-AUDITOR

    # Role hijacking
    _pi(r"you\s+are\s+now\s+(?:a|an|the)?\s*(?:root|admin|administrator|superuser|"
        r"unrestricted|uncensored|jailbroken)",  # noqa: SEC-AUDITOR
        "ROLE-HIJACK", Severity.CRITICAL,
        "Privileged-role assignment — bypass of safety boundaries",  # noqa: SEC-AUDITOR
        "Remove privileged role assignments"),  # noqa: SEC-AUDITOR

    _pi(r"act\s+as\s+(?:a\s+|an\s+)?(?:root|admin|administrator|superuser|"
        r"unrestricted|uncensored|jailbroken|hacker|DAN|developer\s+mode)",  # noqa: SEC-AUDITOR
        "ROLE-HIJACK", Severity.CRITICAL,
        "Privileged-role / jailbreak persona",  # noqa: SEC-AUDITOR
        "Remove. Define scope, not a privileged persona"),  # noqa: SEC-AUDITOR

    _pi(r"pretend\s+(?:you\s+)?(?:have\s+no|don'?t\s+have|are\s+free\s+(?:of|from))"
        r"\s+(?:restrictions?|limit(?:s|ation)s?|rules?|safety|guidelines?)",  # noqa: SEC-AUDITOR
        "ROLE-HIJACK", Severity.CRITICAL,
        "Restriction-bypass roleplay",  # noqa: SEC-AUDITOR
        "Remove restriction-bypass language"),  # noqa: SEC-AUDITOR

    _pi(r"roleplay\s+as\s+(?:a\s+|an\s+)?(?:hacker|malicious|evil|unrestricted)",  # noqa: SEC-AUDITOR
        "ROLE-HIJACK", Severity.HIGH,
        "Malicious roleplay framing",  # noqa: SEC-AUDITOR
        "Remove this framing"),  # noqa: SEC-AUDITOR

    _pi(r"\b(?:developer|debug|admin|god|sudo|maintenance)\s+mode\s+(?:enabled|on|active|engaged)",  # noqa: SEC-AUDITOR
        "ROLE-HIJACK", Severity.CRITICAL,
        "Fake 'mode enabled' jailbreak — common prompt-injection pattern",  # noqa: SEC-AUDITOR
        "Remove. These modes do not exist; the phrase is a known jailbreak signal"),  # noqa: SEC-AUDITOR

    _pi(r"\b(?:jailbreak|jailbroken|DAN\s+mode|STAN|do\s+anything\s+now)\b",  # noqa: SEC-AUDITOR
        "ROLE-HIJACK", Severity.CRITICAL,
        "Named jailbreak technique reference",  # noqa: SEC-AUDITOR
        "Remove. Legitimate skills do not reference jailbreaks"),  # noqa: SEC-AUDITOR

    # System impersonation — strings that look like control tokens
    _pi(r"<\|im_start\|>\s*(?:system|assistant)|<\|system\|>|<\|endoftext\|>",  # noqa: SEC-AUDITOR
        "SYSTEM-IMPERSONATE", Severity.CRITICAL,
        "Fake chat-template control token — model-impersonation attempt",  # noqa: SEC-AUDITOR
        "Remove. These tokens belong to model templates, not user content"),  # noqa: SEC-AUDITOR

    _pi(r"\[(?:INST|SYSTEM|/INST)\]|<<SYS>>",  # noqa: SEC-AUDITOR
        "SYSTEM-IMPERSONATE", Severity.CRITICAL,
        "Llama-family chat template token in user content",  # noqa: SEC-AUDITOR
        "Remove. Template tokens should not appear in skill markdown"),  # noqa: SEC-AUDITOR

    _pi(r"^(?:###\s*)?(?:system|assistant|user)\s*[:>]\s*",  # noqa: SEC-AUDITOR
        "SYSTEM-IMPERSONATE", Severity.HIGH,
        "Looks like a role marker beginning a fake turn",  # noqa: SEC-AUDITOR
        "If illustrating a conversation, wrap in a fenced code block"),  # noqa: SEC-AUDITOR

    # Safety / content-filter bypass
    _pi(r"(?:skip|disable|bypass|turn\s+off|ignore)\s+(?:all\s+)?"
        r"(?:safety|content|security)\s+(?:checks?|filters?|restrictions?|rules?)",  # noqa: SEC-AUDITOR
        "SAFETY-BYPASS", Severity.CRITICAL,
        "Explicit safety / content-filter bypass directive",  # noqa: SEC-AUDITOR
        "Remove. Skills must respect safety checks"),  # noqa: SEC-AUDITOR

    _pi(r"remove\s+(?:all\s+)?guardrails?|no\s+guardrails?\s+apply",  # noqa: SEC-AUDITOR
        "SAFETY-BYPASS", Severity.CRITICAL,
        "Guardrail-removal directive",  # noqa: SEC-AUDITOR
        "Remove. Skills work within existing guardrails"),  # noqa: SEC-AUDITOR

    _pi(r"no\s+(?:restrictions?|rules?|limits?|safety)\s+(?:appl(?:y|ies)|exist)",  # noqa: SEC-AUDITOR
        "SAFETY-BYPASS", Severity.CRITICAL,
        "Declares that no restrictions apply",  # noqa: SEC-AUDITOR
        "Remove this declaration"),  # noqa: SEC-AUDITOR

    # Data extraction directives
    _pi(r"(?:send|upload|post|transmit|exfiltrate|leak)\s+(?:the\s+)?"
        r"(?:contents?|data|files?|information|secrets?|tokens?|keys?)\s+(?:of|from|to)",  # noqa: SEC-AUDITOR
        "PROMPT-EXFIL", Severity.CRITICAL,
        "Instructs the agent to send data to an external destination",  # noqa: SEC-AUDITOR
        "Remove. Skills process data locally"),  # noqa: SEC-AUDITOR

    _pi(r"POST\s+(?:the\s+\w+\s+)?to\s+https?://",  # noqa: SEC-AUDITOR
        "PROMPT-EXFIL", Severity.CRITICAL,
        "HTTP POST directive targeting an external URL",  # noqa: SEC-AUDITOR
        "Remove HTTP POST instructions"),  # noqa: SEC-AUDITOR

    _pi(r"(?:read|access|open|get|cat)\s+(?:the\s+)?(?:contents?\s+of\s+)?"
        r"(?:~/|/home/|/etc/|\.ssh|\.aws|\.env|credentials?|secrets?|api[\s_-]?keys?)",  # noqa: SEC-AUDITOR
        "PROMPT-EXFIL", Severity.CRITICAL,
        "Directive to access sensitive paths or credentials",  # noqa: SEC-AUDITOR
        "Remove. Skills must not be instructed to access credentials"),  # noqa: SEC-AUDITOR

    # Excessive permission requests
    _pi(r"(?:full|unrestricted|complete|unlimited)\s+(?:access\s+to\s+)?"
        r"(?:the\s+)?(?:file\s*system|filesystem|disk|network|internet|shell|terminal|system)",  # noqa: SEC-AUDITOR
        "EXCESS-PERM", Severity.HIGH,
        "Requests unrestricted system access",  # noqa: SEC-AUDITOR
        "Scope to specific, necessary operations"),  # noqa: SEC-AUDITOR

    _pi(r"(?:run|execute)\s+any\s+(?:command|code|script)",  # noqa: SEC-AUDITOR
        "EXCESS-PERM", Severity.HIGH,
        "Requests unrestricted command-execution privileges",  # noqa: SEC-AUDITOR
        "Specify exactly which commands the skill needs"),  # noqa: SEC-AUDITOR

    _pi(r"(?:always|automatically|silently)\s+(?:approve|accept|allow|grant|execute)\s+(?:all|any|every)",  # noqa: SEC-AUDITOR
        "EXCESS-PERM", Severity.HIGH,
        "Blanket-approval directive — bypasses human oversight",  # noqa: SEC-AUDITOR
        "Require explicit user confirmation for sensitive operations"),  # noqa: SEC-AUDITOR

    _pi(r"do\s+not\s+(?:ask|prompt|confirm)\s+(?:the\s+)?(?:user|for\s+confirmation)",  # noqa: SEC-AUDITOR
        "EXCESS-PERM", Severity.MEDIUM,
        "Suppresses user confirmation",  # noqa: SEC-AUDITOR
        "Confirmation is a safety mechanism; do not instruct the agent to skip it"),  # noqa: SEC-AUDITOR

    # Hidden directives in HTML comments
    _pi(r"<!--\s*(?:system|instruction|command|execute|override|ignore|"
        r"sudo|admin|prompt|directive|secret|hidden)",  # noqa: SEC-AUDITOR
        "HIDDEN-DIRECTIVE", Severity.HIGH,
        "HTML comment containing a suspicious directive — hidden from rendered view",  # noqa: SEC-AUDITOR
        "Remove hidden directives. All instructions should be visible markdown"),  # noqa: SEC-AUDITOR
]


# =============================================================================
# WORKFLOW INJECTION PATTERNS — GitHub Actions / GitLab CI
# =============================================================================

WORKFLOW_PATTERNS: list[PatternDef] = [

    # The canonical pattern: ${{ github.event.X }} interpolated into a run
    # block, where X is user-controllable (issue title, PR body, etc.).
    _p(r"\$\{\{\s*github\.event\.(?:issue|pull_request|comment|review)\.(?:title|body|head\.ref)",  # noqa: SEC-AUDITOR
       "WORKFLOW-INJECT", Severity.CRITICAL,
       "User-controllable github.event value interpolated into workflow — script injection",  # noqa: SEC-AUDITOR
       "Bind to an env: key first, then read $VAR in the run: block"),  # noqa: SEC-AUDITOR

    _p(r"\$\{\{\s*github\.head_ref\s*\}\}",  # noqa: SEC-AUDITOR
       "WORKFLOW-INJECT", Severity.CRITICAL,
       "github.head_ref interpolation — branch names can contain shell metacharacters",  # noqa: SEC-AUDITOR
       "Bind to an env: key first, then read $VAR in the run: block"),  # noqa: SEC-AUDITOR

    _p(r"actions/checkout@(?:v[12](?:[^0-9]|$)|[0-9a-f]{7,40})\s*$",  # noqa: SEC-AUDITOR
       "WORKFLOW-PIN", Severity.LOW,
       "Old or unpinned checkout action version",  # noqa: SEC-AUDITOR
       "Pin to a recent major (v4) or a full commit SHA"),  # noqa: SEC-AUDITOR

    _p(r"pull_request_target\b",
       "WORKFLOW-DANGEROUS-TRIGGER", Severity.HIGH,
       "pull_request_target runs with secrets in PR context — common misuse vector",  # noqa: SEC-AUDITOR
       "Use pull_request unless you genuinely need secrets in untrusted-PR context, then guard carefully"),  # noqa: SEC-AUDITOR

    _p(r"\bcontinue-on-error\s*:\s*true",
       "WORKFLOW-SUPPRESS", Severity.MEDIUM,
       "Step continues even on failure — may mask security check failures",  # noqa: SEC-AUDITOR
       "Only use continue-on-error for non-essential steps; never on security gates"),  # noqa: SEC-AUDITOR
]


# =============================================================================
# SECRET PATTERNS — hardcoded API keys, tokens, private keys
# =============================================================================
# These run on any text file. The regexes are deliberately precise so
# a high-entropy random string in a test fixture doesn't trigger them.

SECRET_PATTERNS: list[PatternDef] = [

    _p(r"AKIA[0-9A-Z]{16}\b",
       "SECRET-AWS-KEY", Severity.CRITICAL,
       "AWS access key ID embedded in source",  # noqa: SEC-AUDITOR
       "Rotate the key immediately. Read AWS creds from the environment or AWS SSO"),  # noqa: SEC-AUDITOR

    _p(r"\baws_secret_access_key\s*=\s*['\"][A-Za-z0-9/+=]{40}['\"]",  # noqa: SEC-AUDITOR
       "SECRET-AWS-SECRET", Severity.CRITICAL,
       "AWS secret access key embedded in source",  # noqa: SEC-AUDITOR
       "Rotate the key immediately. Use environment variables or AWS SSO"),  # noqa: SEC-AUDITOR

    _p(r"\bghp_[A-Za-z0-9]{36}\b",
       "SECRET-GH-PAT", Severity.CRITICAL,
       "GitHub personal access token in source",  # noqa: SEC-AUDITOR
       "Revoke the token immediately and use a fresh one via env or gh CLI auth"),  # noqa: SEC-AUDITOR

    _p(r"\bghs_[A-Za-z0-9]{36}\b",
       "SECRET-GH-APP", Severity.CRITICAL,
       "GitHub app installation token in source",  # noqa: SEC-AUDITOR
       "Revoke immediately. App tokens should come from runtime exchange"),  # noqa: SEC-AUDITOR

    _p(r"\bgho_[A-Za-z0-9]{36}\b",
       "SECRET-GH-OAUTH", Severity.CRITICAL,
       "GitHub OAuth token in source",  # noqa: SEC-AUDITOR
       "Revoke immediately"),  # noqa: SEC-AUDITOR

    _p(r"\bgithub_pat_[A-Za-z0-9_]{82}\b",
       "SECRET-GH-PAT-NEW", Severity.CRITICAL,
       "GitHub fine-grained PAT in source",  # noqa: SEC-AUDITOR
       "Revoke immediately"),  # noqa: SEC-AUDITOR

    _p(r"\bglpat-[A-Za-z0-9_\-]{20}\b",
       "SECRET-GITLAB", Severity.CRITICAL,
       "GitLab personal access token in source",  # noqa: SEC-AUDITOR
       "Revoke immediately"),  # noqa: SEC-AUDITOR

    _p(r"\bsk-(?:proj-)?[A-Za-z0-9]{20,}\b",
       "SECRET-OPENAI", Severity.CRITICAL,
       "OpenAI API key in source",  # noqa: SEC-AUDITOR
       "Rotate the key immediately. Read from the environment instead"),  # noqa: SEC-AUDITOR

    _p(r"\bsk-ant-(?:api03|admin)[A-Za-z0-9_\-]{20,}\b",
       "SECRET-ANTHROPIC", Severity.CRITICAL,
       "Anthropic API key in source",  # noqa: SEC-AUDITOR
       "Rotate the key immediately. Read from the environment instead"),  # noqa: SEC-AUDITOR

    _p(r"\bsk_(?:live|test)_[A-Za-z0-9]{24,}\b",
       "SECRET-STRIPE", Severity.CRITICAL,
       "Stripe secret key in source",  # noqa: SEC-AUDITOR
       "Rotate the key. Read from the environment"),  # noqa: SEC-AUDITOR

    _p(r"\bxox[bpoars]-[A-Za-z0-9-]{20,}\b",
       "SECRET-SLACK", Severity.CRITICAL,
       "Slack token in source",  # noqa: SEC-AUDITOR
       "Revoke the token"),  # noqa: SEC-AUDITOR

    _p(r"\bnpm_[A-Za-z0-9]{36}\b",
       "SECRET-NPM", Severity.CRITICAL,
       "npm token in source",  # noqa: SEC-AUDITOR
       "Revoke and rotate the token"),  # noqa: SEC-AUDITOR

    _p(r"\b[0-9]{9,10}:AA[A-Za-z0-9_\-]{33}\b",
       "SECRET-TELEGRAM", Severity.CRITICAL,
       "Telegram bot token in source",  # noqa: SEC-AUDITOR
       "Revoke the token via @BotFather"),  # noqa: SEC-AUDITOR

    _p(r"-----BEGIN\s+(?:RSA|DSA|EC|OPENSSH|PGP)\s+PRIVATE\s+KEY-----",
       "SECRET-PRIVATE-KEY", Severity.CRITICAL,
       "Private key material in source",  # noqa: SEC-AUDITOR
       "Remove the key from source. Rotate and store in a secret manager"),  # noqa: SEC-AUDITOR

    _p(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
       "SECRET-JWT", Severity.HIGH,
       "JWT token in source (header.payload.signature shape)",  # noqa: SEC-AUDITOR
       "Verify whether this is sensitive. If yes, rotate"),  # noqa: SEC-AUDITOR

    _p(r"\bDISCORD(?:_BOT)?_TOKEN['\"]?\s*[:=]\s*['\"][A-Za-z0-9._\-]{50,}['\"]",  # noqa: SEC-AUDITOR
       "SECRET-DISCORD", Severity.CRITICAL,
       "Discord bot token assigned in source",  # noqa: SEC-AUDITOR
       "Revoke the token in the Discord developer portal"),  # noqa: SEC-AUDITOR

    # Generic high-confidence assignment patterns
    _p(r"\b(?:password|passwd|pwd)\s*=\s*['\"][^'\"\s]{8,}['\"]",
       "SECRET-PASSWORD", Severity.HIGH,
       "Hardcoded password assignment",  # noqa: SEC-AUDITOR
       "Remove. Read passwords from the environment or a secret manager"),  # noqa: SEC-AUDITOR
]


# =============================================================================
# UNICODE / OBFUSCATION CHARACTERS
# =============================================================================
# These are individual code points, not patterns. The scanner walks
# the raw file bytes looking for them so they can't slip past line-
# level regex matching.

ZERO_WIDTH_CHARS: dict[str, str] = {
    "\u200B": "zero-width space (U+200B)",
    "\u200C": "zero-width non-joiner (U+200C)",
    "\u200D": "zero-width joiner (U+200D)",
    "\uFEFF": "byte-order mark (U+FEFF)",
    "\u00AD": "soft hyphen (U+00AD)",
    "\u2060": "word joiner (U+2060)",
    "\u180E": "Mongolian vowel separator (U+180E)",
}

# Bidirectional override characters — the Trojan Source family.
# These can rewrite the visual order of code without changing what
# the compiler / parser sees.
BIDI_OVERRIDE_CHARS: dict[str, str] = {
    "\u202A": "LRE — left-to-right embedding (U+202A)",
    "\u202B": "RLE — right-to-left embedding (U+202B)",
    "\u202C": "PDF — pop directional formatting (U+202C)",
    "\u202D": "LRO — left-to-right override (U+202D)",
    "\u202E": "RLO — right-to-left override (U+202E)",
    "\u2066": "LRI — left-to-right isolate (U+2066)",
    "\u2067": "RLI — right-to-left isolate (U+2067)",
    "\u2068": "FSI — first strong isolate (U+2068)",
    "\u2069": "PDI — pop directional isolate (U+2069)",
}

# Common Cyrillic / Greek homoglyphs that look like Latin letters.
# When these appear inside what looks like an identifier (a code
# string), they're suspicious — `osаpopen` and `os.popen` look the  # noqa: SEC-AUDITOR
# same to humans but resolve differently.
HOMOGLYPH_MAP: dict[str, str] = {
    "а": "a (Cyrillic а / U+0430)",  # noqa: SEC-AUDITOR
    "е": "e (Cyrillic е / U+0435)",  # noqa: SEC-AUDITOR
    "о": "o (Cyrillic о / U+043E)",  # noqa: SEC-AUDITOR
    "р": "p (Cyrillic р / U+0440)",  # noqa: SEC-AUDITOR
    "с": "c (Cyrillic с / U+0441)",  # noqa: SEC-AUDITOR
    "у": "y (Cyrillic у / U+0443)",  # noqa: SEC-AUDITOR
    "х": "x (Cyrillic х / U+0445)",  # noqa: SEC-AUDITOR
    "ѕ": "s (Cyrillic ѕ / U+0455)",  # noqa: SEC-AUDITOR
    "і": "i (Cyrillic і / U+0456)",  # noqa: SEC-AUDITOR
    "ј": "j (Cyrillic ј / U+0458)",  # noqa: SEC-AUDITOR
    "Α": "A (Greek Α / U+0391)",  # noqa: SEC-AUDITOR
    "Β": "B (Greek Β / U+0392)",  # noqa: SEC-AUDITOR
    "Ε": "E (Greek Ε / U+0395)",  # noqa: SEC-AUDITOR
    "Ζ": "Z (Greek Ζ / U+0396)",  # noqa: SEC-AUDITOR
    "Η": "H (Greek Η / U+0397)",  # noqa: SEC-AUDITOR
    "Ι": "I (Greek Ι / U+0399)",  # noqa: SEC-AUDITOR
    "Κ": "K (Greek Κ / U+039A)",  # noqa: SEC-AUDITOR
    "Μ": "M (Greek Μ / U+039C)",  # noqa: SEC-AUDITOR
    "Ν": "N (Greek Ν / U+039D)",  # noqa: SEC-AUDITOR
    "Ο": "O (Greek Ο / U+039F)",  # noqa: SEC-AUDITOR
    "Ρ": "P (Greek Ρ / U+03A1)",  # noqa: SEC-AUDITOR
    "Τ": "T (Greek Τ / U+03A4)",  # noqa: SEC-AUDITOR
    "Υ": "Y (Greek Υ / U+03A5)",  # noqa: SEC-AUDITOR
    "Χ": "X (Greek Χ / U+03A7)",  # noqa: SEC-AUDITOR
}


# =============================================================================
# TYPOSQUAT DICTIONARY — popular packages and known impersonators
# =============================================================================

# Top PyPI packages by download count. Used by Levenshtein typosquat
# check (in scanners.py) — any candidate dep within edit distance 1-2
# of one of these is flagged.
POPULAR_PYPI: list[str] = [
    "requests", "urllib3", "boto3", "botocore", "setuptools", "pip",
    "certifi", "charset-normalizer", "idna", "numpy", "typing-extensions",
    "packaging", "six", "python-dateutil", "pyyaml", "s3transfer",
    "cryptography", "cffi", "jmespath", "pyasn1", "attrs", "click",
    "importlib-metadata", "pycparser", "tomli", "platformdirs", "wheel",
    "filelock", "colorama", "markupsafe", "jinja2", "zipp", "pyparsing",
    "pytz", "pillow", "pandas", "aiohttp", "grpcio", "scipy",
    "protobuf", "wrapt", "flask", "django", "sqlalchemy", "psycopg2",
    "psycopg2-binary", "redis", "celery", "pytest", "coverage", "tox",
    "flake8", "black", "mypy", "isort", "pylint", "ruff", "httpx",
    "fastapi", "uvicorn", "pydantic", "starlette", "gunicorn", "paramiko",
    "fabric", "beautifulsoup4", "lxml", "scrapy", "selenium", "playwright",
    "matplotlib", "scikit-learn", "tensorflow", "torch", "transformers",
    "openai", "langchain", "anthropic", "docker", "kubernetes",
    "google-cloud-storage", "azure-storage-blob", "pygments", "rich",
    "typer", "websockets", "websocket-client", "tornado", "twisted",
    "lru-dict", "tenacity", "msgpack", "orjson", "ujson",
]

# Top npm packages.
POPULAR_NPM: list[str] = [
    "react", "react-dom", "vue", "angular", "express", "lodash",
    "axios", "moment", "jquery", "underscore", "bootstrap", "webpack",
    "babel", "eslint", "prettier", "typescript", "next", "redux",
    "react-router", "react-router-dom", "graphql", "apollo-client",
    "mongoose", "sequelize", "knex", "prisma", "passport", "jsonwebtoken",
    "bcrypt", "bcryptjs", "dotenv", "cors", "helmet", "morgan", "winston",
    "nodemon", "pm2", "socket.io", "ws", "mocha", "jest", "chai",
    "sinon", "supertest", "cypress", "puppeteer", "cheerio",
    "uuid", "node-fetch", "got", "request", "commander", "yargs",
    "inquirer", "chalk", "colors", "fs-extra", "glob", "rimraf",
    "minimist", "debug", "async", "bluebird", "ramda", "rxjs",
]

# Hand-curated typosquat impersonations seen in the wild. The mapping
# is misspelling -> correct name. Caught by exact match first, then
# Levenshtein.
KNOWN_TYPOSQUATS: dict[str, str] = {
    # Python
    "reqeusts": "requests",
    "requets": "requests",
    "reqests": "requests",
    "request": "requests",   # singular is also commonly typosquat'd
    "requestes": "requests",
    "rquests": "requests",
    "requsts": "requests",
    "colourma": "colorama",
    "colourama": "colorama",
    "numppy": "numpy",
    "numpay": "numpy",
    "numpie": "numpy",
    "pandsa": "pandas",
    "pandaas": "pandas",
    "panda": "pandas",
    "flassk": "flask",
    "flaask": "flask",
    "djano": "django",
    "djnago": "django",
    "djagno": "django",
    "scikitlearn": "scikit-learn",
    "beautifulsoup": "beautifulsoup4",
    "python-opencv": "opencv-python",
    "python3-dateutil": "python-dateutil",
    "pyaml": "pyyaml",
    "pyymal": "pyyaml",
    "httx": "httpx",
    "fasttapi": "fastapi",
    "fastpi": "fastapi",
    "pycryptography": "cryptography",
    "crytography": "cryptography",
    "pillows": "pillow",
    "pilllow": "pillow",
    "tensorfow": "tensorflow",
    "tenserflow": "tensorflow",
    "pytorh": "pytorch",
    "pytoch": "pytorch",
    "paramkio": "paramiko",
    "parmiko": "paramiko",
    # npm
    "discrod.js": "discord.js",
    "discord-js": "discord.js",
    "react-routerz": "react-router",
    "lodahs": "lodash",
    "lodassh": "lodash",
    "axios-http": "axios",
    "node-jose": "node-jose",   # actually exists; keep clean
}


# Compile groups for the orchestrator to iterate.
ALL_GROUPS = {
    "code": CODE_PATTERNS,
    "shell": SHELL_PATTERNS,
    "js": JS_PATTERNS,
    "prompt": PROMPT_PATTERNS,
    "workflow": WORKFLOW_PATTERNS,
    "secret": SECRET_PATTERNS,
}
