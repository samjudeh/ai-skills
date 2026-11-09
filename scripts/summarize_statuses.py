#!/usr/bin/env python3
"""Count status codes in a CSV with timestamp and status_code columns."""

import csv
import sys
from collections import Counter
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python summarize_statuses.py <csv-path>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    counts = Counter()
    rows = 0

    with path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        required = {"timestamp", "status_code"}

        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            print("CSV must contain timestamp and status_code columns.",
                  file=sys.stderr)
            return 2

        for row in reader:
            rows += 1
            status = (row["status_code"] or "").strip()
            counts[status or "(blank)"] += 1

    print(f"Rows: {rows}")
    for status, count in sorted(counts.items()):
        print(f"{status}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
