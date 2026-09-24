# Class 1 - Orientation and toolchain

**New this week (bold):** the boilerplate repo, the backlog, the toolchain.
**Before class:** read the [VS Code](../01-primer-vscode.md) and [GitHub](../02-primer-github.md) primers and the [So what? Who cares?](../04-so-what-who-cares.md) page.

## Learning goals

- Explain what Flutter and Dart are, and why we chose them.
- Get a running app on a phone or emulator, with hot reload.
- Read the boilerplate: know what each folder is for.
- Understand the class-by-class plan and the release calendar.

## Concepts

- Everything is a widget. `StatelessWidget` vs `StatefulWidget`.
- `main()` -> `runApp()` -> `MaterialApp` -> `Scaffold`.
- Project layout: `lib/`, `pubspec.yaml`, `test/`, and the platform folders `flutter create` generates.
- Hot reload vs hot restart.

## In class

1. **Toolchain check.** Everyone runs `flutter doctor` and fixes red items.
2. **Create the repo.** Follow the README quick start (step 0 installs the issue/PR templates and VS Code settings): `git init`, commit the boilerplate, *then* run `flutter create` to generate `android/`, and review `git status` to see what it added.
3. **Choose the permanent application ID** and set it. See the [Play Store primer](../03-primer-play-store.md).
4. **Run the six-tab shell.** Tap each tab. Change the seed color in `lib/core/theme.dart` and hot-reload.
5. **Trace the code:** `main.dart` -> `app.dart` -> `shell/home_shell.dart` -> `features/*/..._screen.dart` -> `shared/placeholder_tab.dart`.
6. **Seed the backlog:** `tools/backlog/seed_issues.sh`. Walk the milestones.
7. **Run the test:** `flutter test`. Read `test/widget_test.dart` line by line.

## Discussion prompts

- Why six tabs? What does Material 3 recommend? (3-5; we use label-on-selected as a stopgap, and Jobs will make seven.)
- Why do the screens just show placeholders? What would you build first?

## Homework

- Add a seventh placeholder "Jobs" tab in a branch. Notice everything you had to touch (enum, screen, shell, test). Do not merge; discuss next week.
- Read the Play Store primer, sections 1 and 2.
- Complete the "Data source check" issue for **one** source from [data sources](../06-data-sources.md).

## Definition of done

- [ ] `flutter doctor` clean for the Android toolchain
- [ ] App runs on a device; hot reload works
- [ ] Repo on GitHub (private), backlog seeded, `main` branch protected
- [ ] Application ID chosen (not `com.example.*`)
- [ ] `flutter test` passes

## Best-practice notes

- Commit the boilerplate *before* generating platform folders, so the generated diff is reviewable.
- Never commit anything matching the `.gitignore` secrets section.
