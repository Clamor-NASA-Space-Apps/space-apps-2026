# Outpost Gale in Godot: what we need and what we can have 🚀

Written 10 November 2026, for the team and for the agents that build on 14 and 15 November 2026. Every claim here is in the fact-check table in [references.md](references.md).

> [!TIP]
> **30-second version.** We are building a Mars outpost game for kids aged 7 to 12, set in Gale crater, played in a browser. The new direction is third person, a real-looking Mars, on a phone or a laptop, made in Godot 4.7. Godot's web build has one renderer, so "realistic" means good light, real colours, real terrain shape and a well animated astronaut. It does not mean ray tracing, volumetric dust or reflections. The engine is a 38 MB download before our game adds a byte. The one asset we do not have yet is an astronaut with real walk and run animations.

---

## 1. What are we building 🎯 ?

Three sources agree on the core, and one new decision changes the look.

1. **The brief** ([challenge.txt](../junior-astronaut/challenge.txt)): kids aged 7 to 12 run a Moon or Mars outpost. They make real decisions about life support, radiation shielding, power, food and communication delay. No choice is free. Two or three core resources. Real NASA data, credited inside the game. Playable in a browser with no login.
2. **The author's video** ([video-subtitles.txt](../junior-astronaut/video-subtitles.txt)): "Not a quiz, not a slideshow, a living simulation where every choice costs something." His example is a dust storm and a ten-second choice about solar panels.
3. **Our plan** ([plan.md](../../plan.md), "The game"): Outpost Gale. 30 sols in Gale crater, three meters (Power, Life support, Crew health), a seeded event deck (dust storm, solar storm, ask Earth, dirty panels), a 60-second intro, and a replay of the three choices that lost the mission.
4. **The new direction** (Ravindu, 10 November 2026): third person, realistic, walk and run, a rover, a rocket, solar panels to set up, plants to grow, playable on a mid-range phone or a computer. Engine: Godot, exported to the web.

> [!WARNING]
> The plan describes a management game seen from above. The new direction is a third-person explorer. Both can be the same game, but the brief warns: "Don't let visual polish substitute for mechanical accuracy". Walking around must be how the player makes the trade-offs, not a second game beside them. This is a team decision, listed in section 5.

**Kid version:** you are the commander of a small base on Mars. You walk around it, fix things, and choose what to spend power on. Every choice has a price.

---

## 2. Facts to remember 🧠

| Fact | Value | How we know |
|---|---|---|
| Renderer in a web build | Compatibility (WebGL 2.0) only | Godot docs |
| Not available there | volumetric fog, screen-space reflections, real-time global illumination, decals, particle trails, most anti-aliasing | Godot docs |
| Available there | sky shaders, depth and height fog, glow, simple ambient occlusion, shadows, baked lightmaps, GPU particles | Godot docs |
| Engine download | 38 MB, about 9.7 MB when the host compresses it | measured, 10 November 2026 |
| Languages | GDScript only: C# cannot be exported to the web | Godot docs |
| Physics | Jolt, and it runs in the web build | docs, and measured |
| Web builds need | https or localhost | seen on our laptop |
| Model files | Godot 4.7 cannot read Draco, meshopt or quantized GLBs. Five of our six NASA models are Draco | measured |
| Astronaut with animation | not on disk. Best CC0 candidate found: Quaternius "Astronaut" | checked, see [assets.md](assets.md) |
| Real walking speed in a suit | about 1 m/s on the Moon. No measured Mars number exists | Apollo journal |
| Real rover speed | Perseverance 152 m per hour. NASA's crewed rover concept about 10 km/h | NASA |
| Mars sky | orange or reddish by day, blue-grey around the setting Sun | NASA |

---

## 3. What the scene needs, and where it comes from 🏜️

| Thing on screen | How in Godot's web build | Asset source | Status |
|---|---|---|---|
| Ground | a heightmap mesh in chunks, collision from the same heights | real Gale elevation data (USGS, CC0), or the small landing-site mesh already on disk | data not downloaded |
| Ground surface | one tiling rock and sand texture, tinted | Poly Haven, CC0, 1.7 to 3.5 MB per set at 1k | not downloaded |
| Sky and sol cycle | the built-in physical sky with a red tint, animated sun | none needed | ready |
| Sun and shadows | one sun with shadows | none needed | ready, with a brightness trap ([engine-limits.md](engine-limits.md)) |
| Dust storm | fog colour and depth, dimmer and redder sun, particles | none needed | ready |
| Mount Sharp and the rim | a low far mesh or painted backdrop | from the same elevation data | to make on the day |
| Habitat, tanks, dishes, rocket parts | kit models | Kenney Space Kit, CC0, on disk | ready |
| Solar panels | kit models | Quaternius Ultimate Space Kit, CC0 | not downloaded |
| Rover | kit model, or the real one | Kenney or Quaternius rover; NASA Perseverance (199,521 triangles, needs cutting down) | on disk |
| Astronaut | rigged model with walk, run, idle clips | Quaternius "Astronaut", CC0 | **not downloaded, clips unverified** |
| Greenhouse plants | simple models that grow in steps | Quaternius crops (needs conversion), or made on the day | open |
| Sound | wind and rover clips | NASA Perseverance recordings; Kenney sound packs on disk | NASA clips not downloaded |

Details and licences are in [assets.md](assets.md).

---

## 4. The other pages 📚

- [engine-limits.md](engine-limits.md): what Godot gives a web game on a phone, and the budgets that follow.
- [assets.md](assets.md): what is on disk, what is missing, which licences are safe for a public repo.
- [movement-and-look.md](movement-and-look.md): real numbers for walking, jumping and driving on Mars, and what Gale crater looks like.
- [document-check.md](document-check.md): the unverified "Building a Gale Crater Mars Survival Game" document, claim by claim.
- [references.md](references.md): every source, and the fact-check table.

---

## 5. Decisions for the team ⚖️

1. **Explorer or manager?** How does walking around serve the three meters? One option: every action needs you to be somewhere (clean a panel, switch a machine, reach the shelter), and time outside costs radiation dose.
2. **How real is "realistic"?** The factory's design language recolours every model to a few flat material roles. A photo-textured rover beside flat-coloured kit domes will clash. Pick one: stylised and consistent, or textured with a new rule for mixing.
3. **The astronaut.** Download and inspect the Quaternius model before 14 November 2026. If its clips disappoint, the fallback is a Kenney Mini Character (on disk, 32 clips) with a helmet attached.
4. **Size budget.** The old budget was 15 MB of assets and a first frame in 3 seconds. The engine alone is 9.7 MB compressed. Decide a new budget for our own data and a host that compresses files.
5. **Phones.** Nothing here has run on a real phone yet. One test on the weakest team phone, before 14 November 2026, tells us more than any page.

## What I could not reach
- The Docmost page "Game design and story" and its "Decisions for the team" section were not read for this write-up. If they differ from `plan.md`, they win.
- Frame rate on a real phone: not measured.
- The clip list of the Quaternius astronaut: not on any page, needs the download.
