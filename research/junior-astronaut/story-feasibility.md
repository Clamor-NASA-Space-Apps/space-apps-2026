# Story mechanics: are they real? (fact-check, 13 Nov 2026)

Six mechanics the team wants for Outpost Gale (2 crew, 30 sols, a pressurised rover, trips to Mont Mercou 8.8 km and Curiosity 14.3 km), checked against NASA sources. New sources are in `pages/story/`, older ones are in `pages/sleep/`, `pages/agent-habitat/`, `pages/agent-power/` and `bvad.txt`. Quotes were confirmed with `kwic.py`. "Our maths" means we did the arithmetic ourselves from sourced inputs (⚠️).

## TL;DR

| # | Mechanic | Real? | Key numbers | Game rule it supports |
|---|---|---|---|---|
| 1 | Hard work raises heart rate, burns suit air faster, tires you | ✅ yes. The heart-rate part is weaker: Apollo used it, but it was the least reliable gauge | Apollo average 233 kcal/h vs hard 10 km walk 599 kcal/h; O₂ 0.15 vs 0.4 lb/h (2.7×); Apollo 15 heart rates averaged 84 to 125 bpm | Running drains O₂ and cooling about 2.5 to 3 times faster than calm work; riding the rover is the cheapest way to move |
| 2 | Suit battery limits the EVA | ✅ real, but a weaker limit than oxygen | Apollo 15 PLSS: 25.7 Ah loaded, about 20 Ah used per 7 h EVA, redline 3.1 Ah; ISS suit battery 36.4 Ah at 15.5 to 20.5 V | Battery drains with time, not with effort; O₂ and cooling are what effort burns |
| 3 | Walkback limit | ✅ yes | Apollo: "not more than 6 miles from the LM" (about 9.7 km). NASA's 30-sol plan: "no more than 20 kilometers radial distance", an unpressurised rover goes along as the lifeboat, and the crew sleeps in the pressurised rover | Never drive further than you could get home from if the big rover dies |
| 4 | Rover battery | ✅ yes | 60 kWh base, 200 kWh for 5-sol trips, 8 km/h, life support 1.85 kW, about 1 kWh per km (our maths), recharge from the 10 kW reactor in about 2 sols, a 20 km drive-home reserve kept at all times | The battery runs the wheels **and** the air: keep enough to drive home |
| 5 | The ship in orbit as a moving light | ⚠️ plausible, but only now and then | 5-sol orbit, low point 250 km, high point about 112,500 km (our maths); bright (about mag −1 to +3) only for about 1.5 h around the low point, once every 5 sols | "Once every 5 sols the ship skims low. At dusk you might see it" |
| 6 | Milky Way and dust devils | ⚠️ Milky Way likely overhead on clear nights (no Mars photo of it exists); ✅ dust devils at Gale | Stars overhead lose "nearly 1 magnitude" to dust, 3 to 4 near the horizon; Spirit photographed Orion in 2005 | Clear nights show stars and a faint Milky Way high up; dusty nights hide it |

---

## 1. Exertion in a suit 🫀

**What's real**
- **Work rate is the driver.** NASA's life-support handbook (BVAD 2022, Table 4-71, from NASA HIDH 2014) lists suited metabolic rates:
  - Apollo lunar EVA: min 517, average 1,030, max 2,607 kJ/h (about 143, 286 and 724 W).
  - Space station spacewalks: average 950 kJ/h.
  - "Advanced Walkback Test" (a simulated 10 km walk home after a rover failure, 1 to 2 hours): average 2,505 kJ/h, max 3,167 kJ/h (about 700 and 880 W).
