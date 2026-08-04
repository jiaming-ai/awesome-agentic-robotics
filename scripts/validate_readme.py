#!/usr/bin/env python3
"""Validate paper-table structure and chronology in README.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ROW = re.compile(
    r"^\| (?P<date>\d{4})-(?P<month>\d{2}) "
    r"\| (?P<paper>.+?) \| (?P<venue>.+?) "
    r"\| (?P<evidence>.+?) \| (?P<summary>.+?) \|$"
)
LINK = re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")
ALLOWED_EVIDENCE = {
    "Physical",
    "Sim + physical",
    "Sim-to-real",
    "Simulation",
    "Review",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    text = README.read_text(encoding="utf-8")
    errors = 0
    section = ""
    previous_date: tuple[int, int] | None = None
    seen_urls: dict[str, int] = {}
    paper_count = 0
    section_counts: dict[str, int] = {}

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            section = line[3:].strip()
            previous_date = None
            continue

        if not line.startswith("| 20"):
            continue

        match = ROW.fullmatch(line)
        if not match:
            fail(f"line {line_number}: malformed paper row")
            errors += 1
            continue

        year = int(match.group("date"))
        month = int(match.group("month"))
        current_date = (year, month)
        if not 1 <= month <= 12:
            fail(f"line {line_number}: invalid month {month:02d}")
            errors += 1
        if previous_date is not None and current_date > previous_date:
            fail(
                f"line {line_number}: {year}-{month:02d} is out of "
                f"reverse-chronological order in '{section}'"
            )
            errors += 1
        previous_date = current_date

        evidence = match.group("evidence")
        if evidence not in ALLOWED_EVIDENCE:
            fail(f"line {line_number}: unknown evidence label '{evidence}'")
            errors += 1

        links = LINK.findall(match.group("paper"))
        if len(links) != 1:
            fail(f"line {line_number}: expected exactly one HTTPS paper link")
            errors += 1
        else:
            url = links[0]
            if url in seen_urls:
                fail(
                    f"line {line_number}: duplicate paper URL first used "
                    f"on line {seen_urls[url]}"
                )
                errors += 1
            seen_urls[url] = line_number

        if not match.group("venue").strip():
            fail(f"line {line_number}: missing venue")
            errors += 1
        summary = match.group("summary").strip()
        if not summary.endswith((".", "!", "?")):
            fail(f"line {line_number}: summary must end as a sentence")
            errors += 1

        paper_count += 1
        section_counts[section] = section_counts.get(section, 0) + 1

    if paper_count == 0:
        fail("no paper rows found")
        return 1

    declared = re.search(r"> \*\*(\d+) works", text)
    if not declared:
        fail("missing declared work count")
        errors += 1
    elif int(declared.group(1)) != paper_count:
        fail(
            f"declared {declared.group(1)} works but found {paper_count} paper rows"
        )
        errors += 1

    if len(section_counts) != 8:
        fail(f"expected 8 populated literature categories, found {len(section_counts)}")
        errors += 1

    if errors:
        print(f"Validation failed with {errors} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {paper_count} works across {len(section_counts)} categories.")
    for name, count in section_counts.items():
        print(f"  {count:2d}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
