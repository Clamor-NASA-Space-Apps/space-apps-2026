# Where our story meets real Mars 🔴

Checked on 13 Nov 2026 for Outpost Gale. Saved sources are in `pages/mission/` unless another path is given. Quotes were confirmed with `kwic.py`. ✅ = seen in a NASA (or named) source, ⚠️ = our maths or a secondary source, ❌ = not found.

## TL;DR

- **Where we are:** the base sits on the flat floor of Gale crater, about 200 m west of Curiosity's landing spot (Bradbury Landing, 4.5895° S, 137.4383° E). The ground is real HiRISE data. That is 2.2 km from the spot a JPL-led team proposed for the first human landing in 2015. ✅ honest.
- **Biggest clash:** Curiosity is not near the base. On sol 5070 (about 10 Nov 2026) it was **14.3 km south-south-west, about 1,030 m higher, on the slopes of Mount Sharp**, still working. Mont Mercou is **8.8 km away** (bearing 190°), not 55 m. In the game both stand 55 to 125 m from the habitat, and in the wrong directions.
- **Fix:** keep the base where it is and make Curiosity and Mont Mercou "a drive away": a rover trip with a time skip. NASA's own 30-sol plan does exactly this: three rover trips of about five sols each, up to 20 km from the landing site.
- **Smaller catches:** NASA's first 30-sol crew lives in the rover, not in a base with a greenhouse. No ice to drill at Gale. The trip home is about a year, not 7 months. Mars Sample Return was cancelled in January 2026, so never say "the samples will join Perseverance's". Never say our samples are the first Mars rocks on Earth (about 435 Mars meteorites are known).

**Kid version:** you live on the flat crater floor where Curiosity landed in 2012. Curiosity has since climbed a mountain, so visiting it is a road trip.

---

## 1. Where is Curiosity, and where are we? 📍

**What's true**
- Curiosity is working. The team's blog for sols 5063 to 5069 (planning date 6 Nov 2026, posted 11 Nov 2026) has it "completing its drill campaign at the 'Nazca' drill hole", sending powder to SAM, then a drive "back towards its southerly trending route". ✅ `curiosity-sols-5063-5069.html`
- NASA's rover map data (the "Where is Curiosity" map, file `MSL_waypoints_current.json`): sol 5070, 4.8257° S, 137.3892° E, elevation −3,474 m, odometer **38,610 m** (38.3 km). ✅
- Landing (sol 3 in the same file): 4.589467° S, 137.441633° E, −4,501 m. ✅ This closes the "no NASA page with Bradbury to four decimals" gap in the game's `design/research/sizes.md`.
- On 28 Aug 2026 Curiosity "passed the 1 kilometer mark of elevation from its landing site"; sol 5,000 fell on 29 Aug 2026. ✅ `curiosity-sols-4995-5001.html`
- Mont Mercou: "a rock outcrop that stands 20 feet (6 meters) tall", at the "transition between the 'clay-bearing unit' ... and the 'sulfate-bearing unit'"; selfie on 26 Mar 2021 (sol 3070) beside the "Nontron" drill hole, "the mission's 30th sample". ✅ `mercou-selfie-release.html`. NASA calls it an outcrop or cliff, not a butte.
- Curiosity sat at Mont Mercou on sols 3049 to 3079: 4.7353° S, 137.4126° E, −4,073 m, odometer 25.2 km. ✅ (waypoint file)

**Distances (our maths ⚠️, great circle on a 3,396.19 km sphere, from `MSL_waypoints.json`)**

| From | To | Straight line | Bearing | Height |
|---|---|---|---|---|
| Our base (terrain centre) | Bradbury Landing | 197 m | 89° (east) | same |
| Our base | Mont Mercou | 8.8 km | 190° (S) | +430 m |
| Our base | Curiosity, sol 5070 | 14.3 km | 192° (SSW) | +1,030 m |
| Mont Mercou | Curiosity, sol 5070 | 5.5 km | 194° | +600 m |

**What we have:** `data/world.json` puts Curiosity at (80, 95) and Mont Mercou at (−40, 38), that is 124 m at bearing 140° (SE) and 55 m at 226° (SW). The note says Curiosity "is really far up the mountain", which is right, but the scene shows it next door.

**The clash:** a judge who follows Curiosity knows it left the landing plain in 2012. "Curiosity and Mont Mercou both near the base" is false. The game also turns them to the wrong side.

