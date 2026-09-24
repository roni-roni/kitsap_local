# data/

Curated and generated JSON that ships inside the app as bundled assets.

| File | Written by | Used in |
| --- | --- | --- |
| `help.json` | hand (Class 4) | Help tab |
| `events.json` | hand (Class 5) | Events tab |
| `generated/routes.json` | `tools/gtfs_to_json.py` | Bus tab |
| `generated/stops.json` | `tools/gtfs_to_json.py` | Bus tab |
| `generated/shapes.json` | `tools/gtfs_to_json.py` | Bus tab |
| `generated/gtfs_report.json` | `tools/gtfs_to_json.py` | Instructors (validation) |
| `generated/officials.json` | `tools/county_officials.py` | Government tab |

Every file has a top-level `"version"` integer. Bump it when you change the
*shape*; your Dart parser can then refuse or migrate old data.

## help.json

```
opportunities[]:
  id           string, unique, kebab-case
  name         string
  category     one of: food, housing, animals, environment, seniors, youth,
               veterans, arts, health, education, other
  city         string
  description  string, 1-2 sentences, plain language
  commitment   string, what the time ask really looks like
  url          string, the page where someone STARTS volunteering
  tags         string[]
  lastVerified string, ISO date (YYYY-MM-DD) you last checked the link works
```

## events.json

```
events[]:
  id           string, unique
  title        string
  start        ISO 8601 WITH offset, e.g. 2026-10-03T09:00:00-07:00
  end          ISO 8601 with offset, optional
  location     string
  city         string
  source       string, who hosts/sponsors it (county, a city, ...)
  url          string, optional
  description  string, optional
  recommended  bool, true if the county/city recommends rather than hosts
```

Always store times WITH an offset. "9:00" means nothing across a daylight
saving change, and Class 9's add-to-calendar feature depends on it.

## Editing rules

- Keep it valid JSON (VS Code will underline mistakes; CI checks it too).
- Do not copy logos or seals. Link to the source instead.
- Re-verify links before each release and update `lastVerified`.
