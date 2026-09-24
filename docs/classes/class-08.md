# Class 8 - Post-launch and update planning

**New this week (bold):** analytics and Play vitals, backlog triage, Firebase and Google Sign-In, and the Kitsap Transit outreach review.

## Learning goals

- Read product signals and turn them into a prioritized plan.
- Add Firebase to a Flutter app safely.
- Implement Google Sign-In as an *optional* account, not a gate.
- Make a data-source decision when an outside party has answered (or not).

## In class

1. **Play vitals and reviews.** Open Play Console: crash rate, ANRs, installs, ratings, reviews. Anything above a threshold becomes a P0 issue.
2. **Analytics.** Add Firebase Analytics and Crashlytics; log a small set of meaningful events (tab viewed, ferry terminal opened, park filter used). No personal data in events. Update the **Data safety form and privacy policy** to match before the next release.
3. **Backlog triage.** Sort every open issue into: fix now (v1.0.x), v1.1, Later. Tie each v1.1 item to a tester or vitals signal. Cut anything without a "who cares".
4. **Firebase project and Google Sign-In.**
   - Create the Firebase project, register the Android app (with your release **and** debug SHA-1s), run `flutterfire configure`.
   - `flutter pub add firebase_core firebase_auth google_sign_in`.
   - Sign in/out, show the user, keep every v1 feature working *without* signing in.
   - Keep generated config (`google-services.json`, `firebase_options.dart`) out of git as the `.gitignore` states; each developer regenerates it.
   - **Plan account deletion** now: Play requires in-app deletion and a web link if users can create accounts.
5. **Kitsap Transit outreach review.** What did they say? Decide the live-bus source: BusTime, OneBusAway (if it covers Kitsap), or defer. Record the decision.

## Discussion prompts

- What is the smallest useful thing we can do with sign-in? (Favorites sync is the honest answer.)
- What analytics event would change a decision? What event would we never look at?
- How do we decide between fixing a crash and shipping a feature?

## Homework

- Write a one-page v1.1 plan: scope, order, risks, and what is deliberately out.
- Draft the account-deletion flow on paper.
- Confirm the Cloud Function proxy plan and get the OneBusAway key into Secret Manager (not the repo).

## Definition of done

- [ ] Vitals reviewed; P0 issues filed
- [ ] Analytics + crash reporting working; Data safety form and privacy policy updated
- [ ] Google Sign-In works and is optional
- [ ] v1.1 scope agreed and the backlog re-triaged
- [ ] Live-bus data decision recorded

## Best-practice notes

- Add SDKs deliberately: each one changes your Data safety form and your responsibilities.
- Measure the thing you would act on.
