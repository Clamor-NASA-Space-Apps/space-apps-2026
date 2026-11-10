# Roadmap: Junior Astronaut Mission Trainer

The full plan is in `plan.md`. This file holds the subtasks to come back to. Tick each one when it's done.

Key dates: rehearsal Nov 9–10 · Resources tab and 2026 guides open Nov 13 · hackathon Nov 14–15 (submit by 18:00, hard deadline 23:59 local).

## Phase A: research and Docmost ✅ (Nov 7)
- [x] Save sources to `research/junior-astronaut/` and write `sources.md`
- [x] Fact-check table (`factcheck.md`, 56 claims)
- [x] Rebuild the Docmost space `NASA`: 11 new pages, existing pages corrected and moved

## Phase A+: pictures in the Docmost pages 🖼️ (14 of 15 done, 9 Nov)
- [x] 14 NASA pictures on Power, Life support, Radiation, Weather, Landing and Intro cinematic, each under its heading with a caption and credit (`research/junior-astronaut/images/credits.md`)
- [x] How: NASA Images API to find → curl + ffmpeg (≤1400 px) → Claude-in-Chrome `file_upload` into a temporary file input → `POST /api/files/upload` → image node inserted via JSON. (Fetching NASA files directly in the tab fails: `~orig.jpg` has no CORS header)
- [ ] Moon vs Mars? already has 3 of Ravindu's pictures; add a NASA side-by-side only if the team wants
- [ ] Game design and story: add our own screenshots after 14 Nov
Goal: every page gets 1–3 pictures under the right heading, so a beginner sees what is described.

**Rules**
1. **Find:** Google Images (through Chrome MCP) is fine for *finding* a picture. **Download from the original source page**, never from Google's thumbnail.
2. **Prefer NASA images:**
   - Sources: images.nasa.gov, science.nasa.gov, photojournal.jpl.nasa.gov, jpl.nasa.gov.
   - NASA media is generally not copyrighted. Credit it as "NASA/JPL-Caltech", or whatever credit the page shows.
3. **Anything that isn't NASA:**
   - Check the licence before using it (CC0 / CC-BY is fine with credit).
   - If you can't confirm the licence, don't use the picture.
   - Skip stock photos and news-agency photos.
4. **Never the NASA logo** ("meatball"), the "worm" logotype or the NASA seal.
5. **Captions:** every picture gets a one-line caption, written so a kid understands it, plus the credit and the source URL.
6. **Files:**
   - Save each picture to `research/junior-astronaut/images/<page>/<name>.<ext>`.
   - Add a row to `research/junior-astronaut/images/credits.md`.
7. **Upload:**
   - Use Docmost's attachment upload, run from the logged-in tab. Check the DTO in `apps/server/src/core/attachment/` first.
   - Then insert an image node under the matching heading. Use `dm.fix`-style JSON editing so nothing else on the page changes.
   - Verify with `dm.nodeTypes` (image count) and one screenshot per page.

**Picture list (candidates to search for)**

| Page | Heading | Picture |
|---|---|---|
| Power | 1. Where does the power come from? | MMRTG photo; a solar panel or array on Mars (InSight) |
| Power | 2. How a dust storm killed Opportunity | Opportunity's sky going dark (simulated tau views, JPL 2018); MRO global dust map, June 2018 |
| Power | 3. InSight: death by dusty panels | InSight's dusty final selfie (2022) |
| Life support | 1. Air | MOXIE being lowered into Perseverance |
| Life support | 3. Food | Veggie red romaine lettuce on the ISS |
| Life support | 4. A year in a pretend Mars base | CHAPEA 3D-printed habitat, Houston |
| Radiation | 2. The real numbers | Curiosity's RAD instrument |
| Radiation | 3. Solar storms | Curiosity navcam "snow" from the 20 May 2024 storm; SDO flare image |
| Weather and talking to Earth | 2. Cold / 4. Dust | Blue sunset at Gale crater (Curiosity Mastcam) |
| Weather and talking to Earth | 5. Talking to Earth | Deep Space Network dish |
| Weather and talking to Earth | 7. Gale crater | Curiosity at Gale / Mount Sharp |
| Moon vs Mars? | top | Moon and Mars side by side (NASA) |
| Intro cinematic | shot list | Earth–Mars transfer orbit diagram; Perseverance EDL diagram |
| Landing | 1. Seven minutes of terror | EDL sequence graphic |
| Game design and story | later | our own screenshots once the game exists |

