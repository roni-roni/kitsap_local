# Class 4 - Navigation, forms, theming

**New this week (bold):** Help tab, park filters, go_router, theme pass, and the first closed-test upload. **The 14-day count starts here.**

## Learning goals

- Navigate between screens with named routes and deep links.
- Build interactive controls and manage their state.
- Apply a consistent theme and think about brand.
- Run a closed test with real testers.

## Concepts

- `go_router`: `GoRouter`, `StatefulShellRoute.indexedStack` (the bottom-nav pattern), path parameters (`/ferry/:terminalId`), `context.go` vs `context.push`.
- Forms and controls: `FilterChip`, `SegmentedButton`, `SearchBar`, `TextField`, `Form` and validators.
- Local UI state: `setState`, and why filters will move to Riverpod in Class 5.
- Theming: `ColorScheme.fromSeed`, `TextTheme`, component themes, dark mode, spacing constants.
- External links: `url_launcher` (open volunteer links).
- Brand storytelling: name, voice, color, icon. Not a logo contest; a consistent identity that says "community, unofficial, helpful".

## In class

1. `flutter pub add go_router url_launcher`. Replace `HomeShell`'s hand-rolled index with a `StatefulShellRoute`. Confirm behavior matches, then add detail routes.
2. **Help tab.** Curate `data/help.json` (target 15 real organizations: use the schema in `data/README.md`). Load, group by category, tile with description + commitment + "Get started" button that opens the link.
3. **Park filters.** Owner (multi-select) and entry requirement; a "clear filters" action; an empty state.
4. **Theme pass.** Text theme, card and chip styling, dark mode, a simple About screen with the **unofficial-app disclaimer** and data-source credits.
5. **Closed-test upload.** In Play Console: create the closed track, add the tester list (email list or Google Group), upload the `.aab`, roll out, and copy the **opt-in link**.
6. **Testers opt in.** Send the link to your recruited testers today. Record the date: **Day 0**.

## Tester management (start now)

- Message: what the app is, opt in via the link, **stay opted in for 14 days**, open it a few times, reply with one thing that confused or broke.
- Track in a sheet: name, email, opted-in date, still-in?, feedback.
- Day 3: nudge the ones who have not opted in. Day 7: check the count.
- If you cannot get 12 opted in at once, recruit more; the clock counts *each tester's continuous days*.

## Discussion prompts

- Why does a filter belong in the app's state rather than in the widget? (Preview of Class 5.)
- What should the back button do after a deep link?
- What would make a volunteer link "trustworthy" enough to ship?

## Homework

- Verify every link in `help.json` and set `lastVerified`.
- Collect at least one piece of tester feedback and file it as an issue.
- Read the Data safety section of the Play Store primer.

## Definition of done

- [ ] go_router shell replaces the manual shell; deep link to a ferry terminal works
- [ ] Help tab with 15+ verified organizations
- [ ] Park filters with an empty state
- [ ] Dark mode looks right; About screen has disclaimer and credits
- [ ] **Closed-test build live, 12+ testers opted in, Day 0 recorded**

## Best-practice notes

- Make the empty state a designed screen, not an afterthought.
- Do not copy logos or seals for organizations; link to them.
