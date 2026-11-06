#!/usr/bin/env python3
"""Check generated links, content exclusions, and original PDF integrity."""
import json
import hashlib
import logging
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

asset = json.loads((ROOT / 'site/_data/cv_asset.json').read_text())
pdf_path = SITE / asset['url'].lstrip('/')
if hashlib.sha256(pdf_path.read_bytes()).hexdigest() != asset['sha256']:
    errors.append('CV PDF differs from the owner-provided original')
if pdf_path.stat().st_size != asset['bytes']:
    errors.append('Original PDF byte count changed')
logging.getLogger('pypdf').setLevel(logging.ERROR)
pdf = PdfReader(pdf_path)
if len(pdf.pages) != asset['pages']:
    errors.append('Original PDF page count changed')
cv_html = (SITE / 'cv/index.html').read_text()
if 'data-pdf-reader' not in cv_html or 'data-pdf-url="' + asset['url'] + '"' not in cv_html:
    errors.append('CV does not embed the original PDF')
if 'data-original-cv' not in cv_html or 'data-cv-download' not in cv_html:
    errors.append('CV open/download actions missing')
reader_html = (SITE / 'cv/original/index.html').read_text()
if 'data-fullscreen' not in reader_html or asset['url'] not in reader_html:
    errors.append('Full-window original CV reader missing')
for required in ('assets/js/pdf-reader.js', 'assets/vendor/pdfjs/build/pdf.mjs', 'assets/vendor/pdfjs/build/pdf.worker.mjs'):
    if not (SITE / required).is_file(): errors.append(f'Missing original-PDF reader resource: {required}')
if (ROOT / 'scripts/generate_cv.py').exists():
    errors.append('Retired PDF generator still exists')
if (ROOT / 'site/_data/cv.json').exists():
    errors.append('Retired generated-CV data is still active')

home = (SITE / 'index.html').read_text()
for marker in ('data-profile-hero', 'data-unfold', 'data-stack-deck', 'data-work-showcase', 'headshot-original.jpg'):
    if marker not in home: errors.append(f'Homepage experience missing: {marker}')
if '/assets/img/speaking-1280.webp' in home:
    errors.append('Rejected activity photograph is still on the homepage')
profile = json.loads((ROOT / 'site/_data/home_profile.json').read_text())
portrait = SITE / profile['portrait']['website_asset'].lstrip('/')
if hashlib.sha256(portrait.read_bytes()).hexdigest() != profile['portrait']['sha256']:
    errors.append('Approved portrait differs from its original')
for page_id in ['connection-0','connection-1','connection-2','connection-3','featured-0','featured-1','featured-2']:
    if page_id not in pages[SITE / 'index.html'].ids: errors.append(f'Missing homepage panel {page_id}')

for required in ('assets/js/navigation.js', 'assets/js/explore.js', 'assets/css/product.css', 'writing/health-information/index.html', 'writing/languages-and-context/index.html', 'writing/execution-and-commerce/index.html'):
    if not (SITE / required).is_file(): errors.append(f'Missing product iteration resource: {required}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f"PASS: {len(pages)} pages, seven cases, local links/anchors, content exclusions; original {asset['pages']}-page PDF, SHA-256 {asset['sha256']}.")
