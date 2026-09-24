# So what? Who cares? Flutter and Dart, in plain terms

Every technology claim gets the same two questions. If you cannot answer them
for *this* project, do not adopt the thing.

---

## Flutter

**What it is.** A toolkit from Google for building apps from one codebase. You
write Dart; Flutter draws every pixel itself instead of wrapping each platform's
native buttons.

**So what?**

- One codebase for Android now and iOS or desktop/web later. The Kitsap app has
  six tabs of mostly lists, maps, and forms; writing that twice is waste.
- **Hot reload** shows changes in under a second while you keep your place in the
  app. For a learner, the feedback loop is the whole game.
- Everything is a **widget**, and widgets compose. Once you can read one screen
  you can read them all.
- Because Flutter draws its own UI, the app looks and behaves the same on a
  five-year-old phone and a new one.
- Big, well-maintained ecosystem for exactly what we need: maps (`flutter_map`),
  navigation (`go_router`), state (`riverpod`), Firebase, and Maps/calendar
  hand-offs.

**Who cares?**

- **You**, because fast feedback means more learning per hour.
- **A resident with a two-minute window before a ferry**, because a smooth, fast
  app matters more than a clever one.
- **Whoever maintains this in a year**, because one codebase and one language
  is easier to hand over than two native apps.

**Honest costs.** Bigger app size than a minimal native app. Some platform
features (deep hardware, brand-new OS features) arrive in plugins after the OS
does. Flutter's own look is not "native"; you choose to embrace Material 3.
For a community info app these costs are small.

**Alternatives you should be able to name.** Native Kotlin (Android) and Swift
(iOS): best platform fit, double the work. React Native: JavaScript, uses native
widgets. A mobile website (PWA): no store, no install, weaker device hand-offs.
We pick Flutter for the learning loop and the single codebase.

---

## Dart

**What it is.** The language Flutter is written in. Statically typed, garbage
collected, with a syntax familiar to anyone who has seen Java, JavaScript,
C#, or Kotlin.

**So what?**

- **Sound null safety.** The compiler tells you where a value might be missing
  (a stop with no code, a route with no color), instead of your users finding out
  as a crash. Our data is messy; this helps daily.
- **Fast development, fast release.** It runs in a VM with hot reload during
  development and compiles ahead-of-time to native code for release.
- **`async`/`await` and `Future`/`Stream`** make network calls (ferry API) and
  live updates (bus positions) readable.
- **Modern features**: records, pattern matching, sealed classes, and enhanced
  enums let you model "loading / data / error" or "free / Discover Pass" so
  illegal states cannot be represented.
- **Single toolchain**: `dart format`, `dart analyze`, `flutter test` come with
  it. No configuration marathon.

**Who cares?**

- **You**, because a typed language catches whole classes of mistakes before
  you run the app, and the editor autocompletes accurately.
- **Users**, because null-safety and typed models mean fewer crashes.
- **Instructors and reviewers**, because the analyzer gives objective feedback
  on every student's code.

**Honest costs.** Dart is mostly used with Flutter, so skills transfer less to
other stacks than, say, JavaScript or Python. If you know either, you will
be productive quickly. If you know neither, Class 2 is designed for you.

---

## Mobile-first, for this app

**So what?** The people who need "when is the next ferry" are standing at a
terminal with a phone. Design for thumbs, small screens, bad signal, and
glances first; a bigger screen is an afterthought.

**Who cares?** Anyone with a phone and a few minutes: commuters, parents,
seniors, visitors, and people who found a pothole and wish it were easier to
report.

Practical consequences you will meet:

- Touch targets at least 48x48 dp.
- Layouts that survive large text sizes and small phones.
- Offline and slow-network states are normal, not edge cases.
- Show *when* data was last updated; stale is worse than blank.

---

## Applying the question to your own choices

When someone proposes a package, a pattern, or a feature, ask:

1. **So what?** What concretely gets better, and for which tab?
2. **Who cares?** Which user, or which future maintainer, feels it?
3. **What does it cost?** Lines of code, dependencies, permissions, Play Store
   form changes, and your attention.

If the answers are vague, put it in the "Later" milestone.
