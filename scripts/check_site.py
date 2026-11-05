#!/usr/bin/env python3
"""Check generated links, content safety, and online/PDF CV consistency."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
errors = []

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.text, self.h1s = [], set(), [], 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag == 'h1': self.h1s += 1
        for attr in ('href', 'src'):
            if attr in attrs: self.links.append(attrs[attr])
        if tag == 'img' and 'alt' not in attrs: errors.append('Image has no alt attribute')
    def handle_data(self, text): self.text.append(text)

pages = {p: Page(p.read_text()) for p in SITE.rglob('*.html')}
expected_projects = {'orbis-glaucoma','u21-ipe','ecommerce-brand','hku-academy','public-speaking','nursing-forum','digital-system'}
for slug in expected_projects:
    if not (SITE / 'projects' / slug / 'index.html').exists(): errors.append(f'Missing case page: {slug}')
for path, page in pages.items():
    if page.h1s != 1: errors.append(f'{path}: expected one h1, found {page.h1s}')
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = SITE / unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent / unquote(url.path)
        if not url.path: target = path
        if target.is_dir(): target /= 'index.html'
        if not target.exists(): errors.append(f'{path.relative_to(SITE)}: missing {link}')
        elif url.fragment and target.suffix == '.html':
            dest = pages.get(target)
            if dest and unquote(url.fragment) not in dest.ids: errors.append(f'Missing anchor {link}')
    text = ' '.join(page.text)
    for sample in ('Albert Einstein', 'John Doe', 'Lorem ipsum', 'Nobel Prize', 'HKUSON Nursing'):
        if sample in text: errors.append(f'Template/incorrect brand in {path}: {sample}')

for unwanted in ('_project', 'AGENTS.md', 'README.md', 'Gemfile', 'assets/json/resume.json', 'assets/pdf/example_pdf.pdf'):
    if (SITE / unwanted).exists(): errors.append(f'Internal/template material shipped: {unwanted}')

cv = json.loads((ROOT / 'site/_data/cv.json').read_text())
pdf = PdfReader(SITE / 'assets/pdf/Zeyi_Li_CV.pdf')
assert len(pdf.pages) == 2, f'Expected 2 PDF pages, got {len(pdf.pages)}'
def norm(s): return re.sub(r'\s+', ' ', s).strip()
pdf_text = norm(' '.join(p.extract_text() for p in pdf.pages))
online_text = norm(' '.join(pages[SITE / 'cv/index.html'].text))
facts = [cv['name'], cv['title'], cv['summary']]
for section in cv['sections']:
    for entry in section['entries']:
        facts += [entry['title'], entry['role'], entry['period'], *entry['bullets']]
facts += cv['interests'] + [c['value'] for c in cv['contacts']]
for fact in facts:
    for label, text in (('PDF', pdf_text), ('online', online_text)):
        if norm(fact) not in text: errors.append(f'{label} missing CV fact: {fact}')
if 'CV source SHA256' not in str(pdf.metadata.subject): errors.append('PDF source fingerprint missing')
import hashlib
if hashlib.sha256((ROOT / 'site/_data/cv.json').read_bytes()).hexdigest() not in str(pdf.metadata.subject): errors.append('PDF is stale relative to CV JSON')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages, internal links and anchors, content exclusions, {len(facts)} shared CV facts, 2-page PDF.')