**Where should the base honestly be?** Where it is. The landing plain is flat (6 m of relief in our 400 m patch), it is where every human-landing proposal for Gale put the crew (section 2), and moving next to Curiosity would put the base on a 15° slope (rover pitch 14.7° on sol 5070) with no HiRISE patch on disk.

**Fix (one line):** call them "a drive away", show a signpost or map pin ("Curiosity: 14 km, 1 km up the mountain"), and reach them by a rover trip with a time skip; if the 3D models stay near the base, label them as the destination scene, not the view from the base.

---

## 2. Was Gale ever proposed for humans? 🧑‍🚀

**What's true**
- NASA's "First Landing Site/Exploration Zone Workshop for Human Missions to the Surface of Mars" ran 27 to 30 Oct 2015 in Houston. 47 exploration zones, each about 200 km wide, were proposed. ✅ `planetary-2016-ez-vote.html` (Planetary Society, 22 Jan 2016, ⚠️ secondary for the vote)
- Three Gale abstracts were presented:
  - Calef (JPL) et al., #1020, "Assessing Gale Crater as a Landing Site for the First Human Mission to Mars": landing point "at the center of the final MSL landing ellipse at 137.4019° longitude and -4.5965° latitude"; "Go where you know"; Gale is "one of the lowest elevation landing sites", which helps landing; "There is little chance of near-surface water-ice for resource utilization in Gale, but water bound in minerals and adsorbed to loose grains could serve as a water source". ✅ `ez2015-1020.txt`
  - Yun, #1022: Gale "has been proven to meet Engineering Constraints through the successful landing of Curiosity". ✅ `ez2015-1022.txt`
  - Montaño et al. (Los Alamos), #1040: an infrastructure site "less than 5 km to the northeast of the landing site", small craters as "ready-made radiation shielding". ✅ `ez2015-1040.txt`
- After the workshop NASA did not pick a site: "there would be no immediate attempt to downselect". Participant votes put "Melas Chasma, Jezero Crater and Gale Crater" on top. ⚠️ Planetary Society report
- NASA's 2022 surface plan: "A specific landing site has not been selected at this time." ✅ `pages/sleep/ntrs-20220000589-sac21-surface-ops.txt`

**What we have:** a base at Gale. Our spot is 2.2 km east of the Calef landing point (our maths ⚠️).

**The clash:** none, as long as we say "scientists proposed Gale", not "NASA chose Gale". Calef's paper is a proposal by scientists (lead author at JPL), not a NASA decision.

**Fix:** in-game line: "In 2015 scientists proposed Gale for the first human visit, because Curiosity already knows the ground."

---

## 3. Planetary protection and samples 🧫

**What's true**
- NASA agrees with COSPAR: "Safeguarding the Earth from potential back[ward] contamination is the highest planetary protection priority in Mars exploration"; "it will not be possible for all human-associated processes ... to be conducted within entirely closed systems"; humans "will inevitably be exposed to martian materials". ✅ NASA Interim Directive NID 8715.129, 9 Jul 2020 (`nasa-nid-8715-129.txt`). It listed an expiry of 9 Jul 2023; its later status ❌ not confirmed.
- NASA Planetary Protection Office, 4 May 2022: "Robotic prescriptive requirements are impractical for crewed missions"; "Human spaceflight hardware leaks"; crews need "quarantine capabilities, sample containment handling and testing protocols". Their concept draws a "Safe Zone for Human Activities" around the habitat and sends robots, not people, into places that might hold life. Methane sources "(if identified)" count as "Uncertain Regions", "treated as Special Regions until proven otherwise". ✅ `ntrs-20220006192-human-mars-pp.txt`
- NASA's 30-sol plan (SAC21, Jan 2022): rules are "poorly defined for crewed missions", but expect limits on "pristine sample acquisition, containment of waste materials/contaminants, and restricting the amount/type of uncontained Mars material returned to Earth". Before launch the crew wear "clean launch/entry suits"; "EVA suits are left behind on the surface"; a pressurised tunnel links rover and ascent vehicle "without going outside"; trash bags go "next to the MDS as its permanent disposal location". ✅ `pages/sleep/ntrs-20220000589-sac21-surface-ops.txt`
- Crews near a working rover: ❌ no NASA rule found. The nearest precedent: Apollo 12 landed "about 535 feet northwest from where Surveyor III stood" (19 Nov 1969) and the crew were "to retrieve portions of the Surveyor III spacecraft". ✅ `nasa-apollo12-surveyor3.html`. Surveyor was dead; Curiosity is not.
- Mars Sample Return is about **Perseverance's samples at Jezero**, not Gale: objective "Bring Mars samples collected by the Perseverance rover to Earth"; NASA's page now says MSR "was a proposed multi-mission campaign". ✅ `nasa-msr.html`. Congress's January 2026 spending bill: "The agreement does not support the existing Mars Sample Return (MSR) program" (report of 6 Jan 2026; Senate vote reported 15 Jan 2026). ⚠️ Live Science, 16 Jan 2026 (`livescience-msr-dead.html`)
- About 435 Mars meteorites are known on Earth. ✅ NASA/JPL, 29 Oct 2026 (`nasa-mars-meteorite-teghaza.html`)