- **Rest vs work.** Resting oxygen use is "approximately 3.8 mL/kg-min", and "resting in the suit" was measured at 6.8 mL/kg/min (Gernhardt 2013, NASA EVA chapter). For an 82 kg astronaut that is about 105 W at rest (our maths, Weir equation below).
- **Air per unit of work.** BVAD gives the Weir equation: energy = 3.941 × O₂ litres + 1.106 × CO₂ litres. With BVAD's respiratory quotient of 0.86, that is about 4.9 kcal per litre of O₂, or about **0.29 g of O₂ per kcal** (our maths). Check: it predicts 68 g/h at the Apollo average and 174 g/h on the walkback. NASA measured 0.15 lb/h (68 g) and 0.4 lb/h (181 g). It matches.
- **Hard walking vs normal EVA** (Norcross, NASA JSC 2007, Walkback Test):

  | | Walkback (10 km) | Apollo average |
  |---|---|---|
  | Energy | 599 kcal/h | 233 kcal/h |
  | O₂ use | 0.4 lb/h | 0.15 lb/h |
  | Cooling water | 3.1 lb/h | 0.98 lb/h |

  The subjects walked 10 km in 95.8 minutes on average (3.9 mph), at about 51% of their peak oxygen uptake. Rated effort was 11.8 on the Borg scale ("light"). The limit on going faster was heat, not breath: subjects "would have liked to ambulate at higher speeds, but were not able to because of cooling limitations."
- **Suit time shrinks with work.** The Apollo 11 to 14 backpack could absorb about 1,200 kcal of body heat: "at ... 400 kcal/hr for three hours, or at ... 300 kcal/hr for four hours". The Apollo 15 to 17 backpack held 1,800 kcal: "seven hours at ... 250 kcal/hr ... or eight hours at ... 225 kcal/hr" (Biomedical Results of Apollo, NASA SP-368, 1975). At the walkback rate, 1,800 kcal lasts about **3 hours** (our maths).
- **It happened for real.** On Apollo 15 (Jul to Aug 1971): "the oxygen redline limits were approached, indicating that the crew workload was approaching the portable life support system capability" (Apollo 15 Mission Report, 1972).
- **Riding saves air and energy.** Riding the lunar rover gave the lowest rates, close to "shirt sleeve riding in an automobile". That helped "through reduction in both the use of consumables and the fatigue experienced by crewmen" (SP-368). DRA 5.0 says rovers "mitigate crew fatigue and ... extend consumable supplies by allowing lower metabolic rates during seated travel."
- **How Apollo used heart rate.** There were 3 real-time methods:
  1. Heart rate, "related to metabolism on the basis of a correlation with bicycle ergometer workload which was established before the flight".
  2. Oxygen bottle pressure drop.
  3. Cooling-water temperature rise.

  After the flights the best estimate averaged methods 2 and 3, and "the heart rate method was not used independently". Heart rate also rises with nerves: on the command-module spacewalks, "Elevation of these heart rates was attributed more to excitement than to exercise."
- **Typical EVA heart rates.**
  - Apollo 11 (21 Jul 1969): averages of 110 bpm (Commander) and 88 bpm (Lunar Module Pilot).
  - Apollo 15: Commander averaged 92, 84 and 85 bpm over the 3 EVAs, the Lunar Module Pilot 125, 107 and 105 bpm.
  - The Apollo 11 LMP reached 170 and 177 bpm during hard in-flight exercise (mission reports).
  - A 2021 NASA-hosted thesis chapter (2 subjects, simulated lunar EVA) found 56 bpm vs 138 bpm at similar work rates: people differ a lot. ⚠️ Small study.
- **Mars backpack.** The Apollo cooler (a sublimator) "depends on the vacuum of space and would therefore be infeasible on the Mars surface" (Mars PLSS paper, ICES-2026-126). A Mars suit's cooling is still being designed.

**What the game may say**
- "Running burns your suit air about 2 to 3 times faster than walking calmly." Walkback 0.4 vs Apollo 0.15 lb/h.
- "Hard work heats you up. If the suit can't cool you, slow down."
- "Riding the rover saves air."
- "Your heart beats faster when you work hard, or when you're scared." Show heart rate as a feel meter.
- Kid version: "Running makes you hot and hungry for air. Walk smart, ride when you can."

**What it must not say**
- That the suit measures air use from heart rate. Apollo found heart rate the least reliable of the 3 methods.
- That sprinting tires you out in a minute. The 10 km walkback felt "light". Hours of hard work do tire you (Apollo, DRA 5.0).
- Any fixed heart-rate number as "the" EVA rate. Apollo averages ranged from 84 to 125 bpm between people.

## 2. Suit power 🔋

