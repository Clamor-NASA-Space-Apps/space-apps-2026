# The challenge's Resources tab and what Outpost Gale uses (15 Nov 2026)

The tab was read on 15 Nov 2026. Every fetch below was made that morning. Raw responses are in `assets-cache/data-snapshots/*_2026-11-15.json`; the game shows them as ARCHIVED, never as live. The records the game reads are in the game repo, `data/nasa.json`. Fact-check rows: `factcheck.md` 281 to 292.

| Resources-tab item | Did it answer on 15 Nov 2026? | Does the game use it? | How |
|---|---|---|---|
| NASA Open APIs (api.nasa.gov) | Yes for DONKI (CME, CMEAnalysis, notifications, GST, SEP). `DONKI/FLR` 404. Mars Rover Photos 404 "No such app". APOD not tried | Yes | The door we fetched DONKI through, with our own key (never shipped in the game) |
| DONKI (space weather) | Yes, through api.nasa.gov. The direct CCMC host timed out | Yes | Sol 5's solar storm is the real far-side eruption of 20 May 2024: activity ID `2024-05-20T05:36:00-CME-001`, 1927 km/s (row 281). The Gannon storm's Kp 9.0 (row 284) is on hand for the handbook |
| RadLab (OSDR radiation dosimetry) | The API yes. The web pages answered 500, so the units come from the documentation page as archived on 22 May 2024 (row 285) | Yes | Curiosity's own RAD readings through the storm (4.5 before, peak 303.99 μGy/hour at 06:15 on 20 May 2024, row 286) and a quiet-day comparison of the ISS Columbus lab with Gale (rows 287 and 288) |
| NASA OSDR (search API) | Yes | Small | One study named on the crew health page: OSD-342, muscle and bone loss in mice on the ISS (row 290) |
| Mars Trek | Its catalogue search yes | Not confirmed | See below |
| Canadian Space Agency education pages (two) | Not fetched | No | |

## What failed, plainly
- DONKI flare records (`FLR`): 404 from upstream for 2024-05-14, 2024-05-19 to 21 and 2024-10-03. So the flare class "X12" is still sourced to JPL only (row 37), not to DONKI. The DONKI list of particle events (`SEP`) for 18 to 24 May 2024 is empty.
- DONKI's notice for the 20 May 2024 eruption names Juno and Solar Orbiter, not Mars (row 282). The link to Mars is JPL's release (row 37) and Curiosity's RAD readings in RadLab (row 286).
- RadLab gives absorbed dose rate (μGy/hour) only for these instruments; its dose-equivalent column (Sv) is empty. So nothing here can be set beside the 0.67 mSv a day of row 32.
- The RadLab readings add up to about 1,480 μGy on 20 May 2024, far below JPL's "8,100 micrograys" (row 289). We do not know why. Show one or the other, never both as the same thing.
- Mars Rover Photos: the endpoint is gone (row 292).

## The terrain and Mars Trek
The game's ground is a real HiRISE elevation model: `DTEEC_018854_1755_018920_1755` (the `note` in the game's `data/terrain.json`). Mars Trek serves a product named "MRO HiRISE, Gale Crater DEM" (`Gale_DEM_SMG_1m`), a mosaic over 137.12 to 137.73 E, 4.93 to 4.25 S. Its catalogue search for "018854" finds nothing. Whether our model is one of the pieces of that mosaic: **not confirmed**. So we credit HiRISE for the terrain and do not claim Mars Trek.

## Wording for the screen
- Sol 5 alert, source line: "Real storm: 20 May 2024. Data: NASA DONKI (CME 2024-05-20T05:36:00-CME-001) and Curiosity RAD from NASA RadLab (ARCHIVED 15 Nov 2026)"
- Handbook: "Quiet day, 19 May 2024: a detector inside the ISS read about 8.5 μGy an hour. Curiosity's at Gale read about 3.9. Next morning the storm pushed Curiosity's to 304. Data: NASA OSDR RadLab (ARCHIVED 15 Nov 2026)". The two averages are our maths (row 288).
- Credits: "Space weather: NASA DONKI, through NASA Open APIs (api.nasa.gov). Radiation readings: NASA OSDR RadLab. Crew health study: NASA OSDR. All fetched 15 Nov 2026 and shown as ARCHIVED. Not endorsed by NASA."
