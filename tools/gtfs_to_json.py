#!/usr/bin/env python3
"""Validate a GTFS zip and convert it to slim JSON for the app (Class 6).

Standard library only. Usage:

    python3 tools/gtfs_to_json.py path/to/gtfs.zip
    python3 tools/gtfs_to_json.py path/to/gtfs.zip --out data/generated --strict

What it does
  1. VALIDATE: counts routes/stops/trips, reads service dates from
     feed_info.txt and calendar.txt, flags expired feeds, and reports whether
     any route looks like a ferry (route_type 4 or extended 1200-1299).
  2. CONVERT: writes routes.json, stops.json, shapes.json (simplified) and a
     gtfs_report.json into --out.

The point of the validation step is to answer, BEFORE building UI, questions
like "does this feed cover Bremerton and Poulsbo?", "is it current?", and
"do the ferry routes come from here or from WSDOT?".
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROUTE_TYPE_NAMES = {
    0: "tram", 1: "subway", 2: "rail", 3: "bus", 4: "ferry",
    5: "cable tram", 6: "aerial lift", 7: "funicular", 11: "trolleybus",
    12: "monorail",
}


def route_type_name(t: int) -> str:
    if t in ROUTE_TYPE_NAMES:
        return ROUTE_TYPE_NAMES[t]
    if 100 <= t < 200:
        return "rail (extended)"
    if 200 <= t < 300:
        return "coach (extended)"
    if 700 <= t < 800:
        return "bus (extended)"
    if 1200 <= t < 1300:
        return "ferry (extended)"
    return f"other ({t})"


def is_ferry(t: int) -> bool:
    return t == 4 or 1200 <= t < 1300


def read_rows(z: zipfile.ZipFile, name: str):
    """Stream rows of a GTFS text file as dicts (empty if file is absent)."""
    if name not in z.namelist():
        return
    with z.open(name) as raw:
        yield from csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"))


def parse_gtfs_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.strptime(s.strip(), "%Y%m%d").date()
    except ValueError:
        return None


# --- shape simplification (Douglas-Peucker, iterative) -----------------------

def _seg_dist(p, a, b) -> float:
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def simplify(points: list[tuple[float, float]], eps: float) -> list[tuple[float, float]]:
    if len(points) < 3:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        s, e = stack.pop()
        dmax, idx = 0.0, None
        for i in range(s + 1, e):
            d = _seg_dist(points[i], points[s], points[e])
            if d > dmax:
                dmax, idx = d, i
        if idx is not None and dmax > eps:
            keep[idx] = True
            stack.append((s, idx))
            stack.append((idx, e))
    return [p for p, k in zip(points, keep) if k]


# --- main --------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("gtfs_zip", type=Path)
    ap.add_argument("--out", type=Path, default=Path("data/generated"))
    ap.add_argument("--tolerance", type=float, default=0.00005,
                    help="shape simplification tolerance in degrees (~5 m)")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if validation finds errors")
    ap.add_argument("--validate-only", action="store_true")
    args = ap.parse_args()

    today = date.today()
    errors: list[str] = []
    warnings: list[str] = []

    with zipfile.ZipFile(args.gtfs_zip) as z:
        names = set(z.namelist())
        for required in ("agency.txt", "routes.txt", "stops.txt", "trips.txt", "stop_times.txt"):
            if required not in names:
                errors.append(f"missing required file: {required}")
        if errors:
            print("\n".join(f"ERROR: {e}" for e in errors))
            return 1

        agencies = [r.get("agency_name", "?") for r in read_rows(z, "agency.txt")]

        routes = {}
        for r in read_rows(z, "routes.txt"):
            try:
                rtype = int(r.get("route_type") or 3)
            except ValueError:
                rtype = 3
            routes[r["route_id"]] = {
                "id": r["route_id"],
                "short": r.get("route_short_name", ""),
                "long": r.get("route_long_name", ""),
                "type": rtype,
                "color": (r.get("route_color") or "").strip() or None,
                "textColor": (r.get("route_text_color") or "").strip() or None,
            }

        stops = {}
        bad_coords = 0
        for r in read_rows(z, "stops.txt"):
            if (r.get("location_type") or "0") not in ("", "0"):
                continue  # skip stations/entrances; keep boardable stops
            try:
                lat, lon = float(r["stop_lat"]), float(r["stop_lon"])
            except (KeyError, ValueError):
                bad_coords += 1
                continue
            stops[r["stop_id"]] = {
                "id": r["stop_id"],
                "code": r.get("stop_code", ""),
                "name": r.get("stop_name", ""),
                "lat": round(lat, 5),
                "lon": round(lon, 5),
                "routes": set(),
            }

        trip_route: dict[str, str] = {}
        route_shape_counts: dict[str, Counter] = defaultdict(Counter)
        for r in read_rows(z, "trips.txt"):
            trip_route[r["trip_id"]] = r["route_id"]
            if r.get("shape_id"):
                route_shape_counts[r["route_id"]][r["shape_id"]] += 1

        # stop -> routes (streams the biggest file in the feed)
        for r in read_rows(z, "stop_times.txt"):
            rid = trip_route.get(r["trip_id"])
            sid = r["stop_id"]
            if rid and sid in stops:
                stops[sid]["routes"].add(rid)

        # --- validation report ------------------------------------------------
        feed_info = next(iter(read_rows(z, "feed_info.txt")), None)
        feed_start = parse_gtfs_date(feed_info.get("feed_start_date")) if feed_info else None
        feed_end = parse_gtfs_date(feed_info.get("feed_end_date")) if feed_info else None
        if feed_info is None:
            warnings.append("no feed_info.txt; cannot confirm service dates that way")

        cal_starts, cal_ends = [], []
        for r in read_rows(z, "calendar.txt"):
            s, e = parse_gtfs_date(r.get("start_date")), parse_gtfs_date(r.get("end_date"))
            if s:
                cal_starts.append(s)
            if e:
                cal_ends.append(e)
        cal_start = min(cal_starts) if cal_starts else None
        cal_end = max(cal_ends) if cal_ends else None

        latest_end = max([d for d in (feed_end, cal_end) if d], default=None)
        if latest_end and latest_end < today:
            errors.append(f"feed appears EXPIRED: latest end date {latest_end} < today {today}")
        elif latest_end and (latest_end - today).days < 30:
            warnings.append(f"feed expires soon: {latest_end} ({(latest_end - today).days} days)")

        type_counts = Counter(route_type_name(r["type"]) for r in routes.values())
        ferry_routes = [r["short"] or r["long"] for r in routes.values() if is_ferry(r["type"])]
        if bad_coords:
            warnings.append(f"{bad_coords} stops skipped for missing/invalid coordinates")
        unused_stops = sum(1 for s in stops.values() if not s["routes"])
        if unused_stops:
            warnings.append(f"{unused_stops} stops are not served by any trip")

        lats = [s["lat"] for s in stops.values()]
        lons = [s["lon"] for s in stops.values()]
        bbox = [min(lats), min(lons), max(lats), max(lons)] if stops else None

        report = {
            "generatedOn": today.isoformat(),
            "source": args.gtfs_zip.name,
            "agencies": agencies,
            "counts": {"routes": len(routes), "stops": len(stops), "trips": len(trip_route)},
            "routeTypes": dict(type_counts),
            "ferryRoutesInFeed": ferry_routes,
            "feedInfo": {
                "publisher": (feed_info or {}).get("feed_publisher_name"),
                "version": (feed_info or {}).get("feed_version"),
                "start": feed_start.isoformat() if feed_start else None,
                "end": feed_end.isoformat() if feed_end else None,
            },
            "calendarRange": {
                "start": cal_start.isoformat() if cal_start else None,
                "end": cal_end.isoformat() if cal_end else None,
            },
            "stopsBoundingBox_minLat_minLon_maxLat_maxLon": bbox,
            "errors": errors,
            "warnings": warnings,
        }

        print(json.dumps(report, indent=2))

        if args.validate_only:
            return 1 if (errors and args.strict) else 0

        # --- convert ----------------------------------------------------------
        args.out.mkdir(parents=True, exist_ok=True)

        best_shape = {rid: c.most_common(1)[0][0] for rid, c in route_shape_counts.items()}
        wanted = set(best_shape.values())
        raw_shapes: dict[str, list[tuple[int, float, float]]] = defaultdict(list)
        for r in read_rows(z, "shapes.txt"):
            sid = r["shape_id"]
            if sid in wanted:
                raw_shapes[sid].append(
                    (int(float(r["shape_pt_sequence"])), float(r["shape_pt_lat"]), float(r["shape_pt_lon"]))
                )

        shapes = {}
        for rid, sid in best_shape.items():
            pts = [(lat, lon) for _, lat, lon in sorted(raw_shapes.get(sid, []))]
            if pts:
                slim = simplify(pts, args.tolerance)
                shapes[rid] = [[round(a, 5), round(b, 5)] for a, b in slim]

    def dump(name: str, payload) -> None:
        path = args.out / name
        path.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
        print(f"wrote {path} ({path.stat().st_size / 1024:.1f} KiB)")

    dump("routes.json", {"version": 1, "routes": sorted(routes.values(), key=lambda r: r["short"])})
    dump("stops.json", {"version": 1, "stops": [
        {**s, "routes": sorted(s["routes"])} for s in stops.values()
    ]})
    dump("shapes.json", {"version": 1, "shapes": shapes})
    (args.out / "gtfs_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    if errors and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
