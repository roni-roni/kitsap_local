# Class 6 - Data, APIs, and maps

**New this week (bold):** WSDOT API for ferries, validated GTFS to slim JSON, routes and stops on `flutter_map`, park boundaries, caching, error states. **Closed-test Day 14 lands here.**

This is the biggest class. Split it across two sittings if needed: (A) ferries + caching, (B) GTFS + maps + park boundaries.

## Learning goals

- Call a REST API, parse the response, and handle failure.
- Validate a dataset *before* building UI on top of it.
- Render geographic data on a map, keeping it fast.
- Cache data and degrade gracefully offline.

## Concepts

- HTTP: GET, status codes, headers, timeouts, JSON. `package:http`.
- Keys and `--dart-define-from-file=env/dev.json`; why client-side keys are extractable.
- Caching: memory vs disk; `shared_preferences` or a file in `path_provider`; "stale-while-revalidate"; the WSDOT `/cacheflushdate` polling trick.
- Geo basics: latitude/longitude, polylines, polygons, bounds, zoom, tiles.
- `flutter_map` and `latlong2`: `TileLayer`, `PolylineLayer`, `MarkerLayer`, `PolygonLayer`; marker clustering for many stops.
- Performance: simplify shapes; do not put 1,500 widgets on a map.
- Error taxonomy: no network, timeout, bad status, bad data, empty data.

## Part A: Ferries

1. `flutter pub add http shared_preferences`.
2. Write a `WsdotFerryClient` (`/terminals`, `/routes`, `/scheduletoday`, `/alerts`, `/cacheflushdate`) behind the same `FerryRepository` interface used by the mock.
3. Swap the mock; the screens should not change.
4. Alerts banner and outage state on terminals and routes.
5. Cache the last good response; show "Updated 3:42 PM" and a clear offline banner.

## Part B: Bus, maps, parks

1. **Validate the GTFS zip before writing UI.**
   `python3 tools/gtfs_to_json.py path/to/gtfs.zip --validate-only`
   Read the report as a class: route and stop counts, `feed_info.txt` and calendar service dates (expired?), bounding box (does it cover Bremerton, Poulsbo, Port Orchard, Bainbridge?), and **whether ferry routes appear in the feed**. Record the answers in an issue. Then run without `--validate-only` to write slim JSON into `data/generated/`.
2. Add `flutter_map` and `latlong2`. Show routes (polylines, color from GTFS) and stops (markers, clustered), with a route filter.
3. Tile source: OpenStreetMap public tiles are fine for class demos; **show attribution** and read the usage policy; plan a production tile provider.
4. **Parks.** Bring in location and boundary data from the county and state datasets: convert to slim GeoJSON/JSON (simplify polygons), record the license, draw on the map, and link the list and map views.
5. Error and empty states everywhere; tap a stop to see its routes.

## Discussion prompts

- If the GTFS validation reports the feed expired next month, what do we do?
- Why simplify shapes? What is the cost if we do not?
- What should the app do when the WSDOT API is down at 5:15 pm on a Friday?

## Homework

- Run the closed-test count check: **Day 14, 12+ testers still opted in?** Screenshot the Play Console testers page for your records.
- Write the first draft of the production-access application answers.
- File issues for anything that testers reported.

## Definition of done

- [ ] Ferry tab runs on live WSDOT data with alerts, caching, offline state
- [ ] `gtfs_report.json` reviewed and decisions recorded
- [ ] Bus map with routes and stops, smooth pan/zoom on a mid-range phone
- [ ] Parks locations + boundaries on a map, licenses recorded
- [ ] No unhandled exceptions in airplane-mode test
- [ ] Day 14 reached with 12+ testers; **production-access application filed** (or ready to file)

## Best-practice notes

- Validate data first, build UI second.
- Never show stale data as if it were live.
- Record every source's license and attribution requirements.
