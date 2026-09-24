# Architecture (target by Class 6)

The boilerplate starts flat on purpose. Each class adds one layer, so students
feel why the layer exists.

```
lib/
  main.dart                 entry point (ProviderScope from Class 5)
  app.dart                  MaterialApp / router
  core/                     theme, config, shared constants, error types
  shared/                   widgets used by several features
  shell/                    the six-tab scaffold
  models/                   plain Dart data classes (Class 2)
  data/                     repositories + data sources (Class 5)
    sources/                bundled JSON, WSDOT client, proxy client
  features/
    bus/                    screens, widgets, providers for one tab
    ferry/
    government/
    parks/
    events/
    help/
data/                       bundled JSON (curated + generated)
tools/                      Python data scripts, backlog seeder
functions/                  Cloud Functions proxy (keys live here)
docs/                       this course
test/                       unit + widget tests; integration_test/ from Class 9
```

## Layers and the rule between them

```
Screen (widget)  ->  Provider (state)  ->  Repository (interface)  ->  Data source
   what the user sees    loading/data/error      "give me ferry terminals"     JSON, HTTP, cache
```

**Rule:** a layer only knows about the layer directly below it. Screens never
call `http` directly. That is what makes it cheap in Class 6 to swap the mock
ferry repository for the WSDOT one, and in Class 9 to swap bundled bus data for
live data, without touching screens.

## Principles we practice

- **Immutable models** with `fromJson` / `toJson`, tested (Class 2).
- **Small widgets** (extract early), `const` constructors where possible.
- **Model states explicitly**: loading, data, error, empty. No blank screens.
- **One source of truth** for each piece of state; derive the rest.
- **Repository interfaces** so tests can use fakes.
- **Secrets stay out of the client** (`functions/`), configs via `--dart-define`.
- **Versioned local data.** Every JSON file has a `version`; Class 9 adds
  migration for on-device favorites/settings.
- **Attribute your sources** in the UI and record their licenses.
- **Feature folders, not type folders.** Everything for Parks lives together.

## Decisions to record as you make them

Keep a short `docs/decisions.md` (one paragraph per decision): why Riverpod,
why `flutter_map`, why a proxy for live buses, which tile provider, how alerts
will be moderated. Future you, and your testers' questions, will thank you.
