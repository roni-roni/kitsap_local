'use strict';

/**
 * STUB (Class 9). Holds API keys server-side so they never ship in the APK.
 *
 * Setup once you have a Firebase project (Class 8) and the OneBusAway key:
 *   firebase functions:secrets:set OBA_API_KEY
 *   firebase deploy --only functions
 *
 * Then set PROXY_BASE_URL in env/dev.json to the deployed function URL.
 *
 * Design rules for this proxy:
 *  - Keys come from secrets, never from source or the client.
 *  - Cache upstream responses for a few seconds so 1,000 phones = 1 upstream call.
 *  - Return only the fields the app needs (small payloads, fewer surprises).
 *  - Cap instances so a bug can't run up a bill.
 */

const { onRequest } = require('firebase-functions/v2/https');
const { defineSecret } = require('firebase-functions/params');

const OBA_API_KEY = defineSecret('OBA_API_KEY');

// TODO(Class 9): confirm base URL and endpoint in the current OneBusAway
// Puget Sound API docs, and confirm Kitsap Transit's agency id from
// `agencies-with-coverage.json` before relying on this.
const OBA_BASE = 'https://api.pugetsound.onebusaway.org/api/where';
const CACHE_TTL_MS = 10 * 1000;

const cache = new Map(); // url -> { at, body }

async function cachedJson(url) {
  const hit = cache.get(url);
  if (hit && Date.now() - hit.at < CACHE_TTL_MS) return hit.body;
  const res = await fetch(url, { headers: { Accept: 'application/json' } });
  if (!res.ok) throw new Error(`upstream ${res.status}`);
  const body = await res.json();
  cache.set(url, { at: Date.now(), body });
  return body;
}

/** GET /vehicles?agency=<id>  ->  { vehicles: [{id, lat, lon, routeId, heading, updated}] } */
exports.vehicles = onRequest(
  { secrets: [OBA_API_KEY], maxInstances: 3, region: 'us-west1' },
  async (req, res) => {
    const agency = String(req.query.agency || '').replace(/[^A-Za-z0-9_-]/g, '');
    if (!agency) {
      res.status(400).json({ error: 'missing agency' });
      return;
    }
    try {
      // TODO(Class 9): verify this operation exists for the agency; the
      // alternative is `trips-for-route` with includeStatus=true.
      const url = `${OBA_BASE}/vehicles-for-agency/${agency}.json?key=${OBA_API_KEY.value()}`;
      const data = await cachedJson(url);
      const list = (data && data.data && data.data.list) || [];
      const vehicles = list
        .filter((v) => v.location)
        .map((v) => ({
          id: v.vehicleId,
          lat: v.location.lat,
          lon: v.location.lon,
          routeId: v.tripStatus && v.tripStatus.activeTripId ? v.tripStatus.activeTripId : null,
          heading: v.tripStatus ? v.tripStatus.orientation : null,
          updated: v.lastUpdateTime || null,
        }));
      res.set('Cache-Control', 'public, max-age=10');
      res.json({ vehicles });
    } catch (err) {
      console.error(err); // the key is in the URL: never log `url`
      res.status(502).json({ error: 'upstream unavailable' });
    }
  },
);