**What's real**
- **Apollo had a battery tracked like oxygen.** The Apollo 15 consumables table lists each crewman's battery: 25.7 Ah loaded, 19.3 to 20.7 Ah used on 7-hour EVAs, 5.0 to 7.1 Ah left, redline 3.1 Ah (Apollo 15 Mission Report, Table 8-1). In the same table, oxygen came closest to its redline. The Commander's first EVA ended with 0.38 lb of O₂ against a 0.37 lb redline.
- **The rover had batteries too.** The lunar rover ran on "two 36-volt silver-zinc batteries driving an independent 1/4-hp motor in each wheel" (NASA SP-350).
- **Station suit battery.** The ISS suit battery (LLB2) is 36.40 Ah at 15.5 to 20.5 V, about 650 Wh (our maths) (Russell, NASA JSC 2021).
- **Next-generation suits.**
  - xEMU (not flown): "8-hour autonomous performance". Its battery is "pushing the limit on void volume".
  - Mars suit: moving to "a monolithic battery design rather than the multiple discrete battery packs ... used in the xEMU" (ICES-2026-126).

**Our reading** (⚠️ inference)
- The battery runs fans, pumps, radio and displays, which work at a steady rate.
- So battery use tracks time outside, while oxygen and cooling water track effort.
- No source gives a battery number for a Mars suit.

**What the game may say**
- "Your backpack has a battery. It runs the fan, the pump and the radio."
- Battery drains with time; air and cooling drain with effort.

**What it must not say**
- "The suit battery makes your air." Air comes from oxygen tanks.
- Any Mars suit battery capacity. None is published.

## 3. Walkback limit 🚶

**What's real**
- **Apollo.** An Apollo 17 crewman, in NASA's own history (SP-350, ch. 14): "Mission rules restricted us from going more than 6 miles from the LM - the distance we could walk back in a pinch". 6 miles is about 9.7 km. NASA later wrote: "It has been assumed, based on Apollo program experience, that 10 kilometers (6.2 mi) will be the maximum EVA excursion distance from the lander or habitat" (Walkback Test, 2007). Six astronauts then proved a suited 10 km walk at Moon gravity on a treadmill.
- **One rover vs two** (DRA 5.0, 2009):
  - "If one rover is used, the EVA team would be constrained to operate within rescue range of the surface base. This could mean either the team has sufficient time to walk back ... or that there is sufficient time for a rescue team ... to reach them."
  - Two identical rovers are "mutually supporting" and extend the range.
  - DRA 5.0 also names "approximately 15 km, or EVA walk-back distance" for one leg of a long traverse.
- **NASA's 30-sol plan** (SAC21 surface ops, HEOMD-415, Jan 2022):
  - "Due to limited rescue options ... crewed exploration around the landing zone is expected to extend to about 20 kilometers radius". Nobody else is on the surface: the other 2 crew are in orbit.
  - "Because of anticipated limits on the range that crew will be able to walk in Mars EVA suits, it is assumed ... that the unpressurized rover accompanies the pressurized rover on any extended range traverse."
  - The limit is "no more than 20 kilometers radial distance from the landing site", with "an allowance for terrain-caused deviations".
  - Chappell et al. (IEEE 2022) also keep "enough power to perform up to a 20km drive back in the event of a contingency".
- **Trips and sleep.**
  - Three trips: sols 7 to 11, 14 to 18 and 21 to 25. Each is a drive out, EVAs over several sols, then a drive back to recharge.
  - On sol 7 the crew does "a 2.5-hour EVA reconnaissance before preparing the PR for an overnight stay".
  - The crew lives in the pressurised rover the whole mission: "The crew will land and live in a pressurized rover" (Chappell). The rover holds "as much as 14 sols of logistics for two crew".
- **Game check.** Mont Mercou (8.8 km) and Curiosity (14.3 km) are both inside the 20 km radius.

**What the game may say**
- "NASA's plan: never drive more than 20 km from base."
- "Apollo astronauts never drove further than they could walk home (about 10 km)."
- "A small open rover comes along as a lifeboat."
- "You sleep in the rover."
- Kid version: "Only go as far as you can get home from."

**What it must not say**
- That the crew walks 20 km home on Mars. The plan uses the open rover for that.
- That someone on the surface can come and rescue them.

## 4. Rover battery ⚡

