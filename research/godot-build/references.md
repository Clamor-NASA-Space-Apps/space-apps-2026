# References and fact-check 📚

All sources were fetched on 10 November 2026 and saved under `pages/`. Four research agents gathered them; every ✅ row below was then found again in the saved file, or measured, by the main session.

- ✅ **checked:** seen in the named source, or measured on our laptop.
- ⚠️ **reported:** seen only by a research agent, read as an excerpt, or our own arithmetic.
- ❌ **not confirmed:** left out of the other pages, listed here.

## 1. Measured on our laptop (Godot 4.7.2, 10 November 2026)

| Claim | Status | How |
|---|---|---|
| Empty web build: engine 38 MB, whole download 9.7 MB gzipped | ✅ | `tooling/tools/web-check.mjs` on a new project |
| Engine starts in about 0.65 s from a local server | ✅ | same tool, headless Brave |
| Jolt runs in the web build, same result as native (ball rests at 0.484 m) | ✅ | same project, console output |
| A web build refuses to start on plain http that is not localhost | ✅ | seen in the browser, "Secure Context" error |
| Godot cannot read Draco, meshopt or quantized GLBs; `--compress false` output loads | ✅ | loaded each variant headless |
| Five of the six NASA GLBs on disk are Draco | ✅ | read each file's extension list |
| A shadowed sun plus ambient is 2.2 times too bright in Compatibility | ✅ | rendered a grey plane and read the pixel |
| Kenney Mini Character loads with 7 bones and 32 clips | ✅ | loaded headless |
| NASA model triangle counts (Perseverance 199,521 and others) | ✅ | summed from each file |
| In a desktop browser `OS.has_feature("mobile")` is false | ✅ | console output. Not run on a phone |

## 2. Godot engine (official docs, branch 4.7, in `pages/agent-2/`)

| Claim | Status | File |
|---|---|---|
| Web builds use only the Compatibility renderer | ✅ | `exporting_for_web.rst` |
| C# projects cannot be exported to the web | ✅ | `exporting_for_web.rst` |
| Single-threaded export is the default and preferred | ✅ | `exporting_for_web.rst` |
| Native addons need their own web build and special headers | ✅ | `exporting_for_web.rst` |
| Engine compresses to about a quarter with gzip; itch.io and GitLab Pages do not compress | ✅ | `exporting_for_web.rst` |
| Safari has WebGL 2.0 issues other browsers lack | ✅ | `exporting_for_web.rst` |
| Feature table: no volumetric fog, no screen-space reflections, depth and height fog supported, 8 lights per mesh | ✅ | `renderers.rst` |
| Simplified ambient occlusion since 4.6 | ✅ | `environment_and_post_processing.rst` |
| No decals: use Sprite3D | ✅ | `using_decals.rst` |
| Automatic instancing is Forward+ only | ✅ | `optimizing_3d_performance.rst` |
| Occlusion culling is not in the web export templates | ✅ | `class_occluderinstance3d.rst` |
| Shadowed lights render in sRGB space in Compatibility | ✅ | `lights_and_shadows.rst` |
| Keep to a handful of shadowed lights | ✅ | `internal_rendering_architecture.rst` |
| Up to 2 reflection probes per mesh | ✅ | `reflection_probes.rst` |
| Jolt is the default for new projects; the experimental label was removed in 4.6 | ✅ | `using_jolt_physics.rst`, `release_4.6.html` |
| A project with no setting gets Godot Physics | ✅ | `class_projectsettings.rst` |
| HeightMapShape3D collides faster than a concave mesh | ✅ | `class_heightmapshape3d.rst` |
| `OS.has_feature("mobile")` is false for a web build on a phone | ✅ | `feature_tags.rst` |
| Web uses ETC2 textures on mobile; high-quality compression is off in Compatibility | ✅ | `importing_images.rst` |
| Mobile GPUs are typically limited to 4096 px textures | ✅ | `3d_rendering_limitations.rst` |
| Lightmap baking wants a dedicated GPU | ✅ | `using_lightmap_gi.rst` |
| Red Rayleigh colour gives a Mars-looking sky | ✅ | `class_physicalskymaterial.rst` |
| GPU particles run on the GPU in Compatibility; no sub-emitters | ⚠️ | engine source, read by the agent |
| Built-in `VirtualJoystick` node is new in 4.7 | ✅ node exists; ⚠️ "new in 4.7" | `pages/agent-1/godot-docs-virtualjoystick-4.7.rst` |
| No official draw-call or triangle budget exists | ⚠️ | agent searched, found none |

