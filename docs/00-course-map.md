# Course map

A ten-class, weekly course. Students learn Flutter and Dart by building one real
app for Kitsap County, and the app ships to the Play Store around Class 7.

**How to read this map.** Each class lists what is **new this week in bold**;
plain text is carried forward from earlier classes. Each class has its own page
in [`classes/`](classes/) with concepts, the in-class build, homework, and a
definition of done.

Companion pages: [VS Code primer](01-primer-vscode.md) ·
[GitHub primer](02-primer-github.md) · [Play Store primer](03-primer-play-store.md) ·
[So what? Who cares?](04-so-what-who-cares.md) ·
[Instructor setup](05-instructor-setup.md) · [Data sources](06-data-sources.md) ·
[Architecture](07-architecture.md)

---

## Before Class 1 (instructor setup)

Details, email drafts, and lead times in [05-instructor-setup.md](05-instructor-setup.md).

- **Email Sound Transit for the OneBusAway real-time key** (about two business days).
- **Email Kitsap Transit about BusTime API access and documentation.**
- **Register for the WSDOT ferry access code.**
- **Create the Play Console account, and start recruiting testers**, since the app will need 12 of them opted in for 14 continuous days.

---

## The classes

### Class 1 - Orientation and toolchain
[Class page](classes/class-01.md)

- **Boilerplate repo with the six-tab shell** (Bus, Ferry, Government, Parks, Events, Help)
- **GitHub Issues backlog** (seeded from `tools/backlog/backlog.json`)
- **Toolchain: Flutter, Android SDK, VS Code, `flutter doctor`**
- **Permanent Android application ID chosen**

### Class 2 - Dart fundamentals
[Class page](classes/class-02.md)

- Six-tab shell, backlog, toolchain
- **Models for Route, Stop, Vehicle, FerryTerminal, Park, Event, Official, and Meeting**
- **Parsed from bundled JSON** (`data/`)
- **Unit tests for every parser**

### Class 3 - Widgets and layout
[Class page](classes/class-03.md)

- Models, bundled JSON
- **Ferry screen on mock data**
- **Parks screen on mock data**
- **First installable test version** (signed AAB). The closed-test clock cannot start without one.

### Class 4 - Navigation, forms, theming
[Class page](classes/class-04.md)

- Ferry and Parks screens
- **Help tab from hand-curated JSON**
- **Park filters** (form controls)
- **go_router navigation and theme pass**
- **First closed-test build uploaded; testers opt in. The 14-day count starts here.**

### Class 5 - State management and architecture
[Class page](classes/class-05.md)

- Navigation, theme, Help, filters
- **Riverpod and repositories**
- **Government tab**: county officials pulled from the county HTML table by a small data script
- **Curated Events tab**

### Class 6 - Data, APIs, and maps
[Class page](classes/class-06.md)

- Riverpod, repositories, Government, Events
- **Ferry schedules and alerts from the WSDOT API**
- **Static bus data from the GTFS zip**: this is where the class validates it (route and stop counts, service dates in `feed_info.txt`, whether ferry routes are included) and converts it to slim JSON
- **Routes and stops on `flutter_map`**
- **Park boundaries and locations from the county and state datasets**
- **Caching and error states**

### Class 7 - Release and first submission
[Class page](classes/class-07.md)

- Everything above
- **Submit v1**
- **Apply for production access** (the form asks about tester feedback)
- **Store listing, privacy policy, Data safety form**

### Class 8 - Post-launch and update planning
[Class page](classes/class-08.md)

- v1 in review or live
- **Analytics and Play vitals**
- **Triage of the backlog**
- **Firebase and Google Sign-In**
- **Review the outcome of the Kitsap Transit outreach**

### Class 9 - Building v1.1
[Class page](classes/class-09.md)

- Sign-in, analytics
- **Live bus positions through a small proxy (Cloud Function)**, using the OneBusAway feed, or BusTime if Kitsap Transit approves it
- **Favorites**
- **Maps hand-off**
- **Add-to-calendar**
- **Reports handed off to SeeClickFix and the county forms**
- **Data migration, integration tests, and CI**

### Class 10 - Ship the update
[Class page](classes/class-10.md)

- v1.1 feature-complete
- **Same release process as Class 7, run faster and with less help**: bump the version, update the Data safety form, staged rollout, monitor vitals

### After Class 10 (backlog, not scheduled)

- User-submitted alerts (Parks, Bus, Ferry) shown as banners in other users' apps. Needs moderation and report/block tools first; see the UGC section of the [Play Store primer](03-primer-play-store.md).
- Jobs tab: hiring board for local businesses.
- iOS (needs a Mac and an Apple Developer account).

---

## Timeline check

The closed test needs **14 days** of continuous opt-in from **12 testers**, and then Google's production-access review (usually up to about a week, sometimes longer), and then the app's own review after the first production submission.

| Week | Class | Release milestone |
| --- | --- | --- |
| 3 | Class 3 | First installable build exists (signed AAB) |
| 4 | Class 4 | **Day 0:** build in closed test; testers opt in |
| 5 | Class 5 | Day 7: check testers are still opted in |
| 6 | Class 6 | **Day 14:** count reaches 14 days; apply for production access as soon as the console allows it |
| 6-7 | between classes | Production-access review (up to about a week) |
| 7 | Class 7 | Approved: submit v1 to production. If not yet approved, finish store listing and privacy policy |
| 8 | Class 8 | App review outcome; v1 live or in fix-up |
| 9-10 | Classes 9-10 | v1.1 built and shipped |

It is tight but workable. Two things will break it:

1. **Testers who drop out.** Testers who opt out lose their days. Recruit 15-20 to
   land at 12 or more still opted in on day 14.
2. **A rejected or slow review.** Keep a spare week in your head; nothing in
   Classes 8-10 depends on v1 being live on a specific day, except the
   Data safety form updates.

> Note on the schedule: the application for production access can be filed the
> day the 14-day count is met (the end of Class 6 week). Class 7 is where the
> class fills in and refines that application and submits v1. If the
> application is filed earlier, the review can land before Class 7.

## Boilerplate that supports the plan

| Path | Purpose | First used |
| --- | --- | --- |
| `lib/` | Six-tab shell, theme, config, placeholder screens | Class 1 |
| `data/` | Curated JSON (Help, Events) and `generated/` output | Class 2 |
| `tools/` | Data scripts (GTFS to JSON, county officials) and backlog seeder | Class 1 / 5 / 6 |
| `functions/` | Cloud Functions proxy stub; holds keys server-side | Class 9 |
| `env/` | `dev.example.json` for `--dart-define-from-file` (real files ignored) | Class 6 |
| `.gitignore` | Keeps keys, keystores, and service files out of GitHub | Class 1 |
| `docs/templates/` | Issue/PR templates and VS Code settings (copied into `.github/`, `.vscode/` in Class 1); `ci.yml` turns on CI | Class 1 / 9 |
