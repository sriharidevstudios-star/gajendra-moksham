#!/usr/bin/env python3
"""Validate canonical Gajendra source readiness offline; no generated files."""

import argparse
import json
from pathlib import Path
from content_model import validate_project

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--episode", help="S01E01–S01E06")
    parser.add_argument("--scene", help="S01–S06; requires --episode")
    parser.add_argument("--require-complete", action="store_true", help="Reject scoped partial episode")
    args = parser.parse_args(argv)
    report = validate_project(args.root, args.episode, args.scene, args.require_complete)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return {"FAIL": 1, "NOT_READY": 2}.get(report["status"], 0)


if __name__ == "__main__":
    raise SystemExit(main())
