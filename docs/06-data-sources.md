# Data sources

**Status legend:** `?` not yet checked · `docs` seen in documentation · `verified`
you have fetched real data and looked at it. Nothing below is `verified` until a
student or instructor does it; use the "Data source check" issue template.

| Tab | Data | Likely source | Access | Status | Used in |
| --- | --- | --- | --- | --- | --- |
| Bus | Routes, stops, shapes | Kitsap Transit GTFS zip | Public download (find current URL; listed on Transitland) | ? | Class 6 |
| Bus | Live positions | OneBusAway Puget Sound API | Key from Sound Transit OTD | docs | Class 9 |
| Bus | Live positions (alt) | Kitsap Transit BusTime | Needs agency approval | ? | Class 9 |
| Ferry | Routes, terminals, schedule, alerts | WSDOT Ferries Schedule / Terminals APIs | Access code | docs | Class 3 (mock), Class 6 |
| Ferry | Vessel positions (optional) | WSDOT Vessels API | Same access code | ? | Later |
| Government | County officials | County website HTML table | Public page, scrape politely | ? | Class 5 |
| Government | Meetings (county, cities) | Each government's calendar/agenda pages | Public pages; curate links | ? | Class 5 |
| Government | Report an issue | SeeClickFix + county web forms | Link out / deep link | ? | Class 9 |
| Parks | Locations, boundaries | County GIS open data; WA State Parks; WA DNR; federal layers | Public datasets, check licenses | ? | Class 6 |
| Parks | Entry requirements | Discover Pass rules (State Parks, DNR) | Curate by hand | ? | Class 3-4 |
| Events | Events | County and city calendars | Curate by hand for v1 | ? | Class 5 |
| Help | Volunteer organizations | You build the list | Hand-curated | n/a | Class 4 |

## Questions each source must answer

1. **Coverage:** does it include Bremerton, Bainbridge Island, Port Orchard, Poulsbo, and unincorporated areas, or only some?
2. **Freshness:** how often does it change, and how do we know it is stale?
3. **License/terms:** may we redistribute it in an app? What attribution is required?
4. **Access:** open, key, or approval? What are the rate limits?
5. **Shape:** what does a sample look like? Save one (with keys removed) in `tools/raw/` (gitignored) and note its shape in an issue.
6. **Failure plan:** what should the app show if it is down or empty?

## Known facts worth writing down

- The WSDOT ferry API supports JSON via `Accept: application/json`, takes
  `apiaccesscode` as a query parameter, and exposes `/cacheflushdate`, which
  you poll to decide when to drop cached data.
- Ferries in Kitsap include both WSDOT Washington State Ferries routes
  (e.g., Bainbridge, Bremerton, Kingston, Southworth) and Kitsap Transit passenger-only
  ferries. Only the first group comes from WSDOT. Check whether the Kitsap
  Transit GTFS contains the passenger-only ferry routes (Class 6 does this check).
- OpenStreetMap public tile servers have a usage policy; heavy or commercial
  use needs a proper tile provider. Always show attribution.
