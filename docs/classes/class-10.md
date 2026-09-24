# Class 10 - Ship the update

**New this week (bold):** nothing conceptually new. This is the [Class 7](class-07.md) process repeated on your own, faster and with less help. Repetition is the lesson.

## Learning goals

- Ship an update to a live app calmly and repeatably.
- Watch a rollout and decide whether to continue or halt.

## In class (same as before, with the differences noted)

1. **Freeze scope.** Anything not finished goes to "Later". Fix, do not add.
2. **Version.** Bump to `1.1.0+N` (the build number must be higher than the last upload).
3. **Regression pass** on a real device using the release build: every tab, offline mode, sign-in and sign-out, favorites, live buses, calendar and Maps hand-offs.
4. **Data safety form and privacy policy** updated for what v1.1 adds (sign-in, favorites sync, analytics, calendar). This must be done *before* release, not after.
5. **Store listing.** New screenshots if the UI changed; write release notes in plain words ("Live bus positions. Favorites. Add events to your calendar.").
6. **Build, upload, staged rollout** (start small, e.g. 10-20%), and watch **Android vitals** and reviews for a couple of days before expanding.
7. **Tag and record.** `git tag v1.1.0 && git push --tags`; close the milestone; note lessons learned.

## Retrospective (last 20 minutes)

- What was hardest, and what would we do differently?
- Which backlog items are next? (Alerts with moderation? Jobs tab? iOS?)
- What did the tester and store data teach us that we did not expect?

## Definition of done

- [ ] v1.1 in production at 100% (or paused with a written reason)
- [ ] Data safety form and privacy policy match the shipped app
- [ ] Git tag pushed; release notes saved in the repo
- [ ] Backlog re-triaged for v1.2 / Later

## Best-practice notes

- A boring release is a good release: checklists, staged rollouts, and one person watching vitals.
- If vitals spike, halt the rollout first, diagnose second.
