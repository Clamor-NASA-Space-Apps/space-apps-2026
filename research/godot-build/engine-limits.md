# What Godot gives a web game on a phone ⚙️

Godot 4.7.2, the engine we installed on 10 November 2026. "Docs" means the official Godot 4.7 documentation, saved under `pages/agent-2/`. "Measured" means we ran it on our laptop that day.

> [!TIP]
> **TL;DR.** One renderer, one thread, and a 38 MB engine. Inside that: a real sky, fog, shadows, glow and particles all work. Plan for one shadowed light, baked or simple lighting, and few draw calls.

---

## 1. The three fixed choices 🔒

1. **Compatibility renderer.** The docs: "Godot 4 can only target WebGL 2.0 (using the Compatibility rendering method). Forward+/Mobile are not supported on the web platform". So we build and judge the look in Compatibility from the first hour.
2. **GDScript only.** The docs: "Projects written in C# using Godot 4 currently cannot be exported to the web."
3. **Single-threaded export.** The docs call it "the preferred and now default way to export your games on the Web". It runs on any static host. The threaded build needs special server headers.

A native addon (a "GDExtension", code compiled for one platform) needs its own web build and those same headers. Treat native addons as unavailable.

---

## 2. What the renderer has, and what it lacks 🎨

| Wanted for a real-looking Mars | In a web build? | Use instead |
|---|---|---|
| Sky with a sol cycle (physical sky, sky shaders) | yes | |
| Fog by distance and by height | yes | this is the dust haze |
| Volumetric fog (light shafts in dust) | no | fog colour, plus flat transparent quads |
| Shadows from the sun and from lamps | yes | keep to one or two shadowed lights |
| Glow | yes, a simpler version | |
| Ambient occlusion (soft contact shadows) | yes since 4.6, simplified | |
| Screen-space reflections | no | a reflection probe (2 per mesh) |
| Real-time global illumination (SDFGI, VoxelGI) | no | baked lightmaps, or ambient light |
| Decals (tracks, scorch marks) | no | flat sprites on the ground |
| GPU particles | yes | no trails, no sub-emitters |
| Anti-aliasing | MSAA only | 2x MSAA or none on phones |
| HDR | no | colours are stored as 8-bit sRGB |
| Many lights | 8 omni and 8 spot lights per mesh | |
| Automatic instancing of repeated models | no | MultiMesh for rocks and panels |
| Occlusion culling | not in the official web templates | fog, and distance-based hiding |

**Kid version:** the phone can draw a red sky, a hazy horizon, shadows and blowing dust. It cannot draw mirror reflections or glowing beams in the dust.

> [!WARNING]
> In this renderer a light with shadows is added in a different colour space and comes out much brighter. We measured it: one sun plus ambient light was 2.2 times too bright on flat ground. The factory's light rig now corrects its sun. Any extra shadowed light needs its brightness cut by eye.

---

## 3. Physics and movement 🧲

- Jolt is the default 3D physics engine for new projects since Godot 4.6, and the 4.6 release notes "remove the experimental label".
- A `project.godot` written by hand gets the older Godot Physics unless it names Jolt. The factory's project template names it.
- Measured: a ball dropped in a web build came to rest at the same height (0.484 m) as in the native run, with Jolt in both.
- Terrain collision: `HeightMapShape3D` is "faster to check collisions against" than a triangle mesh, but its grid points are 1 unit apart and it cannot do overhangs. There is no built-in terrain node. The visible ground is a mesh we generate, cut into chunks.

---

## 4. The download 📦

| Part | Size | Note |
|---|---|---|
| Engine (`index.wasm` + `index.js`) | 38 MB | fixed, before any game data |
| Whole empty build, gzip | 9.7 MB | what a compressing host sends |
| Game data (`index.pck`) | ours to budget | models, textures, sound, scripts |

- The docs say the engine compresses "down to around a quarter of its original size with gzip". Our number matches.
- GitHub Pages compresses files. The docs say itch.io and GitLab Pages do not.
- Engine start on our laptop, from a local server: about 0.65 seconds. A phone on venue Wi-Fi will be slower. Not measured.
- A smaller engine is possible by compiling our own export template with unused features off. The docs give no number, and it costs build time we may not have.

---

## 5. Phone checklist 📱

1. **Textures for phones.** Web presets ship desktop texture formats by default. Turn on "For Mobile" in the web preset and `import_etc2_astc` in the project. The factory's template does both.
2. **"Is this a phone?"** In a phone browser `OS.has_feature("mobile")` is false. Ask for `web_android` or `web_ios`. So the engine's `.mobile` setting overrides do not apply either: set shadow sizes ourselves.
3. **Touch controls.** Godot 4.7 has a built-in `VirtualJoystick` node. Every control must be an input action, so keys and touch feed the same code.
4. **Sound and full screen** only start after the player taps or presses a key. The first screen needs a "Start" button anyway.
5. **Safari.** The docs: "Safari has several issues with WebGL 2.0 support that other browsers don't have". Test on an iPhone if a judge may use one.
6. **Texture size.** Mobile GPUs are "typically limited to 4096×4096 textures".
7. **Testing on a phone.** A web build only runs on https or localhost. Plug the phone in and run `adb reverse tcp:5188 tcp:5188`, then open `localhost:5188` on the phone.

---

## 6. Budgets we can defend 📏

The docs give no numbers for draw calls or triangles ("not found"). These are the limits they do give, plus what we measured.

| Budget | Value | Source |
|---|---|---|
| Shadowed lights on screen | 1 or 2 | docs: "only have a handful of lights with shadows" |
| Lights touching one mesh | at most 8 omni and 8 spot | docs |
| Reflection probes per mesh | 2 | docs |
| Largest texture | 4096 px, and smaller is safer | docs |
| Draw calls | no official number. Keep the old 150 until a phone says otherwise | our old budget, unverified for Godot |
| Game data | to be decided, see README section 5 | |

## Open questions ❓
- Frame rate of a third-person scene on our weakest phone.
- Whether baking lightmaps is fast enough on a laptop with integrated graphics. The docs say baking wants a dedicated GPU.