## Phase B: tooling and downloads (started Nov 7)
- [x] NASA 3D models + planet textures → `assets-cache/nasa-3d/` (10 files, 14.5 MB)
- [x] Kenney Space Kit → `assets-cache/kenney/space-kit/` (153 GLB, CC0). Has domes, corridors, generators, dishes, rover, rocket parts, platforms, rocks, astronauts. **No solar panels → forge recipe.**
- [x] Kenney Space Station Kit (97 files), Interface Sounds (100 ogg), Sci-fi Sounds (73 ogg), all CC0, in `assets-cache/kenney/`
- [x] Data snapshots → `assets-cache/data-snapshots/` (NOAA flares, Kp, Curiosity weather 4,745 sols)
- [ ] DONKI snapshots: FLR/SEP/CME/GST May 2024 + FLR Oct 2024. On Nov 7 api.nasa.gov returned 503 even with our key, and the CCMC endpoints timed out. Retried Nov 8: still 503 ("upstream connect error … connection timeout"). Retry daily; the fetch loop is in the session log, and the key is in `.env.local`
- [x] npm cache warmed with full dependency trees (three 0.187, vite 8.3, gltf-transform 4.5, playwright-core 1.65, postprocessing, n8ao, three-bvh-csg)
- [x] three.js skills installed globally (13 CloudAI-X skills, reviewed: SKILL.md only, no scripts)
- [x] `tooling/forge/lib.py` + `smoke_crate.py`: GLB + 3 previews in about 15 s (Blender 5.2, Cycles CPU)
- [x] `tooling/tools/capture-view.mjs`: headless Brave + SwiftShader, preset views, state dump, error gate (smoke test passes)
- [ ] Fedora's Blender logs an OCIO 2.5 vs 2.4.2 mismatch, so previews use raw colour. Fine for shape checks; check final colours in three.js
- [x] `tooling/` pushed to Gitea as `agent-forge-3d` (git@100.108.184.127:ravindu644/agent-forge-3d.git)
- [ ] Mirror `agent-forge-3d` to public GitHub before Nov 14 (Ravindu decides when; cite it in the submission)
- [x] Rehearsal repo `storm-night-lighthouse` created on Gitea (README with the no-reuse rule)
- [x] Workspace repo initialised in `~/Documents/NASA-Space-apps` (plan, roadmap, research, asset cache; the two repos above are ignored)
- [x] Workspace repo pushed to Gitea `nasa-space-apps-2026`; AGENTS.md + CLAUDE.md symlink in all three repos
- [x] Personal api.nasa.gov key → `.env.local` (chmod 600, gitignored). Use it only for snapshot fetching on our machine. **Never ship it in the game's JS**: anything in a browser game is public. Live data in the game comes from NOAA (no key needed)
- [x] Piper TTS in `~/opt/piper` with two openly licensed voices: `en_US-kristin-medium` (public domain) and `en_US-libritts_r-medium` (CC BY 4.0, many speakers). 1.6 s per line, about 14 KB per line as Opus via ffmpeg. Skipped `lessac`, `amy`, `hfc_female` (restricted or unclear licences)
- [x] Fonts cached in npm: `@fontsource-variable/lexend` (designed for easier reading), `@fontsource-variable/fredoka` (headings), both OFL-1.1
- [x] `gltf-transform optimize` tested: Perseverance 4.99 MB → 2.0 MB in 2 s

## Team call: 9 Nov, 10 PM
- [x] "Decisions for the team" section added to Game design and story: 9 taste items (A), 7 story problems with recommended fixes (B), 6 fixed rules (C). Sub-pages have ✏️ notes; page names are links everywhere
- [ ] Before the call: check all 4 teammates can edit the `NASA` space (Settings → Members)
- [ ] After the call ("decisions are in"): apply the decisions to the design pages, the facts, `plan.md` and `AGENTS.md`; fact-check any new science goal

## Phase C: rehearsal "Storm Night Lighthouse" (Nov 9–10)
- [x] Factory set up (10 Nov): workflow, code rules, commits, modules, token rules and self-improvement in `tooling/AGENTS.md`; projects built in `tooling/projects/<name>/` (rehearsal moved there)
- [ ] Run the rehearsal through the factory: open `claude` in `tooling/projects/storm-night-lighthouse/` and say "build this game"
- [ ] Two timed sessions, the same length as the hackathon days
- [ ] Log time per lane, tokens, stuck points, screenshot loops, fps on the weakest team laptop
- [ ] Retro page in Docmost; fix tooling and agent briefs (Nov 11)
- [ ] Factory lessons from the rehearsal folded back into `tooling/` (tools + gotchas)

## Phase D: design pack (Nov 11–13)
- [ ] `GAME_DESIGN.md`, `DESIGN.md` (art direction), `CONTRACTS.md` drafted as Docmost pages
- [ ] Nov 13: read the challenge Resources tab and the 2026 Submission + Judging guides; update the checklist page
- [ ] Email the Colombo Local Lead: event start/end times, and whether design docs written in advance are OK
- [ ] Team names filled in on "Start here: our path"

## Hackathon (Nov 14–15)
- [ ] H0: paste the design pack, scaffold, contracts
- [ ] Five agent lanes (rules, world, forge, screens, cinema+sound), merges at H4 and H8
- [ ] First playable by H14; playtest; tune
- [ ] Day 2: polish, credits screen, AI-use paragraph, 30 s video with English subtitles, GitHub Pages, submit by 18:00

## Open questions research (8 Nov) ✅
- [x] MOXIE power (300 W, user's find confirmed on NASA's page), habitat power ranking, ISS air machine power, plants for air, soil depth, plastic vs water, science goal source. Fact-check rows 57–91; Docmost Power, Life support, Radiation, Game design (B7), NASA data, References updated
- [ ] Still open: ISS water recycler power (no NASA number); a plain NASA "X cm of Mars soil cuts dose by Y%"; Röstel 2020 primary (Wiley blocks curl, read in browser); CDRA 1,000 W from an NTRS copy
- [ ] Optional: new Trade-off cards from these (oxygen maker vs night power; water tanks as shield)

## Survival deep dive (8 Nov) ✅
- [x] Mars survival 101 + Life support + Weather + Power + Radiation rebuilt in place: oxygen budget, CO₂ (Sabatier), water loop (CCAA, UPA, WPA, BPA), Mars water (soil, ice), food (sol-1 menu, shelf life, pick-and-eat timeline), pressure, suits, airlocks/suitports, perchlorate dust. 4 charts + 23 NASA photos. Fact-check rows 92–143
- [ ] Team call: the game design should use NASA's own first-mission plan (30 sols, tanks) as the backbone; oxygen maker = water splitter, MOXIE only as a "future tech" upgrade
- [ ] Still open: habitat heating power; current water-recycler power (only 2005 estimates)