**What a real crew would do differently**
1. Pick samples with clean tools straight into sealed tubes or bags, never by glove, and keep them sealed, outside the living space.
2. Look at Curiosity, do not touch it: it is working, and its team on Earth is driving it.
3. Leave suits and trash on Mars, fly home in clean suits through a tunnel.
4. Go into quarantine and hand sealed samples to a special lab on Earth.

**The clash:** our story says "collect samples so Earth's labs can study them": ✅ fine. Risky lines: "the first Mars rocks on Earth" (meteorites exist), "join the Perseverance samples" (MSR cancelled, and those are at Jezero), a hero who grabs pebbles with a glove and drops them in a hip bag (`design/plans/next-lanes.md`, "Take a rock sample"), and a kid who touches or repairs Curiosity.

**Fix:** a scoop or tongs puts the pebble into a sealed tube in the hip bag, and the visit to Curiosity is "look, photograph, don't touch".

---

## 4. 30 sols, then home ✈️

**What's true**
- DRA 5.0 (NASA SP-2009-566): opposition-class missions have "short surface stay times at Mars (typically 30 to 90 days) and relatively short total round-trip mission times (500 to 650 days)"; one leg needs "a close passage by the sun (0.7 AU ... or less)"; the ship leaves "after a brief stay" instead of waiting for good alignment. Conjunction-class: "500 days or more" on Mars, "approximately 900 days" in all. ✅ `pages/agent-power/dra5-sp-2009-566.txt`
- DRA 5.0 example timeline, opposition class: "OUTBOUND 217 days, STAY 30 days, RETURN 403 days" (650 days). ✅ same file
- ICES-2023-265: the plan is a crew of four on "up to a 1200 Earth-day roundtrip", with "a minimum 50 sol stay in Mars orbit which would support a minimum 30 sol two crew Mars surface mission"; "At the completion of the 30 sol mission, the crew will return to the TH in the Mars Ascent Vehicle (MAV), dock with the TH, and return to Earth." ✅ `pages/agent-power/ntrs-20230002103.txt`
- SAC21: launch from the surface "nominally Sol 31"; "the next 2.5 sols flying to the DST" (the ship in orbit). ✅ SAC21 surface ops
- Launch windows every 779.94 days (about 26 months). ✅ factcheck (NSSDC)

**What we have:** 2 crew, 30 sols, then pack up and fly home. This matches the NASA plan (factcheck rows 132, 149, 150).

**The clash:** only if the game says the trip home is "7 months" (that is the outbound trip on a slow, cheap path) or that the whole mission is 30 days. Also, NASA's first crew lives in the pressurised rover: "crew for 30 sols and will be their only means of habitation" (ICES-2023-265 p.7). Our base with HAB 1, a greenhouse and a storm shelter is a bigger, later kind of outpost. A greenhouse also cannot grow a full lettuce in 30 sols (33 days, factcheck); microgreens and radishes can.

**Fix:** "After 30 sols you ride a small rocket up to your ship. The trip home takes about a year (403 days in one NASA plan)." For the base, one line: "Cargo landers set this outpost up before you came; NASA's very first visit would live in its rover."

---

## 5. What a crew at Gale would collect, and why 🪨

