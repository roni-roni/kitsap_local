# Primer: VS Code for Flutter

Read this before Class 1. Goal: be productive in the editor in 30 minutes.

## Setup

1. Install Flutter (which includes Dart) from the official docs for your OS, then
   the Android SDK (easiest via Android Studio, even if you never open it again).
2. In VS Code install two extensions: **Flutter** (pulls in **Dart**). Optional:
   **GitLens**, **Error Lens**, **YAML**.
3. Run `flutter doctor` in a terminal. Fix every red item that matters to you
   (Android toolchain, VS Code). Chrome and Linux desktop entries are optional but
   handy for quick iteration.
4. Accept licenses: `flutter doctor --android-licenses`.
5. Phone: turn on Developer options and USB debugging, plug in, and check
   `flutter devices` lists it.

## The ten things you will actually use

| Action | How |
| --- | --- |
| Command Palette | `Ctrl/Cmd+Shift+P`. Type "Flutter:" to see every command |
| Pick a device | Status bar (bottom right), or "Flutter: Select Device" |
| Run / debug | `F5` (with breakpoints), or `Ctrl+F5` (run without debugging) |
| Hot reload | Save the file (or `Ctrl/Cmd+S`); UI updates in under a second, state kept |
| Hot restart | `Ctrl/Cmd+Shift+F5`; resets app state |
| Quick fix / refactor | `Ctrl/Cmd+.` on a widget: wrap with Padding, extract widget, add const |
| Go to definition | `F12`; `Ctrl/Cmd+Click` on any symbol; `Alt+Left` to go back |
| Find file / symbol | `Ctrl/Cmd+P` (file), `Ctrl/Cmd+Shift+O` (symbol in file) |
| Format | `Shift+Alt+F`. Team rule: format on save (see below) |
| Problems panel | `Ctrl/Cmd+Shift+M`. The analyzer's list of everything wrong |

## Settings worth turning on

Workspace settings (`.vscode/settings.json`, which you may commit):

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": { "source.fixAll": "explicit" },
  "dart.previewFlutterUiGuides": true,
  "dart.closingLabels": true
}
```

## Flutter DevTools

Open with "Flutter: Open DevTools" while the app runs. Three tabs matter early:

- **Widget Inspector**: click a thing on the phone, see its widget and layout box.
  Your first stop for "why is this in the wrong place?"
- **Performance**: catches jank (dropped frames) once the map arrives in Class 6.
- **Network**: see every API call your app makes (Class 6).

## Reading errors

- **Red screen of death**: read the *first* line of the message, then the
  `relevant error-causing widget` line. `RenderFlex overflowed` means a Row or
  Column ran out of room; wrap a child in `Expanded` or make the content scroll.
- **Analyzer squiggles** are cheaper than runtime errors. Keep the Problems
  panel at zero.
- **`flutter clean && flutter pub get`** fixes surprising numbers of odd problems.

## Terminal commands you will use every week

```
flutter pub get          # fetch dependencies
flutter pub add <pkg>    # add a dependency at a current version
flutter run              # run on the selected device
flutter test             # run unit and widget tests
flutter analyze          # static analysis
dart format .            # format everything
flutter build appbundle  # release bundle for the Play Store
```

## Habits

- Save often; hot reload rewards small changes.
- Commit at every green state (see the [GitHub primer](02-primer-github.md)).
- Never hard-code a key in a file you might commit. See [`../.gitignore`](../.gitignore).
