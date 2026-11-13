# AGENTS.md: NASA Space Apps 2026 workspace

`CLAUDE.md` holds one line, `@AGENTS.md`, which loads this file (a real file, not a symlink, so it works on Windows). Claude Code also loads it in every sub-folder, including the nested repos, so the rules here apply everywhere. Nested repos add only their own specifics.

## Mission
- **Team:** 4 beginners (Ravindu = Commander, drives Claude), NASA Space Apps 2026, Colombo local event, **14–15 Nov 2026**.
- **Challenge:** "Build a Junior Astronaut Mission Trainer". Kids aged 7–12 run a Moon/Mars outpost and learn real trade-offs: life support, radiation shielding, power, food, communication delay.
  - Full text: `research/junior-astronaut/challenge.txt`.
  - Author video transcript: `research/junior-astronaut/video-subtitles.txt`.
- **Our answer:** a **Godot game exported to the web, "Outpost Gale"** (working title). A base in Gale crater on Mars, 30 sols, 3 meters, PG "mission lost" + replay of the 3 choices that caused it.
  - **Engine and view changed on 10 Nov 2026:** Godot 4.7 in place of three.js, third person, a real-looking Mars, playable on a mid-range phone or a computer. What that needs and allows: `research/godot-build/README.md`. Its section 5 lists the decisions still open.
  - Full design: Docmost page "Game design and story".
- **Plan:** `plan.md`. **Checklist:** `roadmap.md`. Tick roadmap items when done.

## Hard rules (breaking these can disqualify us or mislead kids)
1. **Everything may be prepared before 14 Nov, the story included; at the event we wire the flow, playtest and submit.** 2026 FAQ: "Teams are not allowed to begin working on the challenges prior to the hackathon." The local organisers then told the team, in meetings reported by Ravindu, that assets may be prepared in advance (12 Nov 2026) and that preparing the game at home is allowed (13 Nov 2026).
   - Before 14 Nov: research, docs, tooling, the look, every model, the world and map, the HUD, the sandbox, and the game's systems: `sim/` rules (O2, power, water, food, radiation), meters, the sol clock, PIP's guiding, use spots, the machinery for cinematics and tutorials. Systems are tested on their own, with placeholder values where the story will decide.
   - The story is drafted before the event too (Ravindu, 13 Nov 2026: a crowded venue would cost us the plot, and the local organisers said preparing is fine): `design/story.md` in the game repo, read and changed by the team, fact-checked. At the event: wire the story into the flow (beats order, win and lose), playtest, polish, submit.
   - Both permissions were verbal, and the global FAQ above says otherwise. Ask the Colombo Local Lead to confirm in writing and save the reply in `research/junior-astronaut/`. Tag each repo when the event starts, so judges can see what came before.
2. **Never copy anything from `tooling/projects/one-night-stray/` into the hackathon repo.** Only `tooling/` (agent-forge-3d) is shared.
3. **Every number shown to players has a source** in `research/junior-astronaut/factcheck.md`. ❌ claims never ship.
4. **Never present archived data as live.** Every data value is labelled LIVE (fetched now) or ARCHIVED + date.
5. **No NASA logos** (meatball, worm, seal), and nothing that implies NASA endorsement. Text credit "Data: NASA" is fine.
6. **AI ("SI") use must be described** in the submission. AI images/videos need a visible "AI-generated" watermark. AI audio (Piper voices) and code are acknowledged in text.
7. **Cite every source and asset.** Keep `assets-cache/CREDITS.md` current. Original work is open source (Apache-2.0).
8. **Under-18s:** no photos, video or voices of minors in the project or the demo.
9. **Secrets:** the api.nasa.gov key lives only in `.env.local` (gitignored, chmod 600).
   - Never print it.
   - Never commit it.
   - Never ship it in browser JS.
   - Live in-game data comes from NOAA (no key).
10. **Offline first.** The venue network may be slow. The game must run with the network unplugged. Download before the event, never during.

