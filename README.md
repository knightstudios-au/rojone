# Rojone B2B site concept

Static design concept for Rojone Pty Ltd, deployed on Netlify from this repo.

- `site/` is what Netlify publishes (`netlify.toml` sets this). Self-contained HTML, images inlined.
- `source/` holds the artboard sources (`Main.dc.html`, `Category.dc.html`). Edit these, never `site/`.
- `assets/` holds every image, named by blob id. See `rojone-asset-manifest.md`.
- `build-static-export.py` rebuilds `site/` from `source/` + `assets/`:

      python3 build-static-export.py              # homepage
      python3 build-static-export.py --category   # homepage + category page

Change history and open questions: `rojone-handover-round2.md`.
