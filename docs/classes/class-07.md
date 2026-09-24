# Class 7 - Release and first submission

**New this week (bold):** production-access application, store listing, privacy policy, Data safety form, and the v1 submission.

Read the [Play Store primer](../03-primer-play-store.md) first. This class is a guided checklist, not new code.

## Learning goals

- Prepare a release build and a complete Play Store listing.
- Answer the production-access form truthfully and specifically.
- Understand what Google reviews and what happens after you submit.

## In class

1. **Production access.** Fill in (or refine and submit) the application. It asks about:
   - Your closed test: how you recruited testers, how many, how engaged.
   - The app: who it is for, what value it gives.
   - Production readiness: what feedback you received and **what you changed because of it**. Use the issues that testers generated; specifics beat generalities.
2. **Privacy policy.** Write and publish (GitHub Pages works). State what the app collects (v1: likely nothing personal beyond what Play/OS provide), what third-party services it calls (WSDOT, map tiles), how to contact you. Keep it true. Update it when Class 8 adds analytics and sign-in.
3. **Store listing.** Name, short and full description, screenshots (real, phone-sized), icon, feature graphic. Include the **unofficial-app** statement and data-source credits. No county seals or agency logos.
4. **Forms.** Data safety, content rating, target audience, ads, government-app declaration, app access. Answer for what the app *and its SDKs* actually do.
5. **Release build.** Bump the version (`1.0.0+N`), build the `.aab`, test that **exact** build on a real device (release mode behaves differently from debug).
6. **Submit** to production once access is approved; use **staged rollout** if offered. If access is not yet approved, finish everything else and submit the moment it is.

## While you wait

- Keep testers opted in; they are still your best early feedback.
- Do not change the app's declared behavior mid-review.
- Start the Class 8 planning: what did testers ask for?

## Discussion prompts

- Which question on the production-access form is hardest to answer honestly for us?
- What in the Data safety form depends on a package you added?
- What is the smallest thing that could get a first submission rejected?

## Definition of done

- [ ] Production access approved (or waiting; everything else ready)
- [ ] Privacy policy URL live
- [ ] Store listing, screenshots, forms complete
- [ ] Signed release `.aab` tested on a device
- [ ] **v1 submitted**; release notes written

## Best-practice notes

- Answer forms with specifics from your own issue tracker.
- Keep a `docs/release-checklist.md` (copy the checklist from the primer). You will reuse it in Class 10.