## 3. Reference projects and addons (`pages/agent-1/repos/`, commits in `HEADS.txt`)

| Claim | Status | File |
|---|---|---|
| GDQuest controller: art is CC-BY-NC-SA 4.0 | ✅ | `godot-4-3d-third-person-controller/LICENSE` |
| That licence changed on 16 May 2026 | ⚠️ | from the repo history, not saved |
| TPS demo: art CC-BY 3.0; project sets SDFGI | ✅ | `tps-demo/LICENSE.md`, `project.godot` |
| solodeveloping controller: touch only on Android or iOS | ✅ | `godot4-third-person-shooter/.../Controls.gd` |
| ogeeice/Vehicle is Godot 3 | ✅ | `Vehicle/Vahicles/Car.gd` |
| Discover Mars has no licence | ✅ | `Discover-Mars/README.md` |
| MarsLanding and kasei have no licence file | ✅ | no `LICENSE` in either |
| MarsLanding is 2D only | ⚠️ | agent counted scene nodes |
| Mars HAWC builds terrain from a PNG heightmap with a trimesh collider | ✅ | `gnome-hd-mars/godot/scripts/mars_terrain.gd` |
| Mars HAWC terrain is Candor Chasma; one model is from a non-commercial generator | ⚠️ | agent read `tools/` and `CREDITS.md` |
| Terrain3D: native addon, web "very experimental", current release supports 4.5 to 4.8 | ✅ | `Terrain3D/doc/docs/platforms.md`, `terrain3d-releases.html` |
| HTerrain is pure GDScript | ✅ | `godot_heightmap_plugin/README.md` |
| Phantom Camera 0.11.0.4, Godot 4.4+ | ✅ | `assetlib-pcam-1822.html`, `phantom-camera/README.md` |
| Dialogic 2 needs Godot 4.5+ | ✅ | `dialogic/README.md` |
| Platformer 3D demo: touch joystick, Forward+ | ✅ | `godot-demo-projects/3d/platformer/README.md` |
| Truck Town demo: touch steering | ✅ | `godot-demo-projects/3d/truck_town/README.md` |

## 4. Assets (`pages/agent-3/`)

| Claim | Status | File |
|---|---|---|
| NASA media: not subject to copyright in the US; insignia not public domain | ✅ | `nasa-media-guidelines.html` |
| Perseverance GLB 4.76 MB; Curiosity glTF 11.31 MB | ✅ | `nasa-3d-mars-2020-perseverance-rover.html`, `nasa-curiosity-3d.html` |
| NASA has Mark III suit, Viking Lander, Apollo Lunar Module GLBs | ✅ | `nasa-3d-*.html` |
| NASA astronaut model credited to DigitalSpace Corporation | ✅ | `nasa-3d-hub.html` |
| Quaternius Astronaut: CC0, animated, pack has 24 animations | ✅ | `pp-m-3hC2i0CTuO.html`, `q-ultimatemodularcharacters.html` |
| Its clip names | ❌ | not on any page |
| Quaternius site licence of 28 August 2026 forbids redistribution; FAQ says CC0 | ✅ | `q-license.html`, `q-faq.html` |
| Mixamo raw files may not be distributed | ✅ community FAQ; ⚠️ not an official Adobe terms page | `adobe-mixamo-licensing-faq.html` |
| Poly Haven is CC0; texture and rock sizes | ✅ licence; ⚠️ sizes | `polyhaven-license.html`, `ph-files-*.json` |
| Quaternius Solar Panel, 812 triangles, CC0 | ✅ | `pp-m-ah89Y79JdT.html` |
| Gale HiRISE product: 1.01 m per pixel; USGS cloud-optimized copy, 179,340,715 bytes, CC0 | ✅ | `hirise-dtm-gale.html`, `usgs-stac-gale-search.json`, `usgs-cog-head.txt` |
| NASA driving sound: credit NASA/JPL-Caltech, MP3 2.60 MB | ✅ | `nasa-sound-driving-sol16.html` |
| Solar System Scope textures are CC-BY 4.0 | ✅ | `sss-textures.html` |
| Kenney kit page details (versions, counts) | ⚠️ | Kenney blocks curl: excerpts only. The on-disk `License.txt` files say CC0 |

