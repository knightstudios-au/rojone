# Rojone concept: asset manifest

Every image used by the two artboards, referenced from the source as `/_blob/<id>`.

Originals were extracted from the client's own mockup files (`Rojone_Homepage_Preview.html`,
`Rojone_Category_Preview.html`), then resized and compressed. Roughly 10MB down to 457KB.

**Note (2 November 2026):** the original design canvas (https://claude.ai/artifact/1J1NY6ZLJyqoAMJP2TxDKb)
can no longer be read, so its asset store is gone. The images survive inside the deployable builds
in `claude/build/`, which carry every image as a base64 data URI. `build-static-export.py` now looks
for each asset as `assets/<blob id>.<ext>`, so recovering the folder means decoding the data URIs from
the build and saving each under its blob id (the source's `/_blob/` order matches the build's `<img>` order).

## Brand

| Blob id | File | Used for |
|---|---|---|
| `0dd5b61fc6ec6dd7ea94adf1413a7cdb` | logo-rojone.png | Header logo, red diamond and black wordmark |
| `bad678488f8685c65015f48d6c476ef6` | logo-rojone-reversed.png | Footer logo, white wordmark on navy, red diamond kept |

## Hero and banner art (transparent PNG, sits on tinted panels)

| Blob id | File | Used for |
|---|---|---|
| `7381e0c42606bcc2b1b39a05a652d33d` | hero-art.png | Homepage hero watermark, 13% opacity, centred |
| `2f3807a1e642b2501e87d469667d5c85` | banner-adapters.png | Category page banner art |

Earlier white-matted JPEG versions (`7961d82d019aa05796d3878ae3800f4d` hero-art.jpg) are superseded.
They showed a visible white box against the tinted panel.

## Shop by category tiles

| Blob id | File | Category |
|---|---|---|
| `c95cbfd6fe8726a2c01a89fd45b8d8af` | cat-antennas.jpg | Antennas |
| `ecc89a2249b2c08b5b763f3bf0621295` | cat-adapters.jpg | Adaptors |
| `d5ffee3d587c5dd4d94a0f2cbbe9caa3` | cat-cables.jpg | Cable Assemblies |
| `4cb05d0217064e5c58069ae47622f1ba` | cat-gps.jpg | GPS Products |
| `c3827a4f6f418ccbc18bdcab9d4ceb73` | cat-fibre.jpg | Fibre Optic |
| `94fc406e6a0f4121bc5c968e0fdab58f` | cat-tooling.jpg | Tooling |

## Category page product shots

| Blob id | File | Products |
|---|---|---|
| `d10457fe33226b1dd000c661350acb74` | prod-bulkhead.jpg | RJ-SMA-1421, RJ-SMA-1477 |
| `3c7c4442ecf0f073b7438cd12ec219d7` | prod-gold-sma.jpg | RJ-NM-2210, RJ-UHF-5502 |
| `e462e1506708aa36bf96d7477e53c71a` | prod-nf-barrel.jpg | RJ-BNC-0087 |
| `971724b34ffcbdf4241477bf0117f641` | prod-silver-ad.jpg | RJ-TNC-3305 |

Four unique photos across six demo SKUs, two reused, matching the client's own mockup.

## Homepage popular products

| Blob id | File | Product |
|---|---|---|
| `1c1e6ba23a292293bd6d8f446b8fa018` | pop-yagi.jpg | Hand-held Quick Fold Yagi Array |
| `07b027613654fde6d9d941a07686edc2` | pop-pigtail.jpg | Pigtail MMT Right Angle Female Cable |
| `6741160be63b00aaa750d3c2c345fc5c` | pop-socket.jpg | Size 1 Socket Coaxial Contact |
| `29747c48705d1ca79db8e5ad83a893dd` | pop-ssmc.jpg | SSMC Straight Jack Male, Gold |
| `5ea84b30af13255f8769a164956cc1bb` | pop-positioner.jpg | 615179 Positioner SK2/2 |

Added 2 November 2026 (client round 2 asked for ten popular products). Cropped from the category
tile photos above and padded to 300px white squares.

| Blob id | Cropped from | Product |
|---|---|---|
| `53df0f7739bbf4b12429cc23fb408aa8` | cat-antennas.jpg | Magnetic Mount Whip Antenna |
| `22b06095f2ee744bc9d1ea2ccbd442c4` | cat-adapters.jpg | SMA Male to SMA Female Adaptor, Gold |
| `cc042e7240677fe1cd333e7600261cc6` | cat-cables.jpg | Coaxial Cable Assembly, Male to Male |
| `d3b3d952f074233590e7f768b16cf9d6` | cat-fibre.jpg | LC to LC Duplex Fibre Patch Lead |
| `75aa6d14d891bc9e13d8fd2fe81fc2c9` | cat-tooling.jpg | Ratchet Crimp Tool |

These five are placeholders made from existing client imagery. Swap in real product shots when the
client supplies them.

## Manufacturer logos

Filenames are historical and do not match the brands. The `alt` text in the client's mockup is
offset by one image, which caused the original mislabelling. The brand column below was verified
visually and is correct.

| Blob id | File | Actual brand |
|---|---|---|
| `fb360c93b8dddccfb8021954572fe7c0` | mf-commscope.png | Cooper Antennas |
| `17745e5738e519119cb82287a6f7c10c` | mf-radiall.png | RFS |
| `d3d0126217c3f3123b4ddcd79aa2e837` | mf-times.png | Spinner |
| `e85c65ce5abd6356b1a54ad9df77956b` | mf-amphenol.png | Astro Tool |
| `de1a8b63580f8faaa33f230c2054b738` | mf-pasternack.png | Radiall |
| `5f789481086a534eebd31ae86bc9c1a1` | mf-lcom.png | MilesTek |
| `e4035b24c0fd5ece7f534445d9d138bb` | mf-fischer.png | Freelin-Wade |
| `c2d9f26283782dbf98fdd9768801ebbe` | mf-fairview.png | Fairview Microwave |

The client's mockups carried 26 manufacturer logos in total. The remaining 18 (including Amphenol
Nexus, Pasternack, L-com, Fischer, Times Microwave, CommScope, Satel, Sinclair, Mobile Mark,
Optical Zonu, Nextek, Shireen, Konnect RF, IW, Spinner Group) were not uploaded and can be pulled
from the original mockup files. Now that the strip scrolls, adding them costs no layout space.
