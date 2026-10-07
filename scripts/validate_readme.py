#!/usr/bin/env python3
"""Validate the paper tables in README.md: row structure, links, chronology, and counts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LINK = re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")
COUNT = re.compile(r"^\*\*Analyzed in the survey \((\d+)\)\*\*$")
EVIDENCE = {"Physical", "Sim + physical", "Sim-to-real", "Simulation", "Unclear"}
REGIMES = {
    "Open loop",
    "Step-level",
    "Within-rollout memory",
    "Cross-rollout memory",
    "Persistent modification",
}
DECISIONS = {"●", "○", "–"}
REQUIRED_SECTIONS = [
    "Task orchestration (T)",
    "Motion/action generation (M)",
    "Task and motion (T + M)",
    "Fixed-procedure improvement (I_fixed)",
    "Agent-directed improvement (I_agent)",
]


def cells(line: str) -> list[str]:
    # Split on unescaped pipes only.
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def main() -> int:
    lines = README.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    seen_urls: dict[str, int] = {}
    sections = [l[4:].strip() for l in lines if l.startswith("### ")]
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            errors.append(f"missing section '### {name}'")

    header: list[str] | None = None
    previous_year: int | None = None
    declared: tuple[int, int] | None = None  # (line number, declared count)
    rows_in_table = 0
    totals: dict[str, int] = {}
    section = ""

    def close_table(line_number: int) -> None:
        nonlocal declared
        if declared and header is not None:
            if rows_in_table != declared[1]:
                errors.append(
                    f"line {declared[0]}: declared {declared[1]} systems "
                    f"but the table has {rows_in_table} rows"
                )
            declared = None

    for n, line in enumerate(lines, start=1):
        if line.startswith(("## ", "### ")):
            section = line.lstrip("#").strip()
        if m := COUNT.match(line):
            declared = (n, int(m.group(1)))
        if not line.startswith("|"):
            if header is not None:
                close_table(n)
            header = None
            continue
        row = cells(line)
        if header is None:
            header = row
            previous_year, rows_in_table = None, 0
            continue
        if set(line) <= set("|-: "):
            continue
        if header[0] != "Year":
            continue

        rows_in_table += 1
        if len(row) != len(header):
            errors.append(f"line {n}: {len(row)} cells, expected {len(header)}")
            continue
        record = dict(zip(header, row))

        if not re.fullmatch(r"20\d\d", record["Year"]):
            errors.append(f"line {n}: year must be YYYY, got '{record['Year']}'")
        else:
            year = int(record["Year"])
            if previous_year is not None and year > previous_year:
                errors.append(f"line {n}: {year} breaks newest-first order in '{section}'")
            previous_year = year

        paper = record.get("System and paper") or record.get("Paper", "")
        links = LINK.findall(paper)
        if len(links) != 1:
            errors.append(f"line {n}: expected exactly one HTTPS paper link")
        else:
            url = links[0]
            if url in seen_urls:
                errors.append(f"line {n}: duplicate paper URL first used on line {seen_urls[url]}")
            seen_urls[url] = n

        if not record.get("Venue"):
            errors.append(f"line {n}: missing venue")
        if "Evidence" in record and record["Evidence"] not in EVIDENCE:
            errors.append(f"line {n}: unknown evidence label '{record['Evidence']}'")
        if "Feedback regime" in record and record["Feedback regime"] not in REGIMES:
            errors.append(f"line {n}: unknown feedback regime '{record['Feedback regime']}'")
        for key in ("D1", "D2", "D3", "D4"):
            if key in record and record[key] not in DECISIONS:
                errors.append(f"line {n}: {key} must be one of {sorted(DECISIONS)}")
        for key in ("Summary", "Feedback closure", "Scope"):
            if key in record and not record[key].endswith("."):
                errors.append(f"line {n}: '{key}' must end as a sentence")
        totals[section] = totals.get(section, 0) + 1

    if header is not None:
        close_table(len(lines))

    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    if errors:
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {sum(totals.values())} rows.")
    for name, count in totals.items():
        print(f"  {count:3d}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
