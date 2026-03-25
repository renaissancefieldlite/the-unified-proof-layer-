from __future__ import annotations

import argparse
import json

from .unified_source_proof import EverythingIsEverything


def main() -> dict:
    parser = argparse.ArgumentParser(description="Run the unified proof layer.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    report = EverythingIsEverything().execute_unified_proof()
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("Unified Proof Layer")
        print("=" * 60)
        for key, value in report.items():
            print(f"{key}: {value}")
    return report


if __name__ == "__main__":
    main()