## 5. Science (`pages/agent-4/` and `../junior-astronaut/pages/`)

| Claim | Status | File |
|---|---|---|
| Mars gravity 3.73 m/s² | ✅ | `nssdc-marsfact.html` |
| Suited walk-to-run on the Moon: Froude 0.36 ± 0.11, 38 gait events | ✅ | `carr2009-pmc.txt` |
| Walk-to-run happens near the same Froude number in lower gravity | ✅ abstract only | `kram1997-epmc.json` |
| Model: walking at 1.1 m/s on Mars, running or skipping at 2.0 m/s | ✅ | `ackermann2012-pmc.html` |
| Apollo speeds: 3.6 km/h plausible average, above 5 km/h running, 2 to 3 steps to stop | ✅ | `alsj-a11-gaits.html` |
| Apollo 16 jump: 1.17 m/s, 0.42 m | ✅ | `alsj-a16-alsepoff.html` |
| Mark III suit "extremely limited on Mars"; 121 kg | ✅ | `ntrs-20080014853.txt` |
| Suit masses 89, 177 and 104 kg | ✅ | `agent-habitat/ntrs-20260003024-mars-plss.txt` |
| Walking range roughly 20 km | ✅ | `agent-power/dra5-sp-2009-566.txt` |
| Perseverance 152 m per hour; Curiosity 15 to 18 m per hour alone | ✅ | `nasa-m2020-rover-components.html`, `jpl-robotics-m2020-mobility.html` |
| Crewed rover concept about 10 km/h | ✅ | `sev-factsheet.txt` |
| Apollo 17 rover 35.9 km in 4 h 26 min | ✅ | `nssdc-apollo-lrv.html` |
| Dust from Ingenuity became diffuse within seconds | ✅ | `lemmon2022-pmc.txt` |
| Storm dust takes weeks or months to settle; UV down 97%; opacity 8.5 at Gale | ✅ | `storm2018.txt` |
| Day sky orange or reddish | ✅ | `spaceplace-blue-sky.html` |
| Storm haze six to eight times thicker; "cherry red"; rim 30 km away | ✅ | `nasa-storm-haze-2018.html` |
| Gale 154 km wide; Mount Sharp about 5 km; rim about 40 km from one viewpoint | ✅ | `nasa-pia15292-mount-sharp.html`, `nasa-pia22209-telephoto-vista.html` |
| Drilled rock was grey-green | ✅ | `nasa-first-drill-sample.html` |
| Normal dust opacity 0.3 to 0.7 | ✅ | `vasavada2022-pmc.txt` |
| CO₂ 1.085 kg per person per day | ✅ | `bvad.txt` |
| Phoenix perchlorate 0.4 to 0.6% | ✅ abstract | `hecht2009-pubmed.json` |
| Surface radiation 0.64 ± 0.12 mSv per day | ⚠️ excerpt | `hassler2014-sitc.excerpt.txt` |
| InSight 5,000 to 500 watt-hours per sol | ✅ | `nasa-insight-power-photojournal.html` |
| Mars walking speed 1.1 to 1.3 m/s; Mars jump 0.18 m; horizon 3.3 km | ⚠️ | our arithmetic from the rows above |
| The Pavei 2015 skipping quote | ❌ | paywalled |
| Dust falls back in ballistic arcs | ❌ | contradicted for fine dust |
| A measured suited walking speed in Mars gravity | ❌ | not found |

## 6. Could not reach
- Kenney's site, the Journal of Experimental Biology, the Journal of Applied Physiology and phys.org block plain curl. Excerpts or abstracts were used and marked.
- The Docmost design pages were not read for this write-up.
