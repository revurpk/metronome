# 🪘 Tala Metronome

A free, **single-page, offline-capable** metronome for **South Indian Carnatic talas** and
**North Indian Hindustani taals** — with hand-gesture and *bol* guidance for both novice students
and accompanying musicians.

No build step, no dependencies, no tracking. Just open `index.html`.

## Features

- **Carnatic** — the 7 Suladi Sapta Talas (Dhruva, Matya, Rupaka, Jhampa, Triputa, Ata, Eka) across all
  5 *jatis*, plus the *chapu* talas (Misra, Khanda, Tisra, Sankirna). Adi tala preset.
- **Hindustani** — Teentaal, Ektaal, Jhaptaal, Rupak, Keherwa, Dadra, Chautaal, Dhamar, Tilwada, Deepchandi,
  each with its correct *theka* (bols) and *sam / tali / khali* markers.
- **Accurate timing** — sample-accurate scheduling via the Web Audio API (lookahead scheduler), not `setInterval`.
- **Gati / nadai subdivisions** (tisra, chatusra, khanda, misra…) you can hear and drill.
- **Visual avartana** — every beat shown as a box grouped into angas/vibhags, with the live beat highlighted.
- **Gesture coaching** — tells you when to *clap*, *finger-count* or *wave* (Carnatic) / *tali* vs *khali* (Hindustani).
- **Tap tempo, tempo trainer** (auto-increase BPM every N cycles), count-in, accent toggle, volume.
- **Keyboard**: `Space` start/stop, `↑ / ↓` tempo.

## Run locally

Open `index.html` in any modern browser — that's it. Or serve it:

```bash
python -m http.server 8000   # then visit http://localhost:8000
```

## Deploy to GitHub Pages

This repo ships a minimal **build-free** workflow at
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) that publishes the repository root.

1. Push this repository to GitHub.
2. In **Settings → Pages**, set **Source = GitHub Actions**.
3. Push to `main` (or run the workflow manually via *Actions → Deploy to GitHub Pages → Run workflow*).

Your site goes live at `https://<user>.github.io/<repo>/`. The `.nojekyll` file ensures the static files
are served verbatim.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The entire app (HTML + CSS + JS, self-contained) |
| `icon.svg` | App icon / apple-touch-icon (tabla + mridangam) |
| `favicon.svg` | Favicon (mridangam) |
| `.github/workflows/deploy.yml` | GitHub Pages deploy workflow |
| `.nojekyll` | Disables Jekyll processing on Pages |

## Audio on iOS / Lockdown Mode

The metronome uses the Web Audio API for sample-accurate timing. **iOS Lockdown Mode disables Web Audio
entirely** (and blocks programmatic per-click playback), so for that case the app has a second engine:
it renders the *whole tala cycle* into a single `<audio>` element and loops it natively, started directly
by your tap on **Start** — the one kind of audio playback Lockdown Mode allows. The visual highlight is
then driven from the audio element's own clock.

If you hear nothing on iOS, tick **“Compatibility sound (iOS Lockdown)”** (this forces the looped engine
and must be set *before* pressing Start), and make sure the ring/silent switch is off (iOS routes `<audio>`
through it). Alternatively, you can exclude the page from Lockdown Mode in Safari's **aA** menu to restore
full Web Audio. The footer shows the build id and which audio engine is active, for troubleshooting.

## Notes on authenticity

Theka bols and tala structures follow standard pedagogy. Regional *gharana* and school variations exist
(especially in chapu groupings and theka fillers) — treat this as a practice reference, not a single
canonical authority. Contributions/corrections welcome.

## License

MIT — use it, fork it, teach with it. 🙏
