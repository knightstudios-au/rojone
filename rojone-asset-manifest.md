# Rojone concept: asset manifest

Every image used by the five artboards. Files in `assets/` are named by blob id, which is how the
artboards reference them (`/_blob/<id>`) and how `build-static-export.py` resolves them. The same
ids address the Claude Design asset store at https://claude.ai/artifact/1J1NY6ZLJyqoAMJP2TxDKb.

Originals were extracted from the client's own mockup files (`Rojone_Homepage_Preview.html`,
`Rojone_Category_Preview.html`), then resized and compressed. Roughly 10MB down to about 510KB.

## Brand

| Blob id | Used for |
|---|---|
| `0dd5b61fc6ec6dd7ea94adf1413a7cdb` | Header logo, red diamond and black wordmark |
| `bad678488f8685c65015f48d6c476ef6` | Footer logo, white wordmark on navy |

## Hero and banner art (transparent PNG, sits on tinted panels)

| Blob id | Used for |
|---|---|
| `7381e0c42606bcc2b1b39a05a652d33d` | Homepage hero watermark, centred, 13% opacity |
| `2f3807a1e642b2501e87d469667d5c85` | Category page banner art |

## Shop by category tiles

| Blob id | Category |
|---|---|
| `c95cbfd6fe8726a2c01a89fd45b8d8af` | Antennas |
| `ecc89a2249b2c08b5b763f3bf0621295` | Adaptors |
| `d5ffee3d587c5dd4d94a0f2cbbe9caa3` | Cable Assemblies |
| `4cb05d0217064e5c58069ae47622f1ba` | GPS Products |
| `c3827a4f6f418ccbc18bdcab9d4ceb73` | Fibre Optic |
| `94fc406e6a0f4121bc5c968e0fdab58f` | Tooling |

## Category and product page shots

| Blob id | Products |
|---|---|
| `d10457fe33226b1dd000c661350acb74` | RJ-SMA-1421, RJ-SMA-1477, product page main image |
| `3c7c4442ecf0f073b7438cd12ec219d7` | RJ-NM-2210, RJ-UHF-5502, product page thumbnail |
| `e462e1506708aa36bf96d7477e53c71a` | RJ-BNC-0087, product page thumbnail |
| `971724b34ffcbdf4241477bf0117f641` | RJ-TNC-3305, product page thumbnail |

Four unique photos across six demo SKUs, two reused, matching the client's own mockup.

## Homepage popular products

The first five came straight from the client's mockup. The second five were cut from the full
resolution category tile artwork in the same mockup, isolated on their alpha channel, cropped to
the subject and re-optimised as transparent PNGs at 320px on the long side.

| Blob id | Product |
|---|---|
| `1c1e6ba23a292293bd6d8f446b8fa018` | Hand-held Quick Fold Yagi Array |
| `07b027613654fde6d9d941a07686edc2` | Pigtail MMT Right Angle Female Cable |
| `6741160be63b00aaa750d3c2c345fc5c` | Size 1 Socket Coaxial Contact |
| `29747c48705d1ca79db8e5ad83a893dd` | SSMC Straight Jack Male, Gold |
| `5ea84b30af13255f8769a164956cc1bb` | 615179 Positioner SK2/2 |
| `c14b411054b63cf5ba1368da465a9388` | Magnetic Mount Whip Antenna |
| `f76356a0d9ac4f29a3a2f48c261441fa` | SMA Male to SMA Female Adaptor, Gold |
| `eb4dd2b587699ae9910309775bab050c` | Coaxial Cable Assembly, Male to Male |
| `6ecefea7cbdcb2f43fad59ef36cfecc2` | LC to LC Duplex Fibre Patch Lead |
| `b7ebd0f34bec7d83991a5c48b051d434` | Ratchet Crimp Tool |

## Manufacturer logos

The `alt` text in the client's mockup is offset by one image, which caused an early mislabelling.
The brands below were verified visually and are correct.

| Blob id | Brand |
|---|---|
| `fb360c93b8dddccfb8021954572fe7c0` | Cooper Antennas |
| `17745e5738e519119cb82287a6f7c10c` | RFS |
| `d3d0126217c3f3123b4ddcd79aa2e837` | Spinner |
| `e85c65ce5abd6356b1a54ad9df77956b` | Astro Tool |
| `de1a8b63580f8faaa33f230c2054b738` | Radiall |
| `5f789481086a534eebd31ae86bc9c1a1` | MilesTek |
| `e4035b24c0fd5ece7f534445d9d138bb` | Freelin-Wade |
| `c2d9f26283782dbf98fdd9768801ebbe` | Fairview Microwave |

These eight run as a scrolling marquee, duplicated at runtime by a short script in the page, so the
strip reads as continuous without more logos being uploaded.

The client's mockups carried 26 manufacturer logos in total. The remaining 18 (including Amphenol
Nexus, Pasternack, L-com, Fischer, Times Microwave, CommScope, Satel, Sinclair, Mobile Mark,
Optical Zonu, Nextek, Shireen, Konnect RF, IW, Spinner Group) can be pulled from the original
mockup files if the strip needs expanding.

## Radiall manufacturer page

Cut from the client's 9 November `Rojone-Radiall.html` concept, which carried them as base64, then
resized to 260px on the long side and re-optimised as transparent PNGs.

| Blob id | Range |
|---|---|
| `bd0a475d418cfc33d865a873760864b4` | Radiall brand logo |
| `76c6883876f2588ac6ab294c8a52f3cf` | IMP |
| `5162901d5ceeebca19563065ce769886` | TestPro |
| `6f19b497899f035696c5f4cebbc0f30c` | SHF (shows the AEP brand mark, not a part) |
| `9bb1292a5f61ec40ea7a86b94ac70ee4` | EPX |
| `804678af1999650b26cd60f3a85129bc` | OCTIS |
| `11b298109f12ac6cf090a559d86f5258` | D-Lightsys |
| `db5e977c6aa5f073f8891675e14937ad` | ORBIX |
| `4286ed3fec6fcf5d16e9ba8733979fb7` | Armadillo |
| `3306cc797e5b15d5a87b1d29bf9c24e4` | Cryonium |
| `85f064339e93ca9a379a0935c3458440` | COAXIPACK 2 |
| `aac645776c9215c9fe738f297a6eb14c` | CoaxHD70 |
| `1b9dd7e3e5f0c828506bc376c13a3911` | F2C-40 |

The remaining 44 Radiall ranges are listed in the page's full range index without images. Their
source artwork sits in the client's concept file if images are wanted later.

The About Us page reuses the hero watermark (`7381e0c42606bcc2b1b39a05a652d33d`) and adds no assets
of its own.

The A-Z manufacturer index is not built: it needs 25 brand logo files that were not supplied.

## Superseded files

Five earlier popular-product crops are still present in `assets/` but are no longer referenced by
any artboard: `22b06095f2ee744bc9d1ea2ccbd442c4`, `53df0f7739bbf4b12429cc23fb408aa8`,
`75aa6d14d891bc9e13d8fd2fe81fc2c9`, `cc042e7240677fe1cd333e7600261cc6` and
`d3b3d952f074233590e7f768b16cf9d6`. They were replaced by the five transparent PNGs above, cut from
the original full resolution artwork. Safe to delete.