**What's real** (Chappell, Hoffman, Bekdash, Rucker, IEEE 2022, NTRS 20210022250 and slides 20220003043)

| Item | Value |
|---|---|
| Rover mass | 5,193 kg "with 60 kW-H of batteries" |
| Battery for 5-sol trips | "200 kW-hr battery selected to meet continuous operations objectives" (+140 kWh = 933 kg at 150 Wh/kg) |
| Speed | 8 km/h, "fixed at an assumed average rate" |
| "Hotel load" (avionics, habitation) | 1.85 kW |
| Recharge | the 10 kW reactor; 4.85 kW left for the rover, of which 3 kW goes into the battery while 1.85 kW keeps the cabin running |
| Recharge time | about 2 sols ("Total recharge duration = 48 hrs") |
| Drive cost model | rolling resistance 0.15 × mass × gravity × distance |
| Reserve | always keep enough "to perform up to a 20km drive back" |

- **Day trip.** On 60 kWh, a "Commuter" day trip covers 24 km in 11 hours, with 8 hours of EVA. Recharge takes 13.65 h.
- **Solar.** The SAC21 surface ops document assumes "no on-board capability to replenish stored energy – such as solar arrays". Chappell's model adds an optional 3.5 kW panel. So treat solar as "maybe".
- **Our maths** (⚠️, from Chappell's inputs with Mars gravity 3.71 m/s²):
  - Driving: 0.15 × 5,193 kg × 3.71 = 2.9 kN, which is **0.8 kWh per km**.
  - Life support at 8 km/h adds 0.23 kWh/km, so about **1 kWh per km** in all.
  - Check against Chappell's day trip: 24 km takes 19 kWh to drive, plus 11 h × 1.85 kW = 20 kWh, so 39 kWh. Recharging that at 3 kW takes 13 h. Chappell lists 13.65 h, so the model holds.
  - Life support alone uses 45.6 kWh per sol. A flat-out 60 kWh battery keeps the cabin alive for about 32 hours with no driving.
- **Game trips** (our maths): Mont Mercou and back is 17.6 km, about 18 kWh of driving. Curiosity and back is 28.6 km, about 29 kWh. Life support time comes on top.
- **Running flat.** No source describes it, because the plan forbids it (the 20 km reserve). The battery also powers the cabin (the "hotel load"). A flat battery means no air fans, heat or radio, not only stopped wheels (⚠️ inference from the hotel-load definition). The backup is the unpressurised rover (section 3).
- **Older plan.** DRA 5.0 (2009) sized a smaller rover differently: 25 kWe to drive at 3 km/h, 250 kWh of batteries. It is an older, different design; don't mix its numbers in.

**What the game may say**
- "The rover battery runs the wheels and your air."
- "Driving costs about 1 kWh per km." (⚠️ our maths)
- "Always keep enough to drive home."
- "Recharging at the reactor takes about 2 sols."
- Kid version: "The rover battery is your air and your wheels. Never spend the ride home."

**What it must not say**
- That the rover charges itself from solar while you drive (not in the plan of record).
- Any range figure presented as NASA's own. Range per charge is our maths.

## 5. The ship in orbit 🛰️

**What's real**
- **Plan.** The ship waits in "a 5-sol Mars orbit for a 50-Earth day loiter" (SAC21 surface ops). After launch the crew "spends the next 2.5 sols flying to the DST" (Chappell 2022). The orbital crew "may also use their vantage point for Mars surface or Phobos/Deimos observations".
- **Shape.**
  - The 5-sol orbit is "highly elliptical", spending "a significant percentage of their orbital period at distances far from" Mars (Round-Trip Mars Mission Mass Challenges, 2023).
  - In a NASA hybrid-ship study, the capture burn happens "at 250 km altitude" and the ship sits "in 5-sol parking orbit with its periapse directly above the Jezero crater" (AAS 19-225). So the low point can be placed over the landing site.
- **Size of the orbit** (our maths, ⚠️, Kepler's law with Mars GM 42,828 km³/s², a sol of 88,775 s and a low point of 250 km): the high point is about **112,500 km** up.
  - Check: the same maths gives 33,867 km for a 1-sol orbit, and DRA 5.0 lists 250 × 33,793 km.
  - Speed is 4.8 km/s at the low point and 0.15 km/s at the high point.
  - The ship is below 5,000 km for only about 85 minutes of each 5-sol lap, and above 50,000 km for 83% of the time.
  - A NASA NIAC report gives "5-Sol orbits (~200 × 60,000 km)". That cannot be right: an orbit that size takes about 2 sols. ❌
- **Brightness** (our maths, ⚠️). We assume the ship is about as big and shiny as the ISS. The hybrid ship has 435 kW of solar arrays (NTRS 20160006328), so ISS-scale is a fair guess. Sunlight at Mars is 43% of Earth's (≈ 0.9 mag dimmer).

  | Distance | Brightness |
  |---|---|
  | 1,000 km | about −1 (bright as the brightest stars) |
  | 5,000 km | about +2.6 |
  | 20,000 km | about +5.6 (at the naked-eye limit, and dust takes another ~1 mag) |
  | 112,000 km | about +9.4 (invisible) |

- **The ISS comparison.** NASA: the ISS "appears similar to an airplane or a very bright star moving across the night sky", and sightings happen "within a few hours before or after sunrise or sunset ... as the Sun reflects off the space station and contrasts against the darker sky" (Spot the Station). The same physics works at Mars.

**Verdict**
- Plausible, but only on a low pass: once every 5 sols, for minutes, crossing the sky like the ISS, and only if the low point is near Gale at dusk or dawn.
- The rest of the time the ship is too far to see.

**What the game may say**
- "Once every 5 sols the ship swoops low. At dusk you might spot it: a fast star."
- Kid version: "Most nights our ship is very far away. Some evenings it races overhead."

**What it must not say**
- That you can see the ship every night, or that it hangs still in the sky.
- That NASA says it is visible. This is our estimate.

## 6. Sky 🌌

**What's real**
- **Dust.**
  - Mark Lemmon (Texas A&M, rover camera scientist), Astronomy magazine, Oct 2015: "Typically, stars near the zenith lose nearly 1 magnitude due to dust; that increases to 3 to 4 magnitudes at 15° altitude."
  - Rover cameras have "sensitivities similar to the human eye". They have imaged M31 "(barely)", M42 and the Magellanic Clouds.
  - "Twilight is sometimes very long, such that astronomical imaging needs to be at least two hours away from sunset or sunrise."
  - Stars "would not twinkle" in the thin air.
  - Spirit photographed Orion from Gusev Crater in 2005.
- **Clear seasons.** Spirit's optical depth fell "from near 0.90 to below ~0.3" in the clear season. Opportunity's dropped below ~0.5. Dusty seasons are higher (Lemmon et al. 2015, Icarus).
  - At Gale, the 2018 storm peaked at opacity 8.5 (row 182).
  - Optical depth 0.3 to 0.9 equals 0.3 to 1.0 magnitude of dimming overhead, which matches Lemmon's "nearly 1 magnitude" (our maths).
- **Milky Way.**
  - No rover has photographed it, and no NASA source says "you can see the Milky Way from Mars".
  - Our reading (⚠️): overhead, on a clear-season night more than 2 hours after sunset, it loses about 0.3 to 1 magnitude to dust, like a hazy night at a dark site on Earth. So the bright band is likely visible high in the sky. It fades out toward the horizon and vanishes in a dust storm.
- **Dust devils.**
  - At Gale "whirlwinds usually occur ... without lifting much dust". 214 were seen in the foothills of Mount Sharp (row 176).
  - At Spirit's site "Dust devils are common ... when insolation is high, but are rarer when insolation is seasonally low or low due to dust storms" (Lemmon 2015).
  - In the 2018 storm they "ceased entirely" at Gale (row 182).

**What the game may say**
- "On clear nights the stars don't twinkle."
- "Dust hides stars near the horizon."
- "High overhead you may see a faint Milky Way."
- "Dust devils at Gale are mostly faint swirls; they stop in a dust storm."

**What it must not say**
- That a rover photographed the Milky Way.
- That the Milky Way is brighter on Mars than on Earth's darkest nights.
- That dust devils are big or dangerous at Gale.

---

## Proposed factcheck rows

Numbering continues from row 250. Paths are under `pages/` unless noted.

| # | Claim | Status | Source |
|---|---|---|---|
| 251 | Suited metabolic rates (kJ/h, min / avg / max): Apollo lunar EVA 517 / 1,030 / 2,607; ISS+Shuttle 575 / 950 / 2,320; Advanced Walkback Test 1,767 / 2,505 / 3,167 ("Simulated 10-km ... Lunar surface walk requiring 1 to 2 hours") | ✅ | BVAD Rev2 2022 Table 4-71 (from NASA HIDH 2014), `bvad.txt` |
| 252 | Resting O₂ use "approximately 3.8 mL/kg-min"; "resting in the suit" 6.8 mL•kg-1•min-1 | ✅ | Gernhardt et al. 2013 NASA EVA chapter, `agent-habitat/nasa-gernhardt-eva-ops-2013.txt` |
| 253 | Weir equation in BVAD (3.941 × VO₂ + 1.106 × VCO₂), RQ 0.86, gives ≈ 4.9 kcal per L O₂ ≈ 0.29 g O₂ per kcal | ⚠️ our maths from BVAD Eq. 3-4 | `bvad.txt` §3.3 |
| 254 | 10 km suited walkback vs Apollo: 599 vs 233 kcal/h, O₂ 0.4 vs 0.15 lb/h, cooling water 3.1 vs 0.98 lb/h; 95.8 min at 3.9 mph, RPE 11.8 | ✅ | Norcross, NASA JSC 2007, NTRS 20080014853, `story/ntrs-20080014853-walkback.txt` |
| 255 | Walkback subjects "would have liked to ambulate at higher speeds, but were not able to because of cooling limitations"; NASA assumed 10 km max excursion "based on Apollo program experience" | ✅ | EVA Walkback Test, NTRS 20070016007, `story/ntrs-20070016007-walkback.txt` |
| 256 | Apollo 11 to 14 PLSS: about 1,200 kcal of heat ("400 kcal/hr for three hours, or ... 300 kcal/hr for four hours"); Apollo 15 to 17: 1,800 kcal ("seven hours at ... 250 kcal/hr ... or eight hours at ... 225 kcal/hr") | ✅ | Waligora & Horrigan, Biomedical Results of Apollo, NASA SP-368 (1975), NTRS 19760005584, `story/` |
| 257 | Apollo estimated EVA metabolic rate 3 ways: heart rate (preflight ergometer correlation), O₂ bottle pressure, cooling-water temperatures; "the heart rate method was not used independently"; heart-rate rises on command-module spacewalks "attributed more to excitement than to exercise" | ✅ | same, NTRS 19760005584 |
| 258 | Riding the lunar rover gave the lowest metabolic rates, which reduced "both the use of consumables and the fatigue experienced by crewmen" | ✅ | same, NTRS 19760005584 |
| 259 | Apollo 15 (Jul to Aug 1971): "the oxygen redline limits were approached, indicating that the crew workload was approaching the portable life support system capability" | ✅ | Apollo 15 Mission Report, NTRS 19720021182, `story/` |
| 260 | Apollo EVA heart rates: Apollo 11 average 110 (CDR) and 88 (LMP) bpm; Apollo 15 CDR 92/84/85, LMP 125/107/105 bpm; Apollo 11 LMP reached 170 and 177 bpm during in-flight exercise | ✅ | Apollo 11 Mission Report NTRS 19700008096; Apollo 15 Mission Report NTRS 19720021182 |
| 261 | Two suited subjects in a simulated lunar EVA averaged 56 vs 138 bpm at similar work rates | ⚠️ single small study (thesis chapter on NTRS) | NTRS 20210024108, `story/` |
| 262 | Apollo 15 PLSS battery: 25.7 Ah loaded, 19.3 to 20.7 Ah used on 7 h EVAs, redline 3.1 Ah | ✅ | Apollo 15 Mission Report Table 8-1 |
| 263 | Suit battery use tracks time (fans, pump, radio), while O₂ and cooling track effort | ⚠️ inference | rows 254, 262 |
| 264 | ISS suit battery LLB2: 36.40 Ah, 15.5 to 20.5 V (≈ 650 Wh, our maths); Mars suit moving to "a monolithic battery design" | ✅ (Wh ⚠️) | Russell, NASA JSC 2021, NTRS 20210015449; ICES-2026-126 |
| 265 | Lunar rover: "two 36-volt silver-zinc batteries driving an independent 1/4-hp motor in each wheel" | ✅ | NASA SP-350 ch. 14 app. II, `story/sp350-ch14-8.html` |
| 266 | Apollo: "Mission rules restricted us from going more than 6 miles from the LM - the distance we could walk back in a pinch" | ✅ | NASA SP-350 ch. 14 app. II |
| 267 | DRA 5.0: with one rover, the team must stay "within rescue range": walk back or be reached by a rescue team; two identical rovers are "mutually supporting" | ✅ | DRA 5.0 NASA-SP-2009-566 §5.2.1, `agent-power/` |
| 268 | 30-sol plan: exploration to "about 20 kilometers radius" "Due to limited rescue options"; the unpressurised rover "accompanies the pressurized rover on any extended range traverse" because of suit walking limits | ✅ | SAC21 surface ops HEOMD-415 (2022), `sleep/ntrs-20220000589-sac21-surface-ops.txt` |
| 269 | The crew sleeps in the pressurised rover on trips ("preparing the PR for an overnight stay") and lives in it all mission; it stows up to 14 sols of logistics for two | ✅ | SAC21 surface ops; Chappell 2022 |
| 270 | Pressurised rover: 5,193 kg with 60 kWh; 200 kWh chosen for 5-sol trips; 8 km/h; hotel load 1.85 kW; 3 kW net recharge from the 10 kW FSP; 48 h recharge; 20 km drive-back reserve always kept | ✅ | Chappell et al. IEEE 2022, NTRS 20210022250 + 20220003043, `story/` |
| 271 | Rover energy ≈ 0.8 kWh/km driving + 0.23 kWh/km life support ≈ 1 kWh/km; cabin alone 45.6 kWh per sol | ⚠️ our maths from row 270 (checks against Chappell's 24 km / 13.65 h case) | |
| 272 | SAC21 assumes "no on-board capability to replenish stored energy – such as solar arrays" (Chappell models an optional 3.5 kW panel) | ✅ | SAC21 surface ops; Chappell 2022 Table 1 |
| 273 | After launch the crew "spends the next 2.5 sols flying to the DST", which waits in a 5-sol orbit | ✅ | Chappell 2022; SAC21 surface ops |
| 274 | A NASA hybrid-ship design captures "at 250 km altitude" into a "5-sol parking orbit with its periapse directly above the Jezero crater" | ✅ | AAS 19-225, NTRS 20200002738, `story/` |
| 275 | 5-sol orbit with a 250 km low point reaches about 112,500 km at its high point; 4.8 km/s low, 0.15 km/s high; below 5,000 km for about 85 min per lap | ⚠️ our maths (method checks against DRA 5.0's 1-sol 250 × 33,793 km) | |
| 276 | "5-Sol orbits (~200 × 60,000 km)" | ❌ an orbit that size has a period of about 2 sols | NIAC FY16, NTRS 20170002795 |
| 277 | An ISS-sized ship at Mars: about mag −1 at 1,000 km, +2.6 at 5,000 km, +9.4 at 112,000 km; so it is visible only on low passes, at twilight | ⚠️ our maths | Spot the Station (ISS seen near sunrise or sunset), `story/nasa-spot-the-station.html` |
| 278 | Mars night sky: stars overhead "lose nearly 1 magnitude due to dust", "3 to 4 magnitudes at 15° altitude"; astronomy needs "at least two hours away from sunset or sunrise"; rovers imaged M31 (barely), M42, Magellanic Clouds; Spirit imaged Orion (2005) | ✅ (expert, magazine) | Mark Lemmon, Astronomy Oct 2015, `story/astronomy-2015-mars-night-sky.html` |
| 279 | Clear-season optical depth: Spirit "below ~0.3", Opportunity below ~0.5; dust devils "common ... when insolation is high" | ✅ | Lemmon et al. 2015 Icarus (arXiv 1403.4234), `story/` |
| 280 | Milky Way likely visible high in a clear night sky on Mars; no rover image of it exists | ⚠️ inference from rows 278 and 279 | |
