# Plan: Junior Astronaut Mission Trainer — from research to a winning build

## Context
- **Team:** 4 beginners. Space Apps 2026, local event in Colombo, Nov 14–15 (2 days). Building a three.js browser game for kids aged 7–12.
- **What we have so far:**
  - A thin intro page.
  - A research plan with empty tables.
  - A "Moon vs Mars" page that contains errors.
  - Five empty Travel/Landing pages.
  - No storyline.
- **User's asks:**
  - Restructure the Docmost space and get all 4 of them onto one clear path.
  - Write a storyline aimed at winning.
  - Design an AI build method: fewest tokens, highest quality, no slop, no reinvented wheels, and hand-made 3D assets only where nothing exists.
- **Sources read (2026-11-07):**
  - Challenge page. The Resources tab opens Nov 13.
  - The challenge author's video, all subtitles.
  - Both Docmost pages, plus the rest of the `NASA` space.
  - Three research agents' reports.
  - The live 2026 FAQ.
- **What the brief and video want:**
  - Every choice costs something, with no free option.
  - 2–3 core resources.
  - Real NASA data, credited inside the game, and never presented as live when it isn't.
  - Browser-based, no login.
  - Stand-out ideas: real space weather tied to choices, replayability, a short write-up of the data used.
  - In the video: "Not a quiz, not a slideshow, a living simulation", and "No unlimited resource mode in space". The author points to DONKI (NASA's space weather database).
- **Rules (2026 FAQ, checked live):**
  - "Teams are not allowed to begin working on the challenges prior to the hackathon."
  - SI (AI) tools are allowed. The submission must describe how they were used.
  - Teams have 6 members or fewer.
  - 2025 submission guide: a demo video of up to 30 s or up to 7 slides, in English. No NASA logos in AI-made content. Cite all sources. Open-source licence (Apache 2.0 is the default).
  - The 2026 Submission and Judging guides come out Nov 13. Judging criteria in the 2025 guide: Impact, Creativity, Validity, Relevance, Presentation.

## Locked decisions (from the user)
- **Before Nov 14:**
  - Prepare design docs now.
  - Run a **timed rehearsal on a different game**, to see whether the pipeline fits in 2 days.
  - The Mars game itself gets built fresh at the hackathon.
  - The user accepts the grey-area risk of preparing design docs early.
  - Mitigation: generic tooling goes into a public open-source repo before the event and gets cited. No rehearsal game code or assets move into the hackathon repo.
- **Intro:** a cinematic you watch, 30–90 s, not playable.
- **Failure:** PG "mission lost" ending, then a replay of what went wrong, then Retry.
- **Machine:** one laptop runs Claude and every agent. The venue network may be slow, so download everything before the event and make the game run offline.
- **Blender 5.2.2 LTS** is installed at `/usr/bin/blender`. `blender -b` was checked and works.
- **Browser:** Brave at `/usr/bin/brave-browser`. `playwright-core` uses it through `executablePath`, so no Chromium download is needed.

## Phase A — Research, fact-check, rebuild the Docmost space (now)
1. Save every cited page to `research/junior-astronaut/` (curl), with a `sources.md` listing them.
2. Check every claim with `tools/kwic.py` and mark it ✅ (checked), ⚠️ (reported) or ❌ (not confirmed).
   - Check all LEADs from the agents first: MMRTG ~110 W, Veggie lettuce 33 days, Earth background 2.4 mSv/yr, the 2018 storm length.
3. Corrections for the existing pages:
   - Moon gravity is 0.166 g (1.62 m/s²), not "1.6 g".
   - The trip is about 7 months (Perseverance 203 days, Curiosity 253), not 9.
   - A Mars ship does not pass the Moon.
   - A sol is 24 h 39 m.
   - Round-trip radio delay is about 6–44 min.
   - The Moon's "year length" row is muddled.
   - "Severe thyroid dysfunction" overstates what is known.
   - The intro page says "build an outpost". The brief says kids **run and manage** one, and it also lists communication delay.
4. New tree. Existing pages are kept and moved, the empty ones get repurposed, and nothing is deleted. Style: a friend explaining things, numbered emoji headings, one callout per section, a TL;DR, "kid version" lines, no em dashes.
   ```
   🚀 Junior Astronaut Mission Trainer   (root: 30-sec version, judges' checklist, facts-to-remember table, page map, the path to Nov 15)
     🧭 Start here: our path            (who does what, timeline, rules, rehearsal)
     🔴 Mars survival 101               (the 4 research tracks, filled in and fact-checked)
        ⚡ Power · 🫁 Life support · ☢️ Radiation · 📡 Weather & talking to Earth
     🎑 Moon vs Mars?                   (the user's page, corrected, with a corrections note)
     ⚖️ Trade-off cards                 ("do X, gain Y, lose Z", each with a real number, source and kid version)
     🛰️ NASA data we'll use             (tested live: DONKI, NOAA backup, Curiosity weather, OSDR, NASA 3D models, textures)
     🎮 Game design & story              (the existing Travel/Landing pages are reused as the act pages)
     🤖 How we build it with AI          (stack, agents, skills, asset forge, hour-by-hour runbook)
     🏆 Judging & submission checklist
     📚 References & fact-check table
     📋 Research Plan · ⁉️ Better to know facts · 🔗 Resources · ⬜ Whiteboards   (kept; the research tracks link to their filled pages)
   ```
5. Publish with `tools/docmost-browser.js`, 3 pages per call. Verify with `dm.tree`, `dm.nodeTypes`, and one screenshot per page type.

## Phase B — Tooling and downloads (now; network is slow, so do it once)
- **Skills:**
  - `npx skills add cloudai-x/threejs-skills` (the most-used three.js skill pack, updated Oct 2026).
  - Copy the test hooks from the develop-web-game pattern (trailofbits mirror).
  - Already installed: design-taste-frontend, frontend-design, ponytail.
  - Agents read `threejs.org/docs/llms.txt` (5 KB), not the 379 KB full version.
- **Browser checks:**
  - `playwright-core` driving Brave (`executablePath:'/usr/bin/brave-browser'`), so no browser download.
  - claude-in-chrome for manual spot checks.
- **npm cache warm-up:** `three`, `vite`, `@gltf-transform/cli`, `playwright-core`, `postprocessing`, `n8ao`.
- **Assets** (≈ 40 MB total; I'll list each file and size before downloading):
  - CC0 kits: Kenney Space Kit and Space Station Kit.
  - NASA-3D-Resources: Perseverance 5 MB, Ingenuity 2 MB, Habitat Demo Unit 1.2 MB, Astronaut, Curiosity Landing Site STL 2.8 MB (real Gale crater terrain).
  - Planet textures: `Mars.jpg` 1 MB, plus Earth and Moon.
  - One 2k HDRI from Poly Haven (CC0).
  - DONKI and NOAA snapshot JSON.
  - CC0 sound effects from Kenney.
- **Voice:** Piper TTS (offline, open source) to pre-render voice lines. Credited as SI audio.
- **Generic tooling repo** (public before the event, cited at submission):
  - `forge/lib.py`: Blender helpers.
  - `tools/capture-view.mjs`: preset-camera screenshots.
  - `CLAUDE.md` template.
  - Smoke test: a bevelled crate goes to GLB plus 3 preview PNGs via `blender -b -P`.

## Phase C — Timed rehearsal (Nov 9–10, two sessions the length of the hackathon days)
- **Game: "Storm Night Lighthouse"** (a different domain, same pipeline):
  - A 3D island diorama and a keeper's resources (lamp oil vs generator fuel vs keeper energy).
  - Storms arrive as events.
  - A cinematic intro (boat arrival).
  - PG failure plus a replay.
- It exercises every lane: pure-JS sim + tests, scene from kit GLBs, forge recipes, HTML HUD, cinematic, audio, deploy.
- **What to measure:** wall-clock time per lane, tokens per lane, merge conflicts, where agents got stuck, screenshot-loop count, fps on the weakest team laptop.
- **Retro:** results go on a Docmost page. Fix the tooling and briefs (Nov 11–13). The rehearsal game is not reused.

## Phase D — Prepared design pack for the real game (Nov 11–13; user accepted the risk)
Written as Docmost pages (research and design, no code). Pasted into the repo at 0:00 on Nov 14.
- `GAME_DESIGN.md`: the story, loop, meters, event deck and numbers table, each number with a source.
- `DESIGN.md`: art direction.
  - Mars ochre with habitat white and safety-orange accents.
  - Flat PBR with bevelled kit look.
  - One light rig.
  - Fonts.
  - Icon set.
  - UI for kids: big targets ≥ 48 px, icons before words, ≤ 8 words per card, voice-over.
  - Budgets.
- `CONTRACTS.md`: the `state` shape, event schema, prefab registry fields, and the `window.render_game_to_text` / `advanceTime` hooks. These let lanes work without reading each other's code.
- After the Nov 13 Resources drop: add whatever the organisers point at.

## The game (proposal)
- **Working title:** **Outpost Gale**.
- **Site:** Gale crater. Curiosity measured the radiation (0.67 mSv/day) and the weather there, and NASA publishes its terrain.
- **Player:** the Junior Commander. Two cartoon astronauts with visors, so no faces are needed.
- **Sidekick:** PIP, a small original helper rover. It speaks in icons and short voice lines.

### Intro cinematic (~60 s, not playable, captions use real numbers)
1. Earth and Mars line up only every 26 months: launch.
2. The Moon shrinks behind you; it isn't on the way.
3. 7 months of cruise, compressed. A real solar storm passes: "May 2024, NASA's Curiosity measured it on Mars" (archived, labelled as such).
4. "Seven minutes of terror": the landing at Gale. "Sol 1."

### Core loop (one sol ≈ 60–90 s, mission = 30 sols)
- **Three meters only, matching the brief:**
  - ⚡ **Power**: the currency everything spends.
  - 🫁 **Life support**: air from the oxygen maker, water from the recycler, food from the greenhouse, all combined.
  - 🛡️ **Crew health**: radiation dose.
- **Day:** solar charges the batteries. Spend power on systems and science. Send PIP or the crew outside: science points cost dose.
- **Night:** heaters drain power. Choose what to switch off.
- **Build pads:** habitat, solar array, battery, oxygen maker (MOXIE-style), water recycler, greenhouse, storm shelter, comms dish. Each draws power and costs cargo.
- **Win:** the crew is alive at sol 30 when the resupply ship lands. Score = science + crew health + fact cards collected.

### Event deck (seeded, so every run is different; each event shows a "Real NASA fact" card with its source)
- **Dust storm:** sunlight drops sharply. The real 2018 storm ended Opportunity. Choose: retract the panels and lose power tonight, or leave them out and risk losing more (the author's own example).
- **Solar storm:** live NOAA or DONKI data if online, otherwise the archived May 20, 2024 event at 8,100 µGy, "about 30 chest X-rays". Choose: move into the shelter (science stops, power drains) or finish the trip outside (more dose).
- **Ask Earth:** advice arrives after a 3–22 min delay, compressed into a waiting animation. Choose: wait, or decide alone.
- **Solar conjunction:** the Sun blocks contact with Earth for about 2 weeks. No help available.
- **Greenhouse:** lettuce needs about 33 days. Grow lights compete with the heaters.
- **Dirty panels:** cleaning them on a walk outside restores power but adds dose.

### Failure and learning
- Any meter at zero → the base lights go dark one by one, the visors frost, fade out: "Your crew ran out of air."
- Then the **replay**: a timeline of the 3 choices that caused it, shown as an "X → Y → Z" chain. Then Retry (same seed or a new one).
- A **Mission Log** collects fact cards across runs. This covers replayability and data credit.
- **Data credits screen:** every dataset and its date, marked "live" or "archived".

## Build architecture (vanilla three.js + Vite, HTML/CSS HUD; no React, since a plain DOM overlay covers the UI)
```
src/sim/      pure JS: state, rules, events, seeded rng   (no three.js; node --test)
src/data/     tuning.json, facts.json (with sources), events.json (archived DONKI/NOAA)
src/world/    world.json (pads, prefabs, camera presets), prefabs.js, scene.js, style.js, fx.js
src/ui/       hud, cards, replay, credits (HTML/CSS)
src/cine/     intro cinematic (camera path over the same assets)
forge/        Blender recipes → public/models/*.glb + previews/*.png
tools/        capture-view.mjs, balance bots
```
- **The sim is the single source of truth.** Balance bots run 1,000 seeded games, with asserts:
  - "do nothing" loses;
  - "all science" usually loses;
  - "balanced" usually wins;
  - no option is free. That last check is the brief's rule, enforced by a test.
- **3D world: "assemble, don't model".** Order of preference:
  1. Real NASA data: the terrain mesh from the Gale STL, the textures, the NASA GLBs.
  2. A CC0 kit.
  3. three.js built-ins: Sky, environment, ContactShadows, instancing, particles.
  4. Procedural code for effects only. A dust storm is 3 numbers: fog, sun intensity, particle count.
  5. **Asset forge** for gaps (oxygen maker, ice drill, greenhouse dome, shelter, lander).
- **The scene is data.** Agents edit `world.json`, not scene code. Every GLB passes through one `applyHouseStyle()`, so mixed kits look like one game. Every asset passes through one `gltf-transform optimize … --compress meshopt --texture-compress webp`.
- **Asset forge:**
  - One recipe per asset, `forge/<asset>.py`, 40–80 lines of headless Blender Python.
  - Every recipe reuses `forge/lib.py`: palette materials, bevel, weighted normals, export, a 3-angle preview render.
  - The agent looks at the 3 PNGs, fixes the recipe, reruns it. No Blender MCP back-and-forth.
  - Each recipe is given 1–2 NASA reference photos.
  - If Blender is missing, fall back to three.js addons: RoundedBox, Lathe, Tube, Extrude, three-bvh-csg, merged geometry and instancing.
- **Budgets:**
  - Assets < 15 MB.
  - First playable frame < 3 s.
  - < 150 draw calls.
  - 60 fps on a school laptop.
  - Fully offline.
- **Agent loop (develop-web-game pattern):** deterministic `advanceTime(ms)`, `render_game_to_text()` for state checks (cheaper than screenshots), `capture-view` with 4 preset cameras at 0.5 scale, a console-error gate, a `progress.md` handoff.

## Hackathon runbook (one laptop; times are hours from the start)
- **H0–1:** I paste the design pack. I scaffold the repo and the contracts. `npm ci` runs from the cache.
- **H1–10:** five background agents in git worktrees, each given only its folder, the contracts and its skill:
  - (A) sim, tests and balance bots;
  - (B) scene, terrain and house style;
  - (C) forge assets;
  - (D) HUD, cards, replay and credits (design-taste skill);
  - (E) cinematic and audio.
  - I merge at H4 and H8. Each lane ends with its screenshot or text check passing.
- **H10–14:** the first full playable loop. Teammates playtest, and I tune `tuning.json` only.
- **Day 2:**
  - Polish: animation, sound, accessibility checks, perf budget, offline test.
  - The data credits page and the SI-use write-up.
  - Deploy to GitHub Pages.
  - A 30 s demo video with English subtitles, and ≤ 7 slides.
  - Submit by 18:00. The hard deadline is 23:59 local.

## Team lanes (the 3 friends do human work, since agents write the code)
1. **Ravindu, Commander:** drives Claude, approves merges.
2. **Science officer:** checks the fact cards and the data credits, and writes the SI-use text.
3. **Story & sound:** writes the voice lines, checks the wording is right for kids, playtests with real kids. Note the rule that under-18s' faces and voices can't appear in the submission.
4. **Pitch lead:** demo video, slides, project page, rehearsing the demo. Also reviews screenshots against `DESIGN.md`.

## Verification
- **Docmost:**
  - `dm.tree()` and `dm.nodeTypes()`, plus one screenshot per page type.
  - Grep for em dashes and banned words in the markdown before posting.
  - A fact-check table with every claim's status.
- **Tooling (Phase B):** `blender -b --version`. The crate recipe produces a GLB plus 3 PNGs. `capture-view` screenshots a blank three.js scene.
- **Rehearsal (Phase C):** sim tests and bots pass; screenshots match the art brief; fps measured; a timing and token log written up in the retro.
- **Real game (Nov 14–15):**
  - `node --test` (sim + bots).
  - `capture-view` at 4 cameras.
  - `renderer.info` draw calls under budget.
  - Works with the network unplugged.
  - Every on-screen number traced to `facts.json` and its source.
