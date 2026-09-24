# Primer: Google Play Store rules that shape this course

Policies change. Treat this page as a map, and check the linked Play Console
Help pages before each release. Last checked against Play Console Help in
September 2026.

## 1. The rule that sets the calendar: closed testing

For **personal** developer accounts created after **November 13, 2023**, Google
requires a closed test with **at least 12 testers opted in continuously for at
least 14 days** before you can apply for production access. Points that trip
people up:

- Testers must **stay opted in** for the full 14 days. A tester who leaves before
  day 14 does not count, and a gap resets that tester's clock.
- Until you pass, the **Production** track is locked.
- You then **apply for production access** in Play Console: a short form about
  your closed test and tester engagement, your app's audience and value, and how
  you made the app production-ready (including changes based on feedback).
  Google says reviews usually finish within seven days, sometimes longer.
- **Organization** accounts are not subject to this requirement. (They need a
  D-U-N-S number and verification. Worth knowing if this project ever becomes a
  nonprofit or business.)

Source: [App testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465).

**What this means for the class plan:** you need a build in the closed-test track
by Class 4, and you need testers who actually open it. Recruit early (neighbors,
class members, friends, family, a local Facebook or Nextdoor group), aim for
15-20 sign-ups, and give them a short reason to open the app and a way to tell you
what broke. That feedback is also what the production-access form asks about.

## 2. Accounts and app identity

- One-time registration fee for a Play developer account. Use a Google account you
  can keep long term.
- **Application ID** (`com.yourname.kitsaplocal`) is **permanent** once uploaded.
  Choose it in Class 1 and do not ship anything as `com.example.*`.
- **Play App Signing**: Google holds the final signing key; you keep an *upload
  key*. Back up your upload keystore and its password somewhere safe (not git).
  Losing it means a reset process with Google.
- Upload an **Android App Bundle (.aab)**, not an APK: `flutter build appbundle`.
- **Version code** (the number after `+` in `pubspec.yaml`'s `version: 1.0.0+3`)
  must increase with every upload.
- **Target API level**: Play requires new apps and updates to target a recent
  Android API level, and raises the floor about once a year. Check the current
  requirement before Class 7 and keep Flutter up to date so its template does the
  right thing.

## 3. Store listing requirements

- App name, short description, full description.
- Icon (512x512), feature graphic (1024x500), and phone screenshots (real
  screenshots of the real app).
- **Privacy policy URL**, hosted publicly. GitHub Pages works.
- Contact email (public).
- **Do not imply the app is official.** This is a community app. Say so in the
  description and in an About screen. Do not use the county seal, city logos,
  Kitsap Transit or Washington State Ferries logos, or their names in the app
  title. Play's impersonation policy and trademark rules both apply.
- Do not copy content you do not have the right to copy. Link to agendas, forms,
  and pages rather than reproducing them.

## 4. Forms you fill in the console

| Form | What it wants | Where it bites |
| --- | --- | --- |
| **Data safety** | What data the app (and its SDKs) collects or shares, why, whether it is encrypted, whether users can request deletion | Must match reality. Adding analytics, sign-in, or crash reporting in Class 8-9 means **updating the form** before releasing |
| **Content rating** | Questionnaire | Answer honestly; UGC and location features change the rating |
| **Target audience** | Age groups | Choose adults/general; do not target children unless you accept the Families policy |
| **Ads declaration** | Does the app show ads | v1: no |
| **Government apps declaration** | Whether the app is made by or for a government entity | This app is not; answer accurately |
| **App access** | If parts are behind login, reviewers need credentials | Relevant once sign-in exists |

## 5. Policies that touch *this* app specifically

- **Account deletion.** If users can create an account in the app (Google
  Sign-In, Class 8-9), Play requires an in-app way to request deletion **and** a
  web link for it. Plan for it when you add sign-in.
- **User-generated content (UGC)** for the later Alerts and Jobs features.
  Play requires apps with UGC to have terms, **in-app reporting of objectionable
  content, the ability to block abusive users, and active moderation**. Design
  these *before* building the feature.
- **Location permissions.** v1 does not need the user's location; show the
  user's position on the map only if you request runtime permission and can
  explain why. Requesting less is easier to get approved.
- **Calendar access (Class 9).** Prefer handing an event to the calendar app via
  an intent (no permission), over reading/writing calendars directly (permission
  and Data safety implications).
- **Deceptive behavior / accuracy.** Ferry and bus data are safety- and
  time-sensitive. Show "last updated" times and say the source. Do not present
  stale data as live.
- **Third-party data and licenses.** Record the license or terms for every
  dataset (`docs/06-data-sources.md`). Map tiles from OpenStreetMap need visible
  attribution and have a usage policy that bars heavy use of the public tile
  servers; plan for a proper tile provider as usage grows.
- **Sensitive/permission-heavy SDKs.** Every SDK you add (analytics, ads, auth)
  contributes to the Data safety form.

## 6. Release tracks and staged rollouts

| Track | Purpose |
| --- | --- |
| Internal testing | Up to 100 testers, instant; good for your own quick checks |
| **Closed testing** | The 12 testers for 14 days. Testers join via an email list or Google Group and an opt-in link |
| Open testing | Public beta |
| **Production** | Everyone. **Staged rollout** (e.g. 10%, 50%, 100%) limits damage from a bad build |

## 7. First-submission checklist (used in Classes 7 and 10)

- [ ] Production access approved
- [ ] Version name and **version code** bumped
- [ ] Release `.aab` built and signed; upload keystore backed up
- [ ] App icon, feature graphic, screenshots, descriptions final; unofficial-app disclaimer present
- [ ] Privacy policy URL live and accurate
- [ ] Data safety form matches the app (SDKs included)
- [ ] Content rating and target audience complete
- [ ] Release notes written (what's new, in plain words)
- [ ] Tested the exact release build on a real device (not just debug)
- [ ] Staged rollout selected; someone is watching **Android vitals** (crashes, ANRs) and reviews for the first days

## 8. iOS note

This course targets **Android and the Play Store**. Building for iOS requires a
Mac and an Apple Developer Program membership, so it is scheduled as a "Later"
backlog item. The Flutter code is the same; the release process is not.
