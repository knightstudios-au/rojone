# Rojone B2B site concept

Static design concept for Rojone Pty Ltd, deployed on Netlify from this repo.

- `site/` is what Netlify publishes (`netlify.toml` sets this). Self-contained HTML, images inlined.
- `source/` holds the artboard sources (`Main.dc.html`, `Category.dc.html`, `Product.dc.html`, `About.dc.html`, `Manufacturer.dc.html`). Edit these, never `site/`.
- `assets/` holds every image, named by blob id. See `rojone-asset-manifest.md`.
- `build-static-export.py` rebuilds `site/` from `source/` + `assets/`:

      python3 build-static-export.py

  It builds every artboard it finds in `source/`, rewrites the cross-page links to clean URLs
  (`/`, `/category`, `/product`, `/about`, `/radiall`) and reports the byte size and any unresolved
  references.

`Manufacturer.dc.html` is the brand page template, built out with Radiall as the worked example.

The artboards are also editable as a Claude Design canvas:
https://claude.ai/artifact/1J1NY6ZLJyqoAMJP2TxDKb

Keep the canvas and this repo in step. They are the same five files; if they drift, recovering the
difference is slow. Change history, design decisions and open client questions live in the
"Client: Rojone" project under `claude/rojone-handover.md`.