| Rock | Where | Why (kid version) | Source |
|---|---|---|---|
| Grey mudstone with clay | Yellowknife Bay ("Sheepbed", "John Klein", "Cumberland"), near Bradbury | Old lake mud. It holds "sulfur, nitrogen, oxygen, phosphorus and carbon--key ingredients necessary for life", "clay minerals and not too much salt", so "fresh, possibly drinkable water once flowed there". Kid: "This rock was once the bottom of a lake you could drink from." | ✅ `curiosity-science-highlights.html` |
| Organics in old mud | Cumberland (drilled 19 May 2013) | The biggest carbon chains found on Mars (decane to dodecane); maybe pieces of fatty acids, but "there's no way to confirm that these long-chain alkanes resulted from biology". Kid: "building blocks, not life." | ✅ `gsfc-largest-organics-2025.txt` (PNAS, Mar 2025) |
| Lake layers of Mount Sharp | Murray formation (lower Mount Sharp) | "over 1,000 vertical feet of rock formed originally as mud at the bottom of a series of shallow lakes"; lakes lasted "perhaps a million years or longer" | ✅ `curiosity-science-highlights.html` |
| Clay to salt (sulfate) change | Mont Mercou, "Nontron" sample | Where Mars may have dried out: "this transition might reveal what happened to Mars as it became the desert planet". Kid: "the rock where the lake started drying up." | ✅ `mercou-selfie-release.html` |
| Yellow sulfur crystals | Gediz Vallis channel, 30 May 2024 | "the first time this kind of sulfur has been found on the Red Planet" | ✅ `sulfur-crystals-2024.html` |
| Windblown dust and sand | everywhere (Rocknest) | Red dust beside grey drill powder; holds water (factcheck row 129) | ✅ highlights page |

**What we have:** pebbles near Mont Mercou and near the base. **The clash:** pebbles at the base are landing-plain rocks (old river and lake rocks are honest there, as at Yellowknife Bay), but "Mont Mercou rocks" are 8.8 km away. **Fix:** the base-side samples are "lake mudstone like Yellowknife Bay"; Mont Mercou samples come from the rover trip. Keep the line "building blocks, never life" (CLAUDE.md, factcheck rows 69, 70).

Note: NASA's 2022 surface plan names the agency goal as a search "for signs of extant life (i.e., life that still exists today)" (SAC21). Our goal, "could Gale once support life", is Curiosity's goal and the safer one for kids. ✅ No clash.

---

## 6. Other things a Mars judge would catch 🔍

| Topic | What's true | Our risk | Fix |
|---|---|---|---|
| Ice at Gale | "little chance of near-surface water-ice ... in Gale" (Calef 2015 ✅); NASA's first stay brings all water (factcheck row 132) | `plan.md` lists an "ice drill" asset | Drop the ice drill; if water from the ground is shown, it is a soil oven (about 2% water, factcheck row 129) |
| Dust storms | "Larger storms typically only happen during summer in Mars' southern hemisphere" ✅ `../nasa-dust-storms.html`; global about every 3 Mars years | A global storm in a random week | Small storms any time; a big one only in "storm season" |
| Temperature | +15.9 °C to −100 °C at Gale (factcheck row 10) | none seen | |
| Sky | butterscotch by day, blue near the sunset Sun (rows 167, 168) | none, the look already follows it | |
| Phobos and Deimos | Curiosity photographed Phobos crossing Deimos (1 Aug 2013, PIA17350) and an annular eclipse by Phobos (PIA17356); it imaged another Phobos eclipse in early Nov 2026 ✅ (`curiosity-sols-5063-5069.html`, game `design/research/pages/moons/`) | Moons drawn too big | Phobos is about a third of the Sun's width (row 178); Deimos is a bright star |
| Methane | Curiosity sees seasonal methane (row 70); a methane source, if found, is treated as a Special Region ✅ | A "methane vent" place to visit | Leave it out, or a robot-only zone |
| Mont Mercou | a 6 m outcrop (NASA) | Our model stands about 4 to 5 m above ground; docs call it a "butte" | Call it a cliff or outcrop; scale to 6 m if it is ever reused |
| Curiosity's look | 38 km on its wheels, dusty, 14 years on Mars | a clean rover | Dust coat on the model |
| Live data rule | Curiosity's position changes every few sols | A fixed "Curiosity is here" | Label it ARCHIVED 10 Nov 2026 (sol 5070), from NASA's map data |

---

## Open questions ❓

- NID 8715.129's status after its July 2023 expiry date (still in force, replaced, or cancelled).
- Any NASA rule on astronauts approaching a working rover.
- Where the 2024 sulfur crystals site lies relative to our base (not looked up).
- A NASA page (not a news site) on the January 2026 MSR decision.

---

## Proposed factcheck rows

