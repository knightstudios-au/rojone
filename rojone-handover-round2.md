
## Client round 2 changes (2 November 2026)

Five pieces of client feedback, applied to the homepage source and build.

1. **Category nav on one line.** The bar wrapped "Headsets" onto a second row. Items now sit on a single row (`flex-wrap:nowrap`, spaced across the full width, 12px labels at .02em tracking). Verified one row at 1440, 1280 and 1200px; below 1180px the existing collapse to "All products" still applies.
2. **Utility strip sentence removed.** "Australian owned & operated · Stock shipped from Ingleburn NSW" is gone; the phone, locale and currency cluster now right-aligns at every width. The hero eyebrow still says "Australian owned & operated", so the message is not lost.
3. **Hero art centred.** The watermark was pinned to the right edge and cropped on narrow screens. It is now centred in the hero (`left:50%`, `translate(-50%,-50%)`, max 90% wide) with equal margins at every width.
4. **Manufacturer strip scrolls.** The client said "we like that it scrolls instead of staying fixed", read as a request for a scrolling strip. Logos now loop continuously (32s), pause on hover, and stop for visitors with reduced motion turned on. A few lines of script clone the logo set for the seamless loop, so logos are embedded once (keeps `index.html` near 609KB instead of ~810KB). If the client meant something else, revert section `.mfrow`.
5. **Ten popular products.** Five added (whip antenna, SMA adaptor, coax assembly, LC fibre lead, crimp tool) with placeholder photos cropped from the category tiles; see the asset manifest. Grid is 5 columns on desktop and 2 columns from 1080px down, so ten always fills complete rows.

Also swept the last em dash ("Custom-built solutions & kits" card) to a colon.

**Category page.** Items 1 and 2 (one-line nav, sentence removed) are applied there too. Its source was recovered from a browser-saved copy of the live page, with links mapped back to the originals and every embedded image checked against the asset folder.

The homepage source in `claude/source/Main.dc.html` was reconstructed from the deployed build, since the canvas could not be read. Content is the same; only whitespace differs.
