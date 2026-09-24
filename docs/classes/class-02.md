# Class 2 - Dart fundamentals

**New this week (bold):** data models and JSON parsing.

## Learning goals

- Write Dart comfortably: types, null safety, collections, functions, classes.
- Model real-world data as immutable classes.
- Parse JSON safely, and test the parsing.

## Concepts

- Variables: `final`, `const`, `var`; type inference.
- **Null safety:** `String?`, `??`, `?.`, `!` (and why to avoid `!`).
- Collections: `List`, `Map`, `Set`; `map`, `where`, `toList`; collection `for`/`if`.
- Classes, constructors (named, `const`, `factory`), `final` fields, `copyWith`.
- Enums, including enhanced enums (with fields), for `ParkOwner`, `EntryRequirement`, `RouteType`.
- `dart:convert` (`jsonDecode`) and `rootBundle.loadString`.
- `Future` / `async` / `await` (introduced lightly; used heavily from Class 6).
- Records and pattern matching (short tour).

## In class: the models

Build these in `lib/models/`. Each has `fromJson`, `toJson` (where useful), `==`/`hashCode` or a simple value-equality approach, and a test.

| Model | Key fields | Source |
| --- | --- | --- |
| `Route` | id, short, long, type, color | `data/generated/routes.json` shape |
| `Stop` | id, code, name, lat, lon, routeIds | `stops.json` shape |
| `Vehicle` | id, lat, lon, routeId, heading, updated | shape only for now |
| `FerryTerminal` | id, name, lat, lon, routeIds | WSDOT terminals shape |
| `Park` | id, name, owner, entry, lat, lon, description | mock JSON |
| `Event` | id, title, start, end, location, city, source, url | `data/events.json` |
| `Official` | name, office, phone, email | `officials.json` shape |
| `Meeting` | body, city, start, agendaUrl | mock JSON |

Use the synthetic GTFS zip pattern from `tools/gtfs_to_json.py` (or hand-write small JSON fixtures) to get sample data before Class 6.

## Testing pattern

```dart
test('Event parses ISO 8601 with offset', () {
  final e = Event.fromJson({'id': 'x', 'title': 'T',
    'start': '2026-10-03T09:00:00-07:00', /* ... */});
  expect(e.start.toUtc().hour, 16);
});
test('Event throws FormatException on missing title', () { /* ... */ });
```

## Discussion prompts

- Which fields can really be missing in the wild? (Route color, stop code, event end.) How do we model "missing"?
- Why enums instead of strings for `ParkOwner`?
- What should the parser do on bad data: crash, skip the record, or default?

## Homework

- Finish all eight models with tests. Aim for parse-success and parse-failure tests for each.
- Load `data/help.json` into a list of a `VolunteerOpportunity` model (your choice of fields, following `data/README.md`).
- Print a summary from a small Dart script or test: "N events, next one is ...".

## Definition of done

- [ ] Eight models + `VolunteerOpportunity`, all with tests
- [ ] `flutter test` and `flutter analyze` clean
- [ ] No use of `!` without a comment explaining why it is safe
- [ ] PR merged with issue links

## Best-practice notes

- Keep models plain Dart (no Flutter imports). They are the most reusable, testable part of the app.
- Prefer explicit parse errors over silent defaults for required fields.
