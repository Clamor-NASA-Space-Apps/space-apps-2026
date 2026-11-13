# Outpost Gale: what a real 30-sol Mars stay puts on the ground that our scene does not have yet

Written 13 Nov 2026. Research only: no code, no models, no game rules. Compared against `tooling/projects/junior-astronaut-mission-trainer/data/world.json` as it stood on 13 Nov 2026 (habitat HAB 1, storm shelter, greenhouse, 6 solar wings, 3 battery banks, fission reactor, 3 m dish, one lander, pressurised rover and charger, PIP, cargo bags, 2 lamps, beacon, wind telltale, 2 build pads, Curiosity, Mont Mercou).

This builds on two earlier studies in the game repo and does not repeat them: `design/research/missing-assets.md` (12 Nov: interior, tanks, scrubber, food, panels, sizes of the landers and the MAV cabin) and `design/research/layout.md` (13 Nov: the 1 km rules for the reactor and landings, the cable plan). Read those for anything inside HAB 1.

**Marks:** ✅ seen in the saved source and checked with `kwic.py`; ⚠️ reported only, or our own maths or reading; ❌ looked for and not found.

**Sources** (all saved in `research/junior-astronaut/pages/base-gap/` unless marked `ws:`, which means `research/junior-astronaut/pages/`):

| Key | Document | File |
|---|---|---|
| SAC21 | Short-stay human Mars architecture, 2 crew, 30 sols (NTRS 20210026448, 2022) | `ntrs-20210026448-sac21.flow.txt` |
| MAV21 | Mars Ascent Vehicle for SAC21, 2 crew (NTRS 20210026439) | `ntrs-20210026439-sac21-mav.flow.txt`, mass table in `.layout.txt` |
| MAV19 | Mars Ascent Vehicle, 4 crew, ISRU oxygen (NTRS 20190001229) | `ntrs-20190001229-mav-2019.txt` |
| ADD-C | NASA Moon to Mars Architecture Definition Document, Revision C (ESDMD-001, NTRS 20250010956, 12 Dec 2025) | `ntrs-20250010956-add-revC.txt` |
| EZ16 | Bussey and Hoffman, "Human Mars Landing Site and Impacts on Mars Surface Operations" (NTRS 20160001040, 2016), the paper behind the Oct 2015 landing-site workshop | `ntrs-20160001040-landing-site-ops.txt` |
| LANDER16 | Human Mars lander and its keep-out zone (NTRS 20160004402) | `ntrs-20160004402-mars-lander.txt` |
| FSP25 | Fission Surface Power trades (NTRS 20250000841) | `ntrs-20250000841-fsp-trades.txt` |
| PP23 | Spry et al., COSPAR planetary protection for crewed Mars missions, final report (ICES-2023-361, NTRS 20230010481) | `ntrs-20230010481-cospar-pp-crew.txt` |
| ICES23 | Mars habitat life support for the first stay (ICES-2023-265, NTRS 20230002103) | `ws:agent-power/ntrs-20230002103.txt` |
| DRA5 | Mars Design Reference Architecture 5.0 (NASA/SP-2009-566) | `ws:agent-power/dra5-sp-2009-566.txt` |
| MRN | NASA Science, "Mars Relay Network" page | `science-nasa-gov-mars-relay-network.html` |
| MAVEN | NASA release 26-047, "NASA Says Farewell to MAVEN", 3 Jun 2026 | `nasa-maven-farewell.html` |
| PIA17936 | "Bright 'Evening Star' Seen from Mars is Earth" (Curiosity at Gale, sol 529, 31 Jan 2014) | `pds-pia17936.html` |
| PIA06340 | Phobos and Deimos seen from the surface (PDS photojournal) | `pia06340-pds.html` |
| MOONS | NASA Science, Mars moons facts | `nasa-science-mars-moons-facts.html` |

Tool note: `kwic.py` strips anything between `<` and `>`, and NTRS text files contain `<` signs (for example "<5 rem"), which hides whole pages. Check text files with `sed 's/</‹/g; s/>/›/g' file.txt | python3 -I kwic.py /dev/stdin "regex"`.

## 1. TL;DR 🧭

