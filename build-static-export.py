import re, base64, mimetypes, os, glob, sys
ROOT=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(ROOT,'source'); ASSETS=os.path.join(ROOT,'assets'); DIST=os.path.join(ROOT,'site')
LINKS={'Main.dc.html':'index.html','Category.dc.html':'category.html'}
def uri(bid):
    hits=glob.glob(os.path.join(ASSETS,bid+'.*'))
    if not hits: raise KeyError('missing asset '+bid)
    p=hits[0]; m=mimetypes.guess_type(p)[0]
    return "data:%s;base64,%s"%(m,base64.b64encode(open(p,'rb').read()).decode())
def build(src,title,out):
    h=open(os.path.join(SRC,src),encoding='utf-8').read()
    hel=re.search(r'<helmet>(.*?)</helmet>',h,re.S).group(1)
    style=re.search(r'<style>(.*?)</style>',hel,re.S).group(1)
    links='\n'.join(m.group(0) for m in re.finditer(r'<link [^>]*>',hel))
    body=re.search(r'</helmet>(.*?)</x-dc>',h,re.S).group(1)
    body=re.sub(r'/_blob/([a-f0-9]{32})',lambda m:uri(m.group(1)),body)
    body=re.sub(r'href="([A-Za-z0-9_.-]+\.dc\.html)([^"]*)"',lambda m:'href="%s%s"'%(LINKS.get(m.group(1),m.group(1)),m.group(2)),body)
    doc=f'''<!doctype html>
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
    open(os.path.join(DIST,out),'w',encoding='utf-8').write(doc)
    print(out,len(doc),'unresolved',len(re.findall(r'/_blob/|\.dc\.html',doc)))
build('Main.dc.html','Rojone | RF, Microwave & Fibre Components & Assemblies','index.html')
if os.path.exists(os.path.join(SRC,'Category.dc.html')) and '--category' in sys.argv:
    build('Category.dc.html','Rojone | RF Connectors & Adaptors','category.html')
