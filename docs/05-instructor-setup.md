# Instructor setup: before Class 1

Four tracks with different lead times. Start all four on the same day.

| Track | Lead time | Blocks |
| --- | --- | --- |
| OneBusAway real-time key (Sound Transit) | about 2 business days | Class 9 live buses (fallback path) |
| Kitsap Transit BusTime API | unknown; may be weeks or a no | Class 9 live buses (preferred path); reviewed in Class 8 |
| WSDOT ferry access code | short; same-day to a few days | Class 6 ferry data |
| Play Console account + testers | account setup: hours to days; testers: weeks | Class 4 upload, and the whole release calendar |

Do not put any keys in the repo. Save them in a password manager and hand them
out only as needed (`env/dev.json`, or `firebase functions:secrets:set`).

## 1. OneBusAway real-time key

OneBusAway for Puget Sound routes developer API access through Sound Transit's
Open Transit Data (OTD) program.

- Start at [Sound Transit Open Transit Data](https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd).
- Also see [OneBusAway for Puget Sound: Developers](https://pugetsound.onebusaway.org/wiki/Developers).
- Request a key; note the expected lead time (about two business days).
- **Confirm Kitsap Transit coverage.** Ask, or test once you have the key: does
  the API list Kitsap Transit as an agency with real-time vehicle data? If it
  does not, the OneBusAway fallback for live buses does not work and only the
  Kitsap Transit route (below) remains.

Draft:

> Subject: Developer API key request (community app, Kitsap County)
>
> Hello, I am building a free, non-commercial community information app for
> Kitsap County as part of a Flutter learning course. I would like to request an
> OneBusAway Puget Sound API key. The key will be stored server-side (Cloud
> Function proxy) and responses cached to keep request volume low. Could you
> also confirm which agencies (specifically Kitsap Transit) are covered by
> real-time data? Thank you. - NAME, CONTACT

## 2. Kitsap Transit BusTime

- Find the Kitsap Transit developer or open data page, or email the agency's
  IT / public information contact. Ask specifically for: (1) BusTime API access
  (or a GTFS-realtime feed), (2) documentation, (3) terms of use and rate limits,
  (4) the current static GTFS URL and update schedule.
- Save the reply, even if it is no. Class 8 reviews the outcome.
- Static GTFS is separately available (for example via
  [Transitland](https://www.transit.land/feeds/f-c22y-kitsaptransit)); the
  Class 6 script validates whatever zip you have.

Draft:

> Subject: Request for BusTime / GTFS-realtime access for a non-commercial community app
>
> Hello, I teach a beginner mobile-development course and we are building a
> free, non-commercial app for Kitsap County residents. It would show Kitsap
> Transit routes and stops and, if permitted, live bus positions. Could you tell
> me whether Kitsap Transit offers API access to BusTime or a GTFS-realtime
> feed for developers, what documentation and terms apply, and how to request a
> key? We will credit Kitsap Transit as the data source and not imply that the app
> is official. Thank you. - NAME, CONTACT

## 3. WSDOT ferry access code

- The WSF APIs take an `apiaccesscode` query parameter. Register through the
  [WSDOT Traveler API page](https://www.wsdot.wa.gov/traffic/api/) to get one.
- Docs: [Schedule API](https://www.wsdot.wa.gov/ferries/api/schedule/documentation/rest.html),
  [Terminals API](https://www.wsdot.wa.gov/ferries/api/terminals/documentation/rest.html).
- Operations you will use: `/routes/{date}`, `/terminals/{date}`,
  `/scheduletoday/{routeId}/{onlyRemainingTimes}`, `/alerts`, and
  `/cacheflushdate` (poll it; refetch only when it changes).
- Dates are `YYYY-MM-DD`. Send `Accept: application/json`.

## 4. Play Console account and tester recruiting

- Create the developer account at [play.google.com/console](https://play.google.com/console).
  Decide **personal vs organization** now: personal accounts created after
  Nov 13, 2023 are subject to the 12-tester, 14-day rule (see the
  [Play Store primer](03-primer-play-store.md)).
- Complete identity verification early; it can take days.
- **Recruit testers now.** Target 15-20 people with Android phones and a Google
  account. Collect the Gmail addresses (you will add them to a tester list or a
  Google Group in Class 4). Explain: they must accept the opt-in link and
  **stay opted in for 14 days**; asking them to open the app a few times and send
  one line of feedback makes the production-access form easy to answer.
- Keep a spreadsheet: name, Gmail, device, opted in (date), still opted in,
  feedback received.

## Checklist

- [ ] OneBusAway key requested (date: ____)
- [ ] Kitsap Transit contacted (date: ____; reply: ____)
- [ ] WSDOT access code received
- [ ] Play developer account created and verified
- [ ] 15+ tester emails collected
- [ ] GitHub account/organization ready; repo name chosen
- [ ] Application ID chosen (e.g. `io.github.NAME.kitsaplocal`)