- **The ride home is missing.** Every real plan ends with a Mars Ascent Vehicle (MAV): a two-stage rocket standing on its own lander about 1 km from everything else, landed two years early and filled on the ground. Our scene has one generic lander and no rocket. Our story ends with "go home", so this is the top gap.
- **Science has nowhere to go.** The crew "collect samples" (SAC21), but we have no sample box, no sealed container, no cold store and no lab corner. NASA allows 100 kg for samples and stowage in the MAV (MAV21); DRA 5.0 says up to 250 kg.
- **Trash is a real job with real rules.** In SAC21 the crew fill an empty logistics can with trash and park it next to the lander "as its permanent disposal location". Planetary protection experts want double bagging, one disposal site, and a container built to last 50 years (PP23).
- **Weather and radiation need a station on the ground.** NASA wants climate and seismic stations that keep working after the crew leaves (DRA5), and the crew carry personal dosimeters (MAV21). This gives our live NOAA and archived Curiosity data a body in the world.
- **The sky can show home.** Curiosity photographed Earth from Gale as "the brightest point of light in the night sky", and a person could see Earth and the Moon as two "evening stars" (PIA17936). Phobos rises in the west (PIA06340).
- **⚠️ Crew size changed in NASA's newest plan.** Our 2-crew choice follows SAC21 (2022) and ICES-2023-265. NASA's Architecture Definition Document Revision C (Dec 2025) now targets "no fewer than four (4) crew to the surface", because "fewer than four crew would present unacceptable crew risk" (ADD-C, decision MD-05, 2025). The 30-sol minimum and fission power still match. The team should decide how the fact card says this (section 5).
- **ISRU stays out.** The current short-stay plan has no fuel or oxygen factory on Mars (SAC21: ISRU "ground-ruled out"; ICES23: "may not be available for initial Mars surface missions"). ADD-C lists Mars ISRU as an open technology gap. A fuel plant would make our base look like a later mission, so skip it as a model and use it as a fact card.

Kid version: "Your rocket home is already waiting on Mars, full of fuel. Before you climb in, you pack your rocks in sealed boxes, put your trash in a can that stays on Mars forever, and leave your dusty suit behind."

## 2. The gap table 📋

Priority: **must** = add before the demo, it carries a lesson or the story; **nice** = adds realism if time allows; **skip** = not in the real first stay, or no source.

### 2a. Getting home and landing

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| **Mars Ascent Vehicle (MAV) on its lander** | The ride to orbit for 2 crew and 100 kg of cargo; cabin "a vertical cylinder 2.3 m in diameter and 2.9 m tall"; lifts off at 36,827 kg, landed at 22,095 kg (MAV21 ✅ text and Table 4). Figure labels 4.5 m and 7.2 m (⚠️ we read them as width and height). It must work "5.5 years, with up to 4 years on the Mars surface" (MAV21 ✅) | No (one generic crew lander) | **must** | The trip home is a rocket that waited for you; leaving Mars takes a lot of fuel |
| MAV fuelled on the ground, not from Mars air | Lands "one opportunity before crew arrival" with full MMH tanks and part-full NTO tanks; the rest of the NTO comes from a second lander, carried by a robot "about 11 round trips"; "The crew will not be cleared to land on Mars until the full propellant compliment required for powered ascent is confirmed" (MAV21 ✅). Two crew need "more than 30 tons of propellant" to reach the parking orbit (ADD-C ✅). Our maths from Table 4: about 14.3 t of NTO moved on the surface ⚠️ | No | **must** (as a fact card and a full-tank gauge on the MAV) | You never land unless your way home is ready first |
| Cargo lander 1: propellant, reactor, robot | "MAV propellant, a 10 kWe FSP unit, and a robotic mobility system", landing within 1 km of the others (SAC21 ✅) | Partial (reactor stands alone) | nice | Everything came on a few landers; each carries at most 25 t |
| Crew lander with the pressurised rover | Carries "a pressurized rover, a docking adapter, and crew consumables"; lands "about one km from the other two landers" (SAC21 ✅) | Partial (our lander + rover are separate) | nice | The crew's home on wheels came down on its own lander |
| Propellant transfer robot | "A propellant transfer package ... carried by an autonomous rover" pumps NTO lander to lander (MAV21 ✅) | No (PIP is a small helper) | nice | Robots do the dangerous fuel work before people arrive |
| Inflatable crew tunnel, rover to MAV | On sol 28 the crew "deploy and dock with a pressurized tunnel" (SAC21 ✅); it gives "a protected environment to support planetary protection protocols" (MAV21 ✅). The crew "are not expected to live or operate out of the MAV cabin" (MAV21 ✅) | No | nice | You go home without stepping on Mars dust again |
| Keep-out ring and landing pad / berm | Landings "must occur outside of a predefined keep out zone, currently assumed to be 1 km from any surface asset" (LANDER16 ✅). Site plans mark a "primary lander zone" for MAVs and a debris circle (EZ16 ✅); landing pads, roads and berms are the top civil-engineering need (EZ16 ✅); ADD-C lists "launch/landing pads, walls" as construction targets (lunar first, ✅) | Partial (beacon by the lander; layout.md puts it 191 m out) | nice | Rocket exhaust throws rocks, so landers stay far from the base |
| Rover drives 1 km away before launch | On ascent day the empty rover drives "nominally about 1 km" away from the MAV (SAC21 ✅) | No | nice (a cutscene beat) | Same rule as landing: keep away from rocket blast |

