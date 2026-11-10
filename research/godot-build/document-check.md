# The unverified document, claim by claim 🔍

The document is "Building a Gale Crater Mars Survival Game in Godot 4: Reference Games, Addons, Assets and Real Science" (in Ravindu's Downloads folder, checked 10 November 2026). Each claim was compared with the source itself, with our own fact-check table, and with what the installed Godot skills and the engine say.

Status: ✅ right, ⚠️ partly right or out of date, ❌ wrong or unsupported.

> [!WARNING]
> Do not follow its "quick-start list" as written. Four of its ten steps point at things that are mis-licensed, built for the wrong renderer, or unable to run in a web build.

---

## 1. Its advice against ours ⚖️

| The document says | Verdict | What to do |
|---|---|---|
| Use Godot 4.6 or 4.7, standard build, GDScript only, Compatibility renderer from day 1 | ✅ | Same as our setup |
| Keep the default Godot Physics; Jolt is "experimental" | ❌ out of date | That wording is from the 4.4 docs. Jolt lost the label in 4.6 and is the default for new projects. Our skill pack agrees. Use Jolt |
| Fork the player from GDQuest's controller or the official TPS demo | ❌ | Both are Forward+ projects with no touch controls. GDQuest's art is now non-commercial. The TPS demo's art is CC-BY 3.0 and it turns on effects a web build lacks |
| Use the solodeveloping controller for "touchscreen support" | ⚠️ | Its touch controls switch on only when the system is Android or iOS. A phone browser reports "Web", so they stay hidden |
| Phantom Camera for the third-person camera | ⚠️ | MIT, GDScript, version 0.11.0.4, needs Godot 4.4 or later (not 4.3). Usable, but Godot's own `SpringArm3D` does the same job with no addon |
| Rover from the Truck Town demo | ✅ | Official, MIT, Godot 4.7, has touch steering. It is a Forward+ project, so take the vehicle, not the settings |
| ogeeice/Vehicle as "a minimal VehicleBody3D controller" | ❌ | It is a Godot 3 project, untouched since 2023 |
| Terrain3D for the terrain on desktop, HeightMapShape3D for web | ⚠️ | Terrain3D is a native C++ addon and its own docs call web exports "very experimental". For us: a generated heightmap mesh. HTerrain is pure GDScript but untested on web |
| Mars HAWC as the guide for turning HiRISE data into terrain | ⚠️ | Its code is MIT and its method is sound (16-bit PNG heightmap, mesh built in code). But its terrain is Candor Chasma, not Gale, its script points at the author's own disk, and one of its models comes from a non-commercial generator |
| MarsLanding "shows that a Godot 4.7 web export works for this audience" | ⚠️ | It has a live web build, but it is a 2D game with no licence. It proves nothing about 3D |
| Dialogic 2 for dialogue | ⚠️ | Correct facts (MIT, Godot 4.5+, alpha). For a two-day build a text panel is less risk than an alpha addon |
| Red-tinted PhysicalSkyMaterial for the Mars sky | ✅ | The docs say a red Rayleigh colour gives "a Mars-looking atmosphere with a corresponding blue sunset", and add that it is not physically accurate |
| "GPUParticles3D falls back to CPUParticles on Compatibility/web" | ❌ | No such fallback. GPU particles run on the GPU there. Trails and sub-emitters are what is missing |
| SDFGI and volumetric fog disappear in Compatibility | ✅ | |
| C# cannot be exported to the web | ✅ | |
| NASA models are usable, without logos or implied endorsement | ✅ | Quotes match NASA's page |
| Curiosity model credit "NASA VTAD" | ❌ | The page says "NASA/JPL-Caltech" |
| Kenney Space Kit has "Astronaut A/B" | ⚠️ | True, but they have no skeleton and no animation. The document does not say so |
| Kenney, Poly Haven, Quaternius are CC0 | ⚠️ | Kenney and Poly Haven yes. Quaternius has a new site licence that conflicts with its CC0 pages: see [assets.md](assets.md) |
| HiRISE elevation product for Gale: 458 MB, 1.01 m per pixel | ✅ | And USGS has a 171 MB cloud-optimized copy that can be cropped remotely |

What the document missed: the official "Platformer 3D" demo (MIT, Godot 4.7, third-person player, follow camera, touch joystick, hosted web build), and the `VirtualJoystick` node built into Godot 4.7.

---

## 2. Its science against our fact-check 🔬

Our table is [factcheck.md](../junior-astronaut/factcheck.md). Where the two disagree, ours is newer or closer to the source.

| The document says | Verdict | Our value |
|---|---|---|
| Gravity 3.71 m/s² | ⚠️ | 3.73 mean on NASA's fact sheet (row 7). 3.71 is not on it |
| Walk-to-run numbers, jump table | ⚠️ | The arithmetic is right. The suited value was measured on the Moon only, so the Mars cell is an estimate |
| The Pavei 2015 quote about skipping | ❌ not confirmed | Paywalled. The model it summarises is confirmed: walking at 1.1 m/s, running or skipping at 2.0 m/s |
| Kicked-up dust falls back in arcs | ❌ | Fine dust "became diffuse within seconds" and drifted |
| Oxygen 0.84 kg per person per day | ✅ | row 23 |
| CO₂ 1.00 kg per person per day | ❌ | 1.085 (row 24, the 2022 NASA baseline). The document used the 2004 edition |
| Water 3.5 kg per person per day | ❌ | 3.217 (row 25) |
| Food 0.62 kg dry per person per day | ❌ | 2.39 kg packed (row 112). Different basis and an older figure |
| 4 crew, 30 sols: 75 kg food, 430 kg water | ❌ | 295 kg packed food, 397 kg water |
| MOXIE: 122 g in total, 12 g per hour, 98% pure | ✅ | rows 27 and 28 |
| Gale temperatures: about 0 °C to −70 °C | ⚠️ | A 2012 snapshot. Ours is +15.9 °C to −100 °C over two Mars years (row 10) |
| 2018 storm at Gale: opacity about 8.5 | ✅ | |
| Same storm: ultraviolet down 90% | ❌ | NASA's report says 97% |
| InSight: 5,000 down to 500 watt-hours per sol | ✅ | new to our table |
| Perchlorate 0.4 to 0.6% | ⚠️ | True at the Phoenix landing site. NASA's later review says 0.5 to 1% (row 140) |
| Radiation on the surface 0.64 mSv per day | ⚠️ | The paper says 0.64 ± 0.12, the press release 0.67 (row 32). Same instrument. Read as an excerpt only |
| Mount Sharp 5.5 km | ⚠️ | NASA says about 5 km. The 5.5 comes from Wikipedia |

Hard rule 3 of this workspace still applies: a number reaches players only from `factcheck.md`. Nothing in the unverified document goes into the game directly.

## Not checked
Its entries for OpenPlanetSurvival, Open Target Shooter, Sunder, OpenLiberty, the Surviving Mars source, Simple Grass Textured, the Bruneton sky addon and the Spirit rover power figures.
