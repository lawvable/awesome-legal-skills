#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def copy_if_missing(src: Path, dst: Path, force: bool) -> None:
    if dst.exists() and not force:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Initialize reusable contract-review workspace files."
    )
    parser.add_argument(
        "--workspace",
        default=".",
        help="Workspace root where CLAUDE.md and .contract-review/ should be created.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing template files.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent / "assets" / "templates"
    workspace = Path(args.workspace).resolve()

    copy_if_missing(
        template_root / "CLAUDE.md.template",
        workspace / "CLAUDE.md",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "config.yaml",
        workspace / ".contract-review" / "config.yaml",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "connectors.yaml",
        workspace / ".contract-review" / "connectors.yaml",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "workflow-tools.yaml",
        workspace / ".contract-review" / "workflow-tools.yaml",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "approvals.yaml",
        workspace / ".contract-review" / "approvals.yaml",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "memory-policy.yaml",
        workspace / ".contract-review" / "memory-policy.yaml",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "playbooks" / "metadata.yaml.template",
        workspace / ".contract-review" / "playbooks" / "metadata.yaml.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "playbooks" / "source.md.template",
        workspace / ".contract-review" / "playbooks" / "source.md.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "playbooks" / "normalized.yaml.template",
        workspace / ".contract-review" / "playbooks" / "normalized.yaml.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "contract.yaml.template",
        workspace / ".contract-review" / "contracts" / "contract.yaml.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "action-packet.yaml.template",
        workspace / ".contract-review" / "contracts" / "action-packet.yaml.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "workflow-state.yaml.template",
        workspace / ".contract-review" / "contracts" / "workflow-state.yaml.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "review-summary.json.template",
        workspace / ".contract-review" / "contracts" / "review-summary.json.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "approval-routing.json.template",
        workspace / ".contract-review" / "contracts" / "approval-routing.json.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "metrics.yaml.template",
        workspace / ".contract-review" / "contracts" / "metrics.yaml.template",
        args.force,
    )
    copy_if_missing(
        template_root / ".contract-review" / "contracts" / "playbook-comparison.csv.template",
        workspace / ".contract-review" / "contracts" / "playbook-comparison.csv.template",
        args.force,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