### 2b. Power and making things on Mars

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| Fission reactor 1 km away, cable to base | NASA picked fission over solar at its 2024 review because it is "more robust to Martian environmental and atmospheric conditions", works "around the clock, and during global dust storms" (ADD-C, MD-07 ✅). Outpost "1 km away and connected via a 3 kVac power cable" (FSP25 ✅) | Yes (191 m, see layout.md) | have | Why the reactor is far away and the solar panels are not |
| ISRU plant (fuel or oxygen from Mars air) | Not in the first stay: "ISRU was ground-ruled out of this architecture" (SAC21 ✅). Older plans used it: DRA 5.0 agreed "atmospheric-based ISRU (O2) for Mars ascent" (DRA5 ✅); the 4-crew MAV needed "more than 30 kW for a production rate of about 50 kg/day" of oxygen (MAV19 ✅). Today "Without gap closure, Mars mission architectures will be confined to Earth-delivered resources" (ADD-C ✅) | No | **skip** as a model; fact card only | Making fuel from air is real science, but not ready yet |

### 2c. Going outside (EVA)

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| Suitports on the rover | The rover is the EVA base; the logistics can docks "onto a PR suit port" (SAC21 ✅) | Yes (on the rover) | have | Climb into the suit from inside, keep dust out |
| High-pressure O₂ refill for suits | Suits need recharging ">3000 psi"; tanks also "recharge the EVA suits" (ICES23 ✅) | Partial (gas bottles by the airlock) | nice (a refill hose on the bottles) | Every walk outside uses stored oxygen |
| EVA suits stay on Mars | "Extravehicular activity planetary suits would be left behind"; the crew board the MAV "wearing their clean launch/entry suits to mitigate dust transfer back to Earth" (SAC21 ✅) | No | **must** (story beat at the end, no new model) | Mars dust must not come back to Earth |
| Traverse cache | A 1,000 kg "Traverse Cache" of supplies placed along routes (DRA5 Table 5-1 ✅) | No | nice (a marked crate out on a route) | Explorers leave supplies ahead, like a hiking stash |
| Exploration limit | First mission range "perhaps a 20 km radius" because of "limited rescue options" (SAC21 ✅); the wider exploration zone is "approximately 100 kilometers" (EZ16 ✅) | No | nice (map edge sign or fact card) | You may not go further than you can walk back |

