# NASA Space Apps 2026: Junior Astronaut Mission Trainer (team workspace)

This is the planning and research workspace. The factory (`tooling/`) is a submodule; the game is its own repo, cloned into `tooling/projects/`.

## Get started (Windows, macOS or Linux)
On Windows, first turn on Developer Mode (Settings, System, For developers), so git can make the few symlinks the factory uses. Then, in any terminal (PowerShell, cmd, Git Bash):

```
git clone --recurse-submodules -c core.symlinks=true https://github.com/Clamor-NASA-Space-Apps/space-apps-2026.git
git -C space-apps-2026/tooling switch godot
git clone https://github.com/Clamor-NASA-Space-Apps/outpost-gale.git space-apps-2026/tooling/projects/junior-astronaut-mission-trainer
```

Then `cd space-apps-2026/tooling` (or into the game folder) and run `claude`. Not in git, so copy them by hand: `.env.local` (the api.nasa.gov key, never commit it). To open the game, use Godot 4.7.2 (standard, not .NET). The factory's checks (`tools/*.mjs`) need Linux; on Windows, play, edit and run Claude.

To update later: `git pull --recurse-submodules`, then `git -C tooling/projects/junior-astronaut-mission-trainer pull`.

| Path | What it is |
|---|---|
| `plan.md` | The full plan: research, tooling, rehearsal, design pack, hackathon runbook |
| `roadmap.md` | Checklist of every subtask, ticked as we go |
| `research/junior-astronaut/` | Saved sources (`pages/`), `sources.md`, `factcheck.md` (56 claims), challenge text, video transcript |
| `assets-cache/` | Downloaded NASA models and textures, Kenney CC0 kits and sounds, data snapshots, `CREDITS.md` |
| `*.pdf` | Reference papers |

Repos (GitHub org Clamor-NASA-Space-Apps, mirrored to our Gitea):
- `space-apps-2026`: this workspace.
- `agent-forge-3d`: generic tooling (Blender asset forge, test hooks, design language). The submodule `tooling/`, branch `godot`.
- `outpost-gale`: the game, cloned into `tooling/projects/junior-astronaut-mission-trainer/`.
- `one-night-stray`: the rehearsal game (throwaway), on Gitea only.

The team-facing write-up lives in Docmost, in the `NASA` space.
