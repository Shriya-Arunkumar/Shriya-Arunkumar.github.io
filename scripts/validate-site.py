from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=set(); self.links=[]; self.stack=[]; self.errors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('duplicate id '+a['id'])
            self.ids.add(a['id'])
        for attr in ('href','src'):
            if attr in a: self.links.append(a[attr])
        if tag not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'): self.stack.append(tag)
    def handle_endtag(self,tag):
        if not self.stack or self.stack[-1]!=tag: self.errors.append('mismatched closing '+tag)
        else: self.stack.pop()
pages={}
for f in [Path('index.html'),*Path('projects').glob('*.html'),*Path('research').rglob('*.html')]:
    parser=Page(); parser.feed(f.read_text(encoding='utf-8')); pages[f.resolve()]=parser
errors=[]
for f,p in pages.items():
    errors.extend(f'{f.name}: {e}' for e in p.errors)
    if p.stack: errors.append(f'{f.name}: unclosed {p.stack}')
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        target=(f.parent/unquote(u.path)).resolve() if u.path else f
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{f.name}: missing {link}')
        if u.fragment and target in pages and u.fragment not in pages[target].ids: errors.append(f'{f.name}: missing anchor {link}')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML pages; balanced markup, unique IDs, local links, assets and anchors.')
