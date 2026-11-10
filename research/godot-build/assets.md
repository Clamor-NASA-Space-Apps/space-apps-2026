# Assets: what we have, what is missing, what is safe 🧰

Checked 10 November 2026. "On disk" means `assets-cache/` in this workspace. Saved licence pages are under `pages/agent-3/`.

> [!TIP]
> **TL;DR.** Kits, rovers and habitat parts are on disk. The astronaut is the gap: nothing on disk is a suited human with walk and run animations. One CC0 model fits, and nobody has opened the file yet. Five of six NASA models must be re-saved before Godot can read them.

---

## 1. What is on disk 💾

| Asset | What it is | Rig and clips | Use |
|---|---|---|---|
| NASA Perseverance | 199,521 triangles, 5 MB | a 15-joint rig and 23 mechanical clips, no drive cycle | hero prop after cutting triangles down |
| NASA Ingenuity | 9,124 triangles, 2 MB | none | prop |
| NASA astronaut | 6,381 triangles | **none: a statue** | scale reference only |
| NASA Habitat Demo Unit (2 parts) | 2,264 and 4,320 triangles | none | habitat |
| Curiosity landing-site mesh (STL) | real Gale terrain, 2.8 MB | | small ground patch |
| Kenney Space Kit | 153 models, 2 to 876 triangles each | none. The two astronauts are rigid pieces with no skeleton | domes, corridors, tanks, dishes, rocket parts, rocks |
| Kenney Space Station Kit | 97 models | none | interiors |
| Kenney Mini Characters | 20 people, 686 to 947 triangles | **7-bone skeleton, 32 clips**: idle, walk, sprint, jump, fall, crouch, sit, drive, pick-up, interact | fallback hero. No astronaut among them |
| Kenney Blocky Characters | 18 people, 72 triangles | clips move rigid parts, no jump | not for the hero |
| Kenney sound packs | interface and sci-fi sounds | | buttons, alarms |

We loaded a Mini Character in Godot 4.7.2 on 10 November 2026: 7 bones and 32 clips arrived intact.

> [!WARNING]
> Godot 4.7 cannot read GLB files whose meshes are compressed with Draco, meshopt or quantization. The NASA astronaut, habitat units, Ingenuity and Perseverance on disk are all Draco. Re-save each one with `gltf-transform optimize in.glb out.glb --compress false --texture-compress webp`. We tried it on a habitat unit: it then loaded, and shrank from 517 KB to 104 KB.

---

## 2. The astronaut 🧑‍🚀

The last prototype felt soulless mostly because its characters were animated from code. The rule now: a rigged model with clips made by an animator, blended by the engine.

| Candidate | Licence | Rigged, clips | Fits? |
|---|---|---|---|
| **Quaternius "Astronaut"** (Ultimate Modular Men Pack), [poly.pizza/m/3hC2i0CTuO](https://poly.pizza/m/3hC2i0CTuO) | CC0 on the pack page and on Poly Pizza | animated, 5,324 triangles; the pack has "24 animations" | a suited human with a closed helmet. **Clip names and file size are not on any page** |
| Quaternius Ultimate Space Kit astronauts | CC0 | animated | cartoon animal heads holding guns: wrong for a real-science game |
| Kenney Mini Characters (on disk) | CC0 | verified, 32 clips | right motion, wrong outfit. Needs a helmet and backpack attached to its bones |
| NASA Mark III suit, NASA astronaut | NASA media rules | not rigged (astronaut), unknown (suit) | no animation |
| Mixamo | Adobe's terms | yes | **no**: see below |

**Do before 14 November 2026:** download the Quaternius astronaut, list its clips, and check for walk, run, idle and a jump. Keep the licence file from the zip.

---

## 3. Licence traps ⚠️

1. **Quaternius.** Every pack page says CC0, and the FAQ says "All models are under the CC0 License." But the site now also carries a "Quaternius Asset License (QAL) v1.0", dated 28 August 2026, which forbids redistributing the assets as assets. Our repo is public, so we keep the saved pack page and the zip's own licence file as proof of CC0 for the pack we use.
2. **Mixamo.** Fine inside a game. The Adobe community FAQ lists "Any type of free distribution of character or animation raw files" as not allowed. A public repo with the model files in it is that. Do not use it.
3. **GDQuest's third-person demo.** The code is MIT. The art changed to CC-BY-NC-SA 4.0 on 16 May 2026: non-commercial and share-alike. Take ideas from the code, never the robot.
4. **NASA models.** NASA content "generally [is] not subject to copyright in the United States" and may be used "in a factual manner that does not imply endorsement". The insignia, logotype and identifiers "are not in the public domain". Some models come from outside contributors (the astronaut is credited to DigitalSpace Corporation), so copy the credit from each model's page.
5. **Solar System Scope textures** are CC-BY 4.0: credit required.
6. **Repos with no licence** (Discover Mars, MarsLanding, the kasei entry): all rights reserved. Read, do not copy.

---

## 4. Still to download 📥

| Need | Candidate | Licence | Size |
|---|---|---|---|
| Solar panels | Quaternius Ultimate Space Kit: Solar Panel (812 triangles), Solar Panel Ground, Solar Panel Structure | CC0 | not stated |
| Greenhouse shell | same kit: Geodesic Dome (1,432 triangles) | CC0 | not stated |
| Ground texture | Poly Haven `terrain_red_01` or `red_sand`, 1k | CC0 | 1.7 or 2.3 MB for three maps |
| Rocks | Poly Haven `moon_rock_02` (6,194 polygons), 1k | CC0 | 1.5 MB |
| Real Gale elevation | USGS copy of HiRISE product `DTEEC_023957_1755_024023_1755_U01`, 1.01 m per pixel | CC0 | 171 MB as a cloud-optimized GeoTIFF: crop a few km and shrink it |
| Wind and driving sound | NASA "Sounds of Mars": Perseverance driving, sol 16 | credit NASA/JPL-Caltech | 2.6 MB as MP3: cut a few seconds |
| Crops | Quaternius Ultimate Crops Pack, 5 growth stages | CC0 | no glTF: needs Blender conversion |

The rule from `AGENTS.md` still holds: download before the event, and add every asset to `assets-cache/CREDITS.md` with its credit line.

## Open questions ❓
- The Quaternius astronaut's real clip list and size.
- Whether a helmeted Kenney Mini Character reads as an astronaut to a kid.
- How small Perseverance gets while still looking like Perseverance.
