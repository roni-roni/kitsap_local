# Class 3 - Widgets and layout

**New this week (bold):** Ferry and Parks screens on mock data, and the first installable build.

## Learning goals

- Compose UI from widgets; read and fix layout problems.
- Build list screens from model data.
- Produce a signed release build that installs on a phone.

## Concepts

- Layout: `Row`, `Column`, `Stack`, `Expanded`, `Flexible`, `Padding`, `SizedBox`, `Wrap`.
- Constraints: "constraints go down, sizes go up, parent sets position." The source of nearly every overflow error.
- Lists: `ListView.builder`, `Card`, `ListTile`, `Divider`, `RefreshIndicator`.
- Reusable widgets and `const` constructors; extract widget vs helper method.
- Responsive basics: `MediaQuery`, `LayoutBuilder`, text scaling.
- Images and icons; accessible labels (`Semantics`, `tooltip`).
- Stateful vs stateless: `setState` in a small scope.
- **Trade-off to discuss:** `IndexedStack` in the shell keeps all tabs alive (state preserved, memory cost).

## In class

1. **Mock data.** Create `lib/data/mock/` (or `test/fixtures/`) with a handful of ferry terminals, departure times, and parks. Use the Class 2 models.
2. **Ferry screen.** List of terminals; each tile shows the terminal name and the **next departure** (a computed value from a sorted list of times), with a status chip.
3. **Ferry detail.** Tap a terminal: route schedule as a scrollable list, grouped by direction.
4. **Parks screen.** Card list showing name, owner (city/county/state/DNR/federal), and an "entry" badge (free, Discover Pass).
5. **Stress-test the UI.** Small phone, big font (Settings > Display), dark mode, landscape. Fix every overflow.
6. **First installable build.** Set up release signing (upload keystore, `android/key.properties`, both **gitignored**), run `flutter build appbundle`, and also `flutter build apk --release` to sideload and confirm it installs and launches.

## Why the build matters this early

The closed-test clock in Play Console cannot start without an uploaded build (see the [Play Store primer](../03-primer-play-store.md)). A rough app in test now is worth more than a polished app in test three weeks from now.

## Discussion prompts

- "Next departure" needs the current time. Where should "now" come from so it is testable?
- What should the terminal tile show if there are no more departures today?
- A `Column` inside a `ListView` overflows. Why? What are three fixes?

## Homework

- Add "last updated" text to each screen (fake it for now).
- Back up the upload keystore and password (not in git).
- Install the release APK on a second phone if you can.

## Definition of done

- [ ] Ferry list + detail and Parks list work on mock data
- [ ] No overflows at 2x text scale on a small screen
- [ ] Widget tests: one per screen (renders, shows expected text)
- [ ] Signed `.aab` produced; release build tested on a real device
- [ ] Keystore backed up outside the repo; `.gitignore` verified

## Best-practice notes

- Extract widgets once they have a name in your head ("TerminalTile").
- Use `const` wherever the analyzer suggests it.
- Touch targets at least 48x48 dp; contrast that survives sunlight.