### 2d. Science

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| **Sealed sample containers and a return box** | Crew "collect samples" and on sol 28 to 29 transfer "returned samples and logistics" to the MAV (SAC21 ✅); MAV allows "100 kg ... to encompass scientific sample return and any stowage systems" (MAV21 ✅); samples go home "in sealed sample containers" (ADD-C ✅); DRA5: returned samples "could be as much as 250 kg" (✅) | No | **must** | Every rock has a weight cost on the rocket; samples are sealed so Earth stays safe |
| Science equipment cargo | "about two metric tons of science equipment" (SAC21 ✅) | No | nice (crates marked SCIENCE by the lander) | Science is a big part of the cargo |
| Cold sample store (freezer) | Samples "will call for storage at refrigerated, frozen, and cryogenic temperatures" (ADD-C ✅) | No | nice (a small freezer box in HAB 1 or the rover) | Some samples spoil if they warm up, like food |
| Sample lab and glovebox | DRA5: samples go "to the primary habitat and its on-board laboratory"; "Facilities for handling collected samples under appropriate contamination control would be required to protect science, astronauts, and the Earth" (✅). PP23: "pass-through glove box technology with hydrogen peroxide" for cleaning tools (✅, still a study item) | No | nice | Gloves through a sealed box keep you and the rock apart |
| Drill on a trailer | Subsurface samples for "a stratigraphic record of sediments or layered rocks"; drill "on a trailer that is pulled by either the unpressurized or robotic rovers"; 1,000 kg in Table 5-1 (DRA5 ✅) | No | nice (Gale's layered rocks are why we came) | The deeper layers are older pages of Mars's history |
| Pristine sample rules | Samples from "uncharacterized sites or Special Regions" are treated as "restricted Earth return" (PP23 ✅); crew quarantine capability "shall be provided" (PP23 ✅) | No | nice (fact card) | Scientists keep Mars and Earth from swapping germs, both ways |

### 2e. Talking to Earth

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| Relay through orbiters | The Mars Relay Network is "an international constellation of four spacecraft"; rovers send data to orbiters "at data rates up to 2 Mbps" (MRN ✅). Today's four on that page: Mars Odyssey, Mars Express, MRO, ExoMars TGO (MRN ✅). MAVEN, once part of it, was declared lost on 3 Jun 2026, last heard 6 Dec 2025 (MAVEN ✅) | No (only the 3 m direct-to-Earth dish) | **must** (as a fact card and a small relay antenna on HAB 1 or the rover) | Your messages hop through a spacecraft overhead |
| No line of sight to Earth half the day | Rovers "lack line-of-sight to the Earth for about 12 hours per day due to Mars' planetary rotation" (MRN ✅) | No | **must** (it explains why the dish can't always talk) | Earth sets, like the Sun does |
| Crew in orbit as the relay | The two crew left in orbit serve "as a communications relay back to Earth" and give "low-latency" help (SAC21 ✅); the MAV assumes "a constellation of low Mars orbit relays" (MAV21 ✅) | No | nice (a voice on the radio, no model) | Friends in orbit answer fast; Earth answers slowly |
| Local network mast | For users near the habitat, "a Mars communications terminal on the surface would provide even more efficient wired and wireless" links (DRA5 ✅) | No | nice | Short hops are easy, long hops are hard |

### 2f. Weather, radiation, waste, spares

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| **Weather station** | "network stations for seismic monitoring and long-duration climate monitoring" that keep running "after the astronauts leave" (DRA5 ✅). Planetary protection wants "Few 10s of Kgs high fidelity instrument suite" measuring wind, humidity, dust and UV (PP23 ✅) | Partial (wind telltale) | **must** (a mast with sensors; it is where our weather data "comes from") | Real numbers come from real sensors |
| **Personal dosimeters** | MAV safety gear includes "personal radiation dosimeters" (MAV21 ✅) | No | **must** (a badge on the suit, cheap) | Radiation is invisible; you need a meter to see it |
| Seismometer | Same DRA5 line ✅ | No | nice (small dome on the ground) | Mars has quakes; instruments stay after you leave |
| **Trash can at a single disposal site** | Sol 12: an empty Small Pressurized Logistics Container is "filled with trash" and parked "next to the lander as its permanent disposal location" (SAC21 ✅). PP23: "double layer containment", "a single site is preferred", "50+ year container design life" (✅). ICES23: "trash, fluids, vented gasses, spills" must be "managed thoughtfully" (✅) | No | **must** | Nothing is thrown away on Mars; you pack it and leave it in one safe place |
| Logistics cans and restock runs | Restock "On Sol 12" and sol 18 from the lander deck (SAC21 ✅) | Partial (cargo bags) | nice | Supplies are counted and fetched |
| Spare parts | "The number of spares ... is largely driven by each system's assessed reliability" (ICES23 ✅) | No | nice (a SPARES crate in the yard) | A part you didn't bring cannot be bought on Mars |

### 2g. Getting around

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| Pressurised rover | The crew's home for 30 sols (SAC21 ✅) | Yes | have | |
| Robotic helper rovers | SAC21 "robotic mobility system" plugs the crew lander into power (✅); DRA5 lists 2 "Robotic Rovers" (✅) | Yes (PIP) | have | |
| Unpressurised rover (Apollo-style buggy) | In DRA5's plan: "two small pressurized rovers, and two unpressurized rovers (roughly equivalent to the lunar rover vehicle (LRV)" (DRA5, EZ16 ✅). Not in SAC21's first stay | No | skip (not in the plan we follow) | |

### 2h. The sky from Gale

| Item | Real-mission role (source) | We have it? | Priority | What a kid learns |
|---|---|---|---|---|
| **Earth as a bright "star"** | Curiosity, at Gale, shot "Earth as the brightest point of light in the night sky", about "80 minutes after sunset" on 31 Jan 2014; a person "could easily see Earth and the moon as two distinct, bright 'evening stars'" (PIA17936 ✅). Whether Earth is an evening or morning star on our game date: ⚠️ our reasoning only; run `tooling/tools/sky-stars.mjs --date ... --from Mars` | Check night-sky shader (not in world.json) | **must** (one sprite, high lesson value) | Home is that dot; light from it takes minutes to arrive |
| Phobos and Deimos | Phobos "rises in the west and sets in the east"; Deimos "rises ... in the east and sets in the west" (PIA06340 ✅); Phobos goes round "three times a day", Deimos "takes 30 hours" (MOONS ✅) | Yes (night sky has both, per missing-assets.md) | have | Mars has two small moons and one goes "backwards" |
| Relay orbiters crossing the sky | No source says a person on the ground could see them | No | **skip** (❌ no source) | |
| Crew spacecraft in orbit | Orbital crew may watch "Phobos/Deimos" (SAC21 ✅); nothing on seeing it from the ground ❌ | No | skip | |

## 3. Must-add list, in order 🚀

1. **MAV on its lander, about 1 km out (191 m on our patch, as layout.md does for the lander), with a "fuel full" gauge.** The story ends in it; MAV21 and SAC21 give its size and the fuelling rule.
2. **Sealed sample containers and a sample return box (100 kg limit).** The science goal at Gale needs somewhere to go; MAV21, ADD-C, SAC21.
3. **Trash can at one disposal spot by the lander.** A real chore and a real rule (SAC21, PP23).
4. **Weather and radiation station plus suit dosimeter badges.** Gives the live NOAA and archived Curiosity numbers a body in the world (DRA5, PP23, MAV21).
5. **Relay antenna and the "Earth sets 12 hours a day" fact.** Explains the comms window (MRN; MAVEN gone since Jun 2026).
6. **Earth as an evening star in the night sky.** Photographed from Gale itself (PIA17936).
7. **End-of-mission beat: suits left behind, clean suits into the MAV, rover drives 1 km away.** No new model; SAC21.

## 4. Things our scene has that the real first stay does not

Already covered in `missing-assets.md` section 8 (greenhouse, oxygen maker, fixed habitat, solar arrays). New on 13 Nov: no ISRU (section 2b), and the crew count (section 5).

## 5. Proposed factcheck rows

Numbered NEW-1 onward; the factcheck owner assigns real numbers. All files are under `research/junior-astronaut/pages/base-gap/`.

| # | Claim | Status | Source |
|---|---|---|---|
| NEW-1 | NASA's 2025 review set the first human Mars missions at "no fewer than four (4) crew to the surface"; "fewer than four crew would present unacceptable crew risk" | ✅ | ADD Rev C (NTRS 20250010956), MD-05 |
| NEW-2 | At its 2024 review NASA "selected nuclear power technology (specifically, fission power) over" solar with storage for the first human Mars missions; fission works "around the clock, and during global dust storms" | ✅ | ADD Rev C, MD-07 |
| NEW-3 | NASA calls 30 sols "the minimum Mars surface stay duration" | ✅ | ADD Rev C, p.191 |
| NEW-4 | Lifting 2 crew to Mars parking orbit needs "more than 30 tons of propellant" with current technology | ✅ | ADD Rev C, gap 1105 |
| NEW-5 | 2-crew MAV: 22,095 kg landed, 36,827 kg at liftoff; works "5.5 years, with up to 4 years on the Mars surface"; carries 2 crew and 100 kg of cargo | ✅ | MAV21 (NTRS 20210026439), Table 4 and Table 1 text |
| NEW-6 | The MAV lands "one opportunity before crew arrival"; a robot moves the rest of the fuel in "about 11 round trips"; "The crew will not be cleared to land on Mars until the full propellant compliment required for powered ascent is confirmed" | ✅ | MAV21 |
| NEW-7 | About 14.3 t of NTO is moved on the ground (11,404 − 5,020 + 8,359 − 425 kg) | ⚠️ our maths | MAV21 Table 4 |
| NEW-8 | First-stay crew range "perhaps a 20 km radius" because of "limited rescue options"; "about two metric tons of science equipment" | ✅ | SAC21 (NTRS 20210026448) |
| NEW-9 | Trash goes in an emptied logistics container parked "next to the lander as its permanent disposal location" | ✅ | SAC21 |
| NEW-10 | Crew board the MAV in "clean launch/entry suits"; EVA suits "would be left behind"; the empty rover drives "nominally about 1 km" away before launch | ✅ | SAC21 |
| NEW-11 | MAV gives "100 kg" for "scientific sample return and any stowage systems" and carries "personal radiation dosimeters" | ✅ | MAV21 |
| NEW-12 | Returned samples "could be as much as 250 kg"; stations for "seismic monitoring and long-duration climate monitoring" keep working after the crew leaves | ✅ | DRA 5.0 (NASA/SP-2009-566) |
| NEW-13 | Planetary protection advice for waste left on Mars: "double layer containment", "a single site is preferred", "50+ year container design life"; pristine samples are "restricted Earth return" | ✅ | PP23 (ICES-2023-361, NTRS 20230010481) |
| NEW-14 | Mars Relay Network: "four spacecraft" (Odyssey, Mars Express, MRO, TGO), links "up to 2 Mbps"; rovers "lack line-of-sight to the Earth for about 12 hours per day" | ✅ | NASA Science MRN page (fetched 13 Nov 2026) |
| NEW-15 | MAVEN is "not recoverable" and no longer able to relay; last heard Dec. 6 (2025); NASA release 3 Jun 2026 | ✅ | NASA release 26-047 |
| NEW-16 | From Gale, Curiosity saw Earth as "the brightest point of light in the night sky" (31 Jan 2014, sol 529); a person "could easily see Earth and the moon as two distinct, bright 'evening stars'" | ✅ | PIA17936 |
| NEW-17 | Phobos "rises in the west and sets in the east"; Deimos rises in the east; Phobos orbits "three times a day", Deimos in "30 hours" | ✅ | PIA06340; NASA Science moons facts |
| NEW-18 | Human Mars exploration zone: sites "within approximately 100 kilometers" of the landing site; landing pads, roads and berms are the top civil-engineering need; the reactor site in the example sits in low hills that "provide a natural form of radiation protection" | ✅ | EZ16 (NTRS 20160001040) |
| NEW-19 | 4-crew MAV with ISRU (2019): oxygen made from Mars air needs "more than 30 kW for a production rate of about 50 kg/day" | ✅ | MAV19 (NTRS 20190001229) |

## 6. Open questions ❓

- **Crew count for the fact card:** NASA now targets at least 4 crew on the surface (NEW-1), our game has 2 (Ravindu's 12 Nov decision, from SAC21). Keep 2 and say "NASA's 2022 study; newer plans send 4", or change? Team decision.
- Whether Earth is an evening or a morning star on the date the game is set: run `sky-stars.mjs`.
- No NASA source found for seeing relay orbiters or the orbiting crew ship from the ground (❌).
- MAV overall height: only figure labels (4.5 m and 7.2 m), no sentence (⚠️, same as missing-assets.md).
- No NASA drawing found of the trash container, the sample return box or the weather mast; sizes would be our design.
- No source says how far a weather mast or a seismometer stands from the habitat.
