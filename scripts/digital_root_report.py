#!/usr/bin/env python3
"""Generate a simple digital-root frequency report from data/templates or data corpus files.

Usage:
  python scripts/digital_root_report.py --input data/templates/message-samples.template.csv
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def digital_root(number_text: str) -> int:
    digits = [int(c) for c in number_text if c.isdigit()]
    if not digits:
        return 0
    value = sum(digits)
    while value > 9:
        value = sum(int(c) for c in str(value))
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV file with a digits_only column")
    args = parser.parse_args()

    csv_path = Path(args.input)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    counts: Counter[int] = Counter()
    missing = 0
    for row in rows:
        digits_only = (row.get("digits_only") or "").strip()
        if not digits_only:
            missing += 1
            continue
        counts[digital_root(digits_only)] += 1

    print(f"input_rows={len(rows)}")
    print(f"rows_with_digits={sum(counts.values())}")
    print(f"rows_missing_digits={missing}")
    for root in sorted(counts):
        print(f"root_{root}={counts[root]}")


if __name__ == "__main__":
    main()
