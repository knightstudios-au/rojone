import re, base64, mimetypes, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'source')
ASSETS = os.path.join(ROOT, 'assets')
DIST = os.path.join(ROOT, 'site')

# Artboard -> (published URL used in links, filename written to site/)
PAGES = {
    'Main.dc.html':     ('/',         'index.html',   'Rojone | RF, Microwave & Fibre Components & Assemblies'),
    'Category.dc.html': ('/category', 'category.html', 'Rojone | RF Connectors & Adaptors'),
    'Product.dc.html':  ('/product',  'product.html', 'RJ-SMA-1421 SMA Male to N-Type Female Adaptor | Rojone'),
    'About.dc.html':    ('/about',    'about.html',   'About Us | Rojone'),
    'Manufacturer.dc.html': ('/radiall', 'radiall.html', 'Radiall | Rojone'),
}
LINKS = {k: v[0] for k, v in PAGES.items()}


def uri(bid):
    hits = glob.glob(os.path.join(ASSETS, bid + '.*'))
    if not hits:
        raise KeyError('missing asset ' + bid)
    p = hits[0]
    m = mimetypes.guess_type(p)[0] or 'application/octet-stream'
    return "data:%s;base64,%s" % (m, base64.b64encode(open(p, 'rb').read()).decode())


def build(src, title, out):
    h = open(os.path.join(SRC, src), encoding='utf-8').read()
    hel = re.search(r'<helmet>(.*?)</helmet>', h, re.S).group(1)
    style = re.search(r'<style>(.*?)</style>', hel, re.S).group(1)
    links = '\n'.join(m.group(0) for m in re.finditer(r'<link [^>]*>', hel))
    body = re.search(r'</helmet>(.*?)</x-dc>', h, re.S).group(1)
    body = re.sub(r'/_blob/([a-f0-9]{32})', lambda m: uri(m.group(1)), body)
    body = re.sub(r'href="([A-Za-z0-9_.-]+\.dc\.html)([^"]*)"',
                  lambda m: 'href="%s%s"' % (LINKS.get(m.group(1), m.group(1)), m.group(2)), body)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{links}
<style>
{style}
</style>
</head>
<body>
{body}
</body>
</html>
'''
    open(os.path.join(DIST, out), 'w', encoding='utf-8').write(doc)
    unresolved = len(re.findall(r'/_blob/|\.dc\.html', doc))
    print('%-14s %9d bytes  unresolved refs: %d' % (out, len(doc), unresolved))


if __name__ == '__main__':
    os.makedirs(DIST, exist_ok=True)
    for src, (_url, out, title) in PAGES.items():
        if os.path.exists(os.path.join(SRC, src)):
            build(src, title, out)