## Judging (2026 guides, checked 13 Nov: `research/junior-astronaut/judging-2026.md`)
- **Criteria:** Impact, Creativity, Validity, Relevance, Presentation, each scored 1 to 5.
- **Submit** (opens Sat 14 Nov 09:00): project page, a 30 s video with English subtitles (or ≤7 slides), a public no-login game link, sources, and the SI-use paragraph. Page images: JPG, PNG or GIF up to 10 MB; host videos elsewhere.
- **SI (2026):** never used "to come up with your idea of how to solve the challenge" (the idea is the team's). SI audio, code and data are acknowledged in text **and** metadata; SI images and video carry a visible watermark. No NASA branding, logos, flags or mission identifiers in generated content.
- **Eligibility:** at least one NASA data source or resource (Global Awards). Every resource, CC0 and open source included, goes in References with its licence. Our own work is OSI open source (else NASA applies Apache 2.0).
- **Path:** local judges pick Global Nominees (3 Dec 2026), then Finalists (17 Dec), Global Awards (26 Jan 2027). Ask the Colombo Local Lead for the local schedule.
- **Deadline:** Sun 15 Nov 23:59 local. Our target is 18:00.
- **What the brief rewards:**
  - No free choice: every option costs something.
  - 2–3 core resources.
  - Plain language, with terms explained in context.
  - Real data credited in-game.
  - Replayability.
  - Real space weather tied to choices.

## Verified facts (✅ = seen in the source; full table and URLs in `research/junior-astronaut/factcheck.md`)
| Fact | Value | Source |
|---|---|---|
| Trip Earth→Mars | 203 d (Perseverance) to 253 d (Curiosity), about 7 months, **not 9**. It does **not** pass the Moon or the ISS | NASA, SwRI |
| Launch windows | every 779.94 d (~26 months) | NSSDC |
| Sol / Mars year | 24 h 39 min / 687 Earth d = 669.6 sols | NSSDC, NASA |
| Gravity | Mars 0.38 g; Moon 0.166 g | NSSDC |
| Air pressure | 6.36 mb (Earth 1013); ±25% seasonal at Gale | NSSDC, JPL |
| Gale air temp | +15.9 °C to −100 °C | JPL (REMS) |
| Sunlight | 586.2 W/m², 43% of Earth's | NSSDC |
| Radio delay | 3–22 min one way; NASA: "up to 20 minutes"; conjunction blackout about 2 weeks | NSSDC, NASA |
| Opportunity | storm spotted 30 May 2018, tau 10.8, last signal 10 Jun 2018, >1,000 recovery commands, ended 13 Feb 2019 | JPL |
| InSight | last contact 15 Dec 2022, dusty panels, "dead bus" | NASA |
| MMRTG | ~110 W electric, ~2,000 W heat, 4.8 kg PuO₂ | NASA |
| Fission Surface Power | up to 10 kW for ≥10 years | NASA |
| O₂ per person | 0.84 kg/d (0.895 long-mission); CO₂ out 1.085 kg/d; water 3.217 kg/d | NASA BVAD 2022 |
| ISS water recycling | 98% (2023) | NASA |
| MOXIE | 122 g total, 16 runs, best 12 g/h, ≥98% pure | JPL |
| MOXIE power | 300 W (≈3× the MMRTG), ~1 h runs, only ~10% of power made O₂; full-size 2–3 kg/h needs 25 kW | NASA instruments page, PI blog |
| Habitat power | ISS oxygen maker 3.6–4 kW, CO₂ scrubber ~1 kW (⚠️), all ECLSS 5.31 kW; Mars habitat ~12 kW; "ISRU is the Biggest Power Draw" (~25 kW). Water recycler power ❌ not found | NASA ICES, BVAD, DRA 5.0 |
| Plants for air | 20–25 m² of crops per person's O₂, 40–50 m² for food; lettuce 7.78 g O₂/m²·d. A small greenhouse = food and morale, not air | Wheeler (NASA KSC), BVAD |
| Shielding | thin soil barely helps (dose peaks ~30 cm down), ~1–1.6 m for <100 mSv/yr; hydrogen-rich water/polyethylene beat aluminium; 5.3 cm water halves a deep-space storm dose | NASA TP 1991/2013, Zhang 2022, Walker 2013 |
| Science goal at Gale | was Mars ever able to support microbial life; ancient lake "held all the ingredients necessary for life"; organics "not necessarily indicators of life" (never say life was found) | NASA Curiosity, release 18-050 |
| Veggie lettuce | 33 d harvest (64 d cut-and-come-again) | NASA NTRS |
| **NASA's first Mars stay** | ≥2 crew, **30 sols**, O₂ and pressure from tanked gas, all water brought as a consumable and not recycled (2023). Our 30-sol game matches a real NASA plan | ICES-2023-265 |
| Where O₂ really comes from | ISS: splitting water (≈1.1 kg water per kg O₂), 5.4 kg/day for 4 crew; tanks as backup (~36 kg O₂ each). MOXIE flat out ≈ 1/12 of 4 crew's need, it was a demo | NASA fact sheet 2025, ICES |
| Water per person | 3.2 kg/day = drink 2 + food 0.5 + exercise sweat 0.7; early Mars base 4.5 kg/day with a shower; out: breath+sweat 2.9, urine 1.4. ISS loop 98% with the Brine Processor (since Mar 2021) | BVAD, ICES-2026-425 |
| Food per person | ~3,000 kcal, 2.39 kg packed/day; ISS food lasts 1.5–2 yr, Mars needs 5 (still a gap); vitamin C gone in ~1 yr; plants = "pick and eat" supplement (<1% of energy); microgreens 7–18 d, radish 25 d | BVAD, HRP, NASA TM 2025 |
| 4 crew × 30 sols | ≈ 397 kg water, 295 kg packed food, 104 kg O₂ (no recycling) | our maths from BVAD |
| Pressure / suits / dust | below 47 mmHg body water boils (Mars ~5 mmHg); suit 30 kPa pure O₂, 6.5–8 h; habitat air 57 kPa 34% O₂ (proposed); Mars dust 0.5–1% perchlorate, "likely toxic" | NASA JSC, EVA chapter, BVAD, HRP |
| Radiation | cruise 1.8 mSv/d; Gale surface 0.67 mSv/d; 1 Sv ≈ +5% fatal cancer risk | SwRI (RAD) |
| Solar storm at Mars | 20 May 2024, X12: 8,100 µGy at Curiosity = "30 chest X-rays", not deadly | JPL |
| Storm shelter | built "within an hour" of a warning, stay up to 24 h, from bags of food and water | NASA (Orion) |
| Dust storms | global about every 3 Mars years (~5.5 Earth years); dust settles over months | NASA |
| Landing | "seven minutes of terror" | NASA |
| Gale sunset | looks blue near the Sun | NASA |
| Moon dose 1,369 µSv/d; Earth background 2.4 mSv/yr | ⚠️ reported only | press / research agent |

## Start a build
Open `claude` in `tooling/` (or in a project under `tooling/projects/`) and say what to build. The factory workflow in `tooling/AGENTS.md` takes it from there: questions, plan mode, `roadmap.md`, sections in bulk, check + `/code-review medium` + lessons per section. Projects live in `tooling/projects/<name>/` (gitignored there, each its own repo). This file's facts and research paths still apply, because Claude Code loads it from every folder below.

## Where things are
| Path | Contents |
|---|---|
| `research/junior-astronaut/` | `pages/` (saved sources), `sources.md`, `factcheck.md` (rows 1–143), `browser-excerpts.md`, `charts/` (chart HTML → PNG via `tooling/tools/html-to-png.mjs`), `images/` |
| `research/godot-build/` | The Godot build (10 Nov): what the web renderer can and cannot draw, assets and licences, real movement numbers and the look of Gale, the check of the unverified asset document, `references.md` (fact-check), `pages/` (saved sources) |
| `assets-cache/nasa-3d/` | Perseverance, Ingenuity, Astronaut (a statue: no rig), Base Station, Habitat Demo Unit GLBs; Curiosity landing-site STL (real Gale terrain); Mars/Moon/Earth textures. **Five of the six GLBs are Draco-compressed, which Godot cannot read:** re-save with `gltf-transform optimize in.glb out.glb --compress false --texture-compress webp` |
| `assets-cache/kenney/` | Space Kit (153 GLB: domes, corridors, generators, dishes, rover, rocket parts, platforms, rocks; **no solar panels**), Space Station Kit, Mini Characters (rigged, 32 clips: the fallback hero), Sci-fi + Interface sounds. All CC0. **No animated astronaut on disk** (candidate in `research/godot-build/assets.md`) |
| `assets-cache/data-snapshots/` | NOAA flares + Kp, Curiosity weather (4,745 sols). DONKI still down on 8 Nov (503 upstream timeout, even with our key); retry |
| `assets-cache/CREDITS.md` | Every asset's source, licence and credit line |
| `tooling/` | Separate repo **agent-forge-3d**, the game factory: workflow and code rules in its `AGENTS.md`, Blender forge, the Godot test hooks (capture-view, feel-probe, web-check), html-to-png. Will be public. **The Godot factory is on its `godot` branch**; `main` is the three.js one |
| `tooling/projects/one-night-stray/` | Separate repo: the three.js rehearsal game (a stray cat survives one night; brief in `STORY.md`). Throwaway |
| `tooling/projects/junior-astronaut-mission-trainer/` | The hackathon game, Outpost Gale. Separate repo. Look and assets from 12 Nov (`design/BRIEF.md`), the game from 14 Nov |

**Remotes** (Gitea, SSH works): `git@100.108.184.127:ravindu644/{nasa-space-apps-2026,agent-forge-3d,one-night-stray}.git`. GitHub mirrors come later. Ravindu decides when, because his GitHub is widely watched.

## Machine and tools (one laptop runs everything)
| Tool | Where / notes |
|---|---|
| Blender 5.2.2 LTS | `/usr/bin/blender`. Headless: `blender -b -P recipe.py`. Fedora build logs an OCIO 2.5 vs 2.4.2 error, so previews use raw colour. Use Cycles CPU, not EEVEE |
| Browser | Brave `/usr/bin/brave-browser`. There's no Chrome binary. playwright-core uses `executablePath` + SwiftShader |
| Godot 4.7.2 | Standard build (not .NET) at `~/Documents/Godot/Godot_v4.7.2-stable_linux.x86_64`, on PATH as `godot` (link in `~/.local/bin`). Export templates for Web, Linux and Android are installed. Headless: `godot --headless --path <project>` |
| Node | 22. npm cache is warm: @gltf-transform/cli 4.5 (`npx --offline @gltf-transform/cli`), playwright-core 1.65, @fontsource-variable/{lexend,fredoka}, and the three.js set the rehearsal used |
| Piper TTS | `~/opt/piper/bin/piper -m ~/opt/piper/voices/en_US-kristin-medium.onnx -f out.wav`. `kristin` = public domain; `libritts_r` = CC BY 4.0. Never use `lessac`/`amy`/`hfc_female` (licences). ffmpeg → Opus ~14 KB/line |
| Godot skills | 12 `godot-*` plus camera-systems, input-systems, performance-optimization, game-ai, survival-crafting, game-jam, from gamedev-skills/awesome-gamedev-agent-skills (Apache-2.0, reviewed 10 Nov). Copied into `tooling/skills/` (branch `godot`), so sessions in the factory load them; also installed in `~/.claude/skills/`. Which to load for what: the Skills table in `tooling/AGENTS.md`. The 13 three.js skills stay installed for the rehearsal repo |
| Design skills | design-taste-frontend (HUD/UI), ponytail (keep code minimal) |

## Docmost (team docs, space slug `NASA`)
- Site: https://docmost.ravindu644.dpdns.org/s/NASA. The page tree mirrors the plan: Start here, Mars survival 101 (4 pages), Moon vs Mars?, Trade-off cards, NASA data, Game design and story, How we build it with AI, Judging checklist, References and fact-check, Research Plan.
- Method: `~/Documents/Prompts/docmost-via-chrome.md` + `~/Documents/Prompts/tools/docmost-browser.js`. Drive the logged-in tab via Claude in Chrome; `fetch('/api/...')` POST.
- **Gotchas:**
  - Navigating wipes `window.dm`, so paste the helpers again.
  - JS results that look like cookies or URLs get blocked.
  - Edit page text through JSON text-node replacement so hand edits survive.
  - `pages/move` takes a 5–12 char `position` key. Order is lexicographic.
  - **Never fetch from localhost inside the Docmost tab.** It froze Brave with a local-network prompt.
  - **Pictures:**
    - Find them with the NASA Images API (`images-api.nasa.gov`, CORS ok).
    - Download with curl and shrink with ffmpeg (≤1400 px) into `research/junior-astronaut/images/<page>/`.
    - Pass them to the tab with Claude in Chrome `file_upload` on a temporary `<input type=file>`.
    - Upload with `POST /api/files/upload` (FormData: `pageId` first, then `file`).
    - Insert `{type:'image', attrs:{src:'/api/files/<id>/<fileName>', alt, align:'center', attachmentId}}` plus an italic caption with the credit.
    - Log each one in `images/credits.md`.
    - Don't fetch NASA `~orig.jpg` in-page: it has no CORS header.
  - **Links, not page names:** whenever a page is mentioned, link it (`/s/NASA/p/<slugId>`).
  - **New facts go where the topic already lives, never in an appended "answers" section.** A term is explained on the page that owns it (MOXIE → Life support, machine power → Power), and other pages link to it. Each page ends with "Open questions ❓" holding only what is still unknown. Method: fetch the page JSON in the tab, splice nodes into the right section (bullet list, table row, callout), and push the whole page back with `format:'json', operation:'replace'`. Check the image count is unchanged.
  - **Inserting a section mid-page:** append the markdown, then move the new nodes in the JSON to the right index.
  - **Long loops in one `javascript_tool` call time out at 45 s.** The script keeps running; wait, then check the result.
  - **Open team decisions** live in "Decisions for the team" at the top of [Game design and story](https://docmost.ravindu644.dpdns.org/s/NASA/p/Zn6Pf5rXby). Read it before changing the game design.
- **Writing style for docs:**
  - A friend explaining things.
  - Numbered headings with one emoji.
  - At most one callout per section.
  - A TL;DR, plus "kid version" lines.
  - No em dashes.
  - Banned words: leverage, robust, seamless, comprehensive, streamline, ensure, utilize, delve, crucial, powerful, simply, just.
  - Absolute dates.

## Research method (for any new claim)
1. Save the source to `research/junior-astronaut/pages/`. JPL, Spaceflight Now and Kenney block curl, so read those in the browser and save excerpts. Never spoof user agents.
2. Confirm it with `python3 -I ~/Documents/Prompts/tools/kwic.py page.html "regex"`.
3. Mark it ✅ / ⚠️ / ❌ in `factcheck.md`, and add the source to `sources.md`. Use the source's wording ("recognised" ≠ "winner").

## Build approach (details in `plan.md`)
- **Stack:** Godot 4.7, GDScript only, the Compatibility renderer, a single-threaded web export. HUD in Control nodes, pure-GDScript sim in its own folder with headless tests. A web build has no other renderer and cannot run C#.
- **Assemble, don't model.** Use the first option that works:
  1. Real NASA data/models.
  2. Kenney CC0.
  3. Engine built-ins (nodes, sky, particles).
  4. Code for effects only.
  5. Forge recipe (Blender).
- **The scene is data** (`data/world.json`). One `Forge.HouseStyle.apply()` for all GLBs. One `gltf-transform optimize ... --compress false` per asset.
- **Test hooks:** `Forge.register(self)` with `render_game_to_text()`, `set_view(name)`, `place(pos, yaw_deg)`. Check with `tooling/tools/capture-view.mjs`, `feel-probe.mjs` and `web-check.mjs`.
- **Budgets:** no download cap (Ravindu, 12 Nov 2026: "don't shrink anything"; native builds (EXE, APK, Linux) ship too, and the web build shows a loading bar after the splash). The 13 Nov build was 61 MB of game data, 49 MB gzipped with the engine; `web-check --budget-mb 100` only catches accidents. First frame <3 s, <150 draw calls, 60 fps on a school laptop.
  - **Still open before 14 Nov:** the draw-call and fps numbers were set for three.js; re-decide them after one test on the Galaxy A16 (the weakest device). Size is decided (above).
- **Kid UX:** icons first, ≤8 words per card, every line also spoken, targets ≥48 px, colour never the only signal.
  - **Team decision needed before 14 Nov:** in the rehearsal (10 Nov) the spoken lines annoyed the player and were removed; the factory now treats narration as opt-in and shows danger on screen. Decide whether Outpost Gale keeps "every line also spoken" (a Settings switch, off by default?).

## Git
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Don't force-push. Fix forward.