| Claim | Status | Source |
|---|---|---|
| Curiosity still operating: drill campaign at "Nazca", planning date 6 Nov 2026, blog posted 11 Nov 2026 | ✅ | NASA Science, Curiosity Blog sols 5063 to 5069 |
| Curiosity on sol 5070: 4.8257° S, 137.3892° E, −3,474 m, odometer 38,610 m | ✅ | NASA rover map data, MSL_waypoints_current.json (fetched 13 Nov 2026) |
| Bradbury Landing (sol 3 waypoint): 4.589467° S, 137.441633° E, −4,501 m | ✅ | NASA rover map data, MSL_waypoints.json |
| Curiosity passed 1 km above its landing site (28 Aug 2026); sol 5,000 was 29 Aug 2026 | ✅ | NASA Science, Curiosity Blog sols 4995 to 5001 |
| Curiosity on sol 5070 is 14.3 km from our base, bearing 192°, about 1,030 m higher; Mont Mercou 8.8 km, bearing 190°, about 430 m higher | ⚠️ our maths | from the two rows above |
| Mont Mercou: a 6 m outcrop at the clay to sulfate transition; Nontron = 30th sample; selfie 26 Mar 2021 (sol 3070) | ✅ | NASA/JPL release, 30 Mar 2021 |
| 2015 NASA workshop: 47 exploration zones, about 200 km wide; Gale among the three most-voted; no site chosen | ⚠️ secondary | Planetary Society, 22 Jan 2016 |
| Calef et al. 2015: proposed human landing point 4.5965° S, 137.4019° E (centre of Curiosity's landing ellipse); "little chance of near-surface water-ice ... in Gale" | ✅ | First Landing Site/EZ Workshop abstract 1020 |
| NASA 2022: "A specific landing site has not been selected" | ✅ | SAC21 surface ops, NTRS 20220000589 |
| Back contamination is "the highest planetary protection priority"; crews "will inevitably be exposed to martian materials" | ✅ | NASA NID 8715.129 (9 Jul 2020) |
| Crewed missions: "Robotic prescriptive requirements are impractical"; methane sources (if identified) treated as Special Regions | ✅ | NASA PP Office slides, NTRS 20220006192 (4 May 2022) |
| End of a 30-sol stay: clean launch suits, EVA suits left on Mars, tunnel to the MAV, trash left by the lander, launch nominally sol 31 | ✅ | SAC21 surface ops, NTRS 20220000589 |
| Mars Sample Return was for Perseverance's Jezero samples; NASA now calls it "a proposed" campaign in the past tense | ✅ | NASA Science MSR page |
| Congress, Jan 2026: "The agreement does not support the existing Mars Sample Return (MSR) program" | ⚠️ secondary | Live Science, 16 Jan 2026 |
| About 435 Mars meteorites are known on Earth | ✅ | NASA/JPL, 29 Oct 2026 (Teghaza 001) |
| Apollo 12 landed 535 ft from Surveyor 3 and the crew were to retrieve parts of it | ✅ | NASA, "Apollo 12: The Pinpoint Mission" |
| Opposition class: 30 to 90 days on Mars, 500 to 650 days in all, passes inside 0.7 AU; example 217 out, 30 stay, 403 back | ✅ | DRA 5.0, NASA SP-2009-566 |
| NASA plan: "up to a 1200 Earth-day roundtrip", "minimum 50 sol stay in Mars orbit", 30 sols on the surface for two | ✅ | ICES-2023-265, NTRS 20230002103 p.2 |
| Yellowknife Bay mudstone: key ingredients for life, clay, "fresh, possibly drinkable water" | ✅ | NASA Science, Curiosity science highlights |
| Largest organics on Mars (decane, undecane, dodecane) in Cumberland; biology cannot be confirmed | ✅ | NASA GSFC, PNAS Mar 2025 |
| First elemental sulfur on Mars, cracked open 30 May 2024 | ✅ | NASA PIA26309 |

## Files saved (`pages/mission/`)
`curiosity-sols-5063-5069.html`, `curiosity-sols-4995-5001.html`, `curiosity-updates.html`, `MSL_waypoints.json`, `MSL_waypoints_current.json`, `mercou-selfie-release.html`, `mercou-selfie.html`, `ez2015-1020/1022/1040.{pdf,txt}`, `planetary-2016-ez-vote.html`, `nasa-nid-8715-129.{pdf,txt}`, `ntrs-20220006192-human-mars-pp.{pdf,txt}`, `nasa-msr.html`, `livescience-msr-dead.html`, `nasa-mars-meteorite-teghaza.html`, `nasa-apollo12-surveyor3.html`, `curiosity-science-highlights.html`, `gsfc-largest-organics-2025.{pdf,txt}`, `sulfur-crystals-2024.html`. Already on disk and reused: `pages/agent-power/dra5-sp-2009-566.txt`, `pages/agent-power/ntrs-20230002103.txt`, `pages/sleep/ntrs-20220000589-sac21-surface-ops.txt`, `pages/nasa-dust-storms.html`.
