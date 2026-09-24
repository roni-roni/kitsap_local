# Class 9 - Building v1.1

**New this week (bold):** live bus positions through a proxy, favorites, Maps hand-off, add-to-calendar, report hand-offs, data migration, integration tests, and CI.

Split across two sittings if needed: (A) proxy + live buses, (B) features + quality.

## Learning goals

- Put secrets behind a server-side proxy.
- Integrate with the phone: maps, calendar, external sites.
- Migrate stored data safely between app versions.
- Automate quality checks.

## Part A: Live buses through a proxy

1. **Why a proxy:** a key inside the APK is public; a proxy also caches, slims payloads, and lets you change providers without shipping a new app.
2. Firebase CLI: `firebase login`, `firebase functions:secrets:set OBA_API_KEY`, then deploy `functions/`. Read `functions/index.js`; resolve its `TODO(Class 9)` items (confirm base URL, endpoint, and Kitsap agency id against current docs, using the key you have).
3. If Kitsap Transit approved BusTime, implement that as the upstream instead (or in addition); the app-facing shape `{vehicles:[...]}` stays the same.
4. Add `PROXY_BASE_URL` to `env/dev.json`; write `VehiclesRepository`, poll every ~15 s **only while the Bus tab is visible**, mark stale positions.
5. Draw vehicles on the map, tapped for route and "updated N s ago".

## Part B: Features

- **Favorites** for parks, bus routes/stops, and ferry terminals. Store locally first (`shared_preferences`), sync via Firestore when signed in. Same UI either way.
- **Maps hand-off.** `url_launcher` with a `geo:` URI (Android) to open the default Maps app at a location.
- **Add to calendar.** Prefer an intent-based approach (no calendar permission) via a maintained package; pass start/end from the ISO 8601 offset data.
- **Reports.** Government tab: buttons that open SeeClickFix or the specific county form. The app does not store reports; it hands off.
- **Data migration.** Add a `schemaVersion` to on-device data; write a migration step from v1 (no favorites) to v2; test it with an old-format fixture.
- **Tests.** Add `integration_test` for: launch, switch tabs, open a ferry terminal, favorite a park.
- **CI.** Move `docs/templates/ci.yml` to `.github/workflows/ci.yml`; require the check on `main`.

## Discussion prompts

- What does "add to calendar" put in the Data safety form, and how do we reduce it?
- How do we avoid hammering the upstream when 1,000 phones poll?
- Why is a migration test more valuable than a migration?

## Homework

- Update the privacy policy and Data safety draft for sign-in, favorites sync, and calendar.
- Design (on paper only) the moderation flow the future Alerts feature will need.

## Definition of done

- [ ] Proxy deployed; **no key in the repo or the APK** (search for it to prove it)
- [ ] Live bus markers with stale indicator
- [ ] Favorites, Maps hand-off, add-to-calendar, report hand-off work
- [ ] Migration test passes from a v1 fixture
- [ ] Integration tests run; CI green on `main`

## Best-practice notes

- Poll only while visible; stop when backgrounded.
- Hand off to specialized apps (Maps, Calendar, SeeClickFix) rather than rebuilding them.
