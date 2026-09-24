# Kitsap Local

A mobile-first community app for Kitsap County, Washington, built as the
running project for a ten-week Flutter and Dart course.

Six tabs: **Bus**, **Ferry**, **Government**, **Parks**, **Events**, **Help**
(volunteering). Later: favorites, sign-in, alerts, and a Jobs board.

> This is an **unofficial** community project. It is not affiliated with Kitsap
> County, any city, Kitsap Transit, or Washington State Ferries.

**Start here:** [`docs/00-course-map.md`](docs/00-course-map.md)

## What is in this repo

```
lib/         Flutter app: six-tab shell, theme, config, placeholder screens
test/        Widget test for the shell
data/        Curated JSON (help, events) + generated/ output of tools/
tools/       Python data scripts and the GitHub backlog seeder
functions/   Cloud Functions proxy stub (API keys live server-side)
env/         dev.example.json for --dart-define-from-file (real files ignored)
docs/        The course: map, primers, per-class pages, data sources
             (docs/templates/ has issue/PR templates, VS Code settings, CI)
```

The `android/` folder is not included; you generate it in step 2 below so it
matches *your* Flutter version and application ID.

## Quick start (Class 1)

Prerequisites: Flutter (stable), Android SDK, VS Code with the Flutter
extension. See [`docs/01-primer-vscode.md`](docs/01-primer-vscode.md).

```bash
# 0. Install the GitHub and VS Code config files (kept in docs/templates/
#    because hidden folders could not be delivered with the rest of the repo)
mkdir -p .github .vscode
cp -r docs/templates/github/. .github/
cp docs/templates/vscode-settings.json .vscode/settings.json

# 1. Commit the boilerplate first so the next step's changes are reviewable
git init
git add .
git commit -m "Boilerplate: six-tab shell"

# 2. Generate platform folders. CHOOSE THE ORG CAREFULLY: the resulting
#    application ID is permanent once uploaded to the Play Store.
flutter create --platforms=android --org io.github.YOURNAME --project-name kitsap_local .
git status        # review what flutter create added or changed

# 3. Run
flutter pub get
flutter run       # or press F5 in VS Code
flutter test
```

If `flutter create` touched `lib/main.dart`, `pubspec.yaml`, or
`test/widget_test.dart`, restore them: `git restore lib/main.dart pubspec.yaml test/widget_test.dart`.

The boilerplate has been written by hand and reviewed, but it was **not compiled
in the authoring environment**. If `flutter analyze` or `flutter test` reports
anything on first run, treat it as your first bug report (and a fine Class 1
exercise).

Seed the backlog:

```bash
DRY_RUN=1 tools/backlog/seed_issues.sh   # preview
tools/backlog/seed_issues.sh             # create milestones, labels, issues
```

## Keys and secrets

Nothing secret is committed. See `.gitignore` for the full list.

- App config: copy `env/dev.example.json` to `env/dev.json`, fill it in, run
  `flutter run --dart-define-from-file=env/dev.json`.
- Server-side keys (OneBusAway): Firebase Secret Manager via `functions/`.
- Release signing: `android/key.properties` and your keystore stay off GitHub.

## Data scripts

```bash
python3 tools/gtfs_to_json.py path/to/gtfs.zip --validate-only   # Class 6
python3 tools/gtfs_to_json.py path/to/gtfs.zip                   # writes data/generated/
python3 tools/county_officials.py --url <page> --list-tables     # Class 5
```

Python 3.9+ and the standard library only.

## Commands

```bash
flutter pub get
flutter analyze
dart format .
flutter test
flutter build appbundle    # Play Store release bundle
```
