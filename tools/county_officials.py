#!/usr/bin/env python3
"""Turn an HTML table of elected officials into data/generated/officials.json (Class 5).

Standard library only. The county publishes officials as an HTML table; this
script is deliberately generic so students can point it at the real page and
adjust the column mapping.

    # from a live page (find the real URL together in class)
    python3 tools/county_officials.py --url "https://EXAMPLE/officials" \
        --table-index 0 \
        --map "Name=name,Office=office,Phone=phone,Email=email"

    # from a saved copy (good for offline work and for tests)
    python3 tools/county_officials.py --file tools/raw/officials.html --list-tables

Steps: 1) --list-tables to see what tables exist and their headers,
2) pick one with --table-index, 3) map header text to our field names with
--map (left = header as shown on the page, right = JSON field).

Be a good citizen: run it occasionally (not on every build), keep the
User-Agent honest, and check the site's terms and robots.txt.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

USER_AGENT = "kitsap-local-learning-project/0.1 (educational; contact: set-your-email)"


class TableParser(HTMLParser):
    """Collects every <table> as a list of rows of {text, href} cells."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[dict]]] = []
        self._depth = 0
        self._row: list[dict] | None = None
        self._cell: dict | None = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self._depth += 1
            if self._depth == 1:
                self.tables.append([])
        elif self._depth == 1 and tag == "tr":
            self._row = []
        elif self._depth == 1 and tag in ("td", "th") and self._row is not None:
            self._cell = {"text": "", "href": None}
        elif tag == "a" and self._cell is not None and not self._cell["href"]:
            self._cell["href"] = dict(attrs).get("href")
        elif tag == "br" and self._cell is not None:
            self._cell["text"] += " "

    def handle_endtag(self, tag):
        if tag == "table":
            self._depth = max(0, self._depth - 1)
        elif self._depth == 1 and tag in ("td", "th") and self._cell is not None and self._row is not None:
            self._cell["text"] = " ".join(self._cell["text"].split())
            self._row.append(self._cell)
            self._cell = None
        elif self._depth == 1 and tag == "tr" and self._row is not None:
            if self._row:
                self.tables[-1].append(self._row)
            self._row = None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell["text"] += data


def load_html(args) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(args.url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def parse_map(s: str) -> dict[str, str]:
    out = {}
    for pair in s.split(","):
        if "=" in pair:
            k, v = pair.split("=", 1)
            out[k.strip().lower()] = v.strip()
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url")
    src.add_argument("--file")
    ap.add_argument("--table-index", type=int, default=0)
    ap.add_argument("--map", default="Name=name,Office=office,Phone=phone,Email=email",
                    help="header=field pairs, comma separated")
    ap.add_argument("--list-tables", action="store_true")
    ap.add_argument("--out", type=Path, default=Path("data/generated/officials.json"))
    args = ap.parse_args()

    parser = TableParser()
    parser.feed(load_html(args))

    if args.list_tables:
        for i, t in enumerate(parser.tables):
            header = [c["text"] for c in t[0]] if t else []
            print(f"[{i}] {len(t)} rows, header: {header}")
        return 0

    if not parser.tables:
        print("ERROR: no <table> found on the page", file=sys.stderr)
        return 1
    table = parser.tables[args.table_index]
    header = [c["text"].strip().lower() for c in table[0]]
    mapping = parse_map(args.map)

    missing = [h for h in mapping if h not in header]
    if missing:
        print(f"ERROR: mapped headers not found: {missing}; page has {header}", file=sys.stderr)
        return 1

    officials = []
    for row in table[1:]:
        rec = {}
        for h, field in mapping.items():
            cell = row[header.index(h)] if header.index(h) < len(row) else {"text": "", "href": None}
            rec[field] = cell["text"]
            if cell["href"]:
                rec[f"{field}Link"] = cell["href"]
        if any(v for k, v in rec.items() if not k.endswith("Link")):
            officials.append(rec)

    payload = {
        "version": 1,
        "source": args.url or str(args.file),
        "retrieved": date.today().isoformat(),
        "officials": officials,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {args.out} ({len(officials)} officials)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
