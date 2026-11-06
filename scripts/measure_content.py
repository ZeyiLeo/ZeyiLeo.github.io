#!/usr/bin/env python3
"""Measure distinct English body copy using one frozen baseline/comparison method.

This is an editorial accounting tool, not a claim that word count alone proves
information value. It does not change, generate, or read the CV PDF.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime
from difflib import SequenceMatcher
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import unicodedata
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASELINE_FILE = ROOT / '_project/CONTENT_BASELINE.json'
SNAPSHOT = ROOT / 'output/product-iteration/baseline'
METHOD_VERSION = 'distinct-body-v1'
MIN_BLOCK_WORDS = 8
CORE = ['/', '/about/', '/projects/', '/experience/', '/photography/', '/writing/']
# The seven original case routes are part of the frozen scope. Legacy
# continuation pages under /projects/ are not new editorial content.
CASE_ROUTES = [
    '/projects/digital-system/', '/projects/ecommerce-brand/',
    '/projects/hku-academy/', '/projects/nursing-forum/',
    '/projects/orbis-glaucoma/', '/projects/public-speaking/', '/projects/u21-ipe/',
]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
BODY_TAGS = {'p', 'li', 'figcaption', 'dd', 'blockquote'}
EXCLUDED_TAGS = {'script', 'style', 'noscript', 'svg', 'button', 'nav', 'aside', 'form', 'label'}
EXCLUDED_ROLES = {'navigation', 'tablist', 'tab', 'status', 'toolbar', 'menu', 'menuitem', 'progressbar'}
EXCLUDED_CLASSES = {
    'eyebrow', 'profile-alias', 'profile-title', 'featured-role', 'project-role',
    'case-role', 'timeline-date', 'role', 'writing-meta', 'draft-badge', 'draft-status',
    'reading-time', 'filter-status', 'featured-status', 'chapter-hint', 'chapter-position',
    'toc', 'page-toc', 'article-toc', 'table-of-contents', 'contents', 'breadcrumbs',
    'related-links', 'citation-list', 'source-list', 'sources', 'references',
    'screen-reader-only', 'sr-only', 'visually-hidden',
}
CONTROL_CLASSES = {'button', 'solid-button', 'text-link', 'button-outline', 'button-small'}
# Only explicit UI instructions/placeholders are filtered; substantive future
# questions and proposed reflections remain eligible body content.
NONCONTENT = re.compile(
    r'(?:^scroll to |^choose (?:a |the )?(?:chapter|project|topic)|^explore the role, the work|'
    r'^read the full background|^open an entry to |^use (?:the |your )?(?:buttons|arrow keys)|'
    r'will be added once confirmed|original texts will appear here|'
    r'^this space will grow with|^publication listed in (?:my|the supplied) cv|'
    r'^Zeyi Li / Z\.?Y\.? Lee / Leo|^Photograph retained from the existing public portfolio)', re.I
)
WORD_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)*(?:[-–][^\W_]+)*", re.UNICODE)
SENTENCE_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9“‘"\[])')


@dataclass(eq=False)
class Node:
    tag: str
    attrs: dict[str, str | None]
    parent: 'Node | None' = None
    children: list['Node | str'] = field(default_factory=list)
    order: int = 0

    def ancestors(self):
        node = self
        while node is not None:
            yield node
            node = node.parent

    def descendants(self):
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.descendants()

    def classes(self):
        return set((self.attrs.get('class') or '').split())


class Document(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.root = Node('document', {})
        self.stack = [self.root]
        self.serial = 0
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        self.serial += 1
        node = Node(tag, dict(attrs), self.stack[-1], order=self.serial)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, text):
        self.stack[-1].children.append(text)


def normalise_text(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text)).strip()


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def signature(text: str) -> str:
    return ' '.join(w.lower().replace('’', "'") for w in words(text))


def ignored(node: Node) -> bool:
    for ancestor in node.ancestors():
        if ancestor.tag in EXCLUDED_TAGS or ancestor.attrs.get('role') in EXCLUDED_ROLES:
            return True
        if ancestor.classes() & EXCLUDED_CLASSES:
            return True
        if 'data-content-ignore' in ancestor.attrs or 'data-animation-copy' in ancestor.attrs:
            return True
        if ancestor.tag == 'a' and ancestor.classes() & CONTROL_CLASSES:
            return True
    return False


def text_of(node: Node) -> str:
    parts = []
    for child in node.children:
        if isinstance(child, str):
            parts.append(child)
        elif not ignored(child):
            parts.append(text_of(child))
    # Spaces preserve inline boundaries such as <strong>role</strong> or <br>.
    return normalise_text(' '.join(parts))


def route_for(path: Path, site: Path) -> str:
    relative = path.relative_to(site)
    if str(relative) == 'index.html':
        return '/'
    return '/' + str(relative.parent).replace('\\', '/') + '/'


def is_redirect(path: Path) -> bool:
    doc = Document(path.read_text())
    for node in doc.root.descendants():
        if node.tag == 'meta' and (node.attrs.get('http-equiv') or '').lower() == 'refresh':
            return True
    return False


def page_files(site: Path) -> list[Path]:
    result = []
    for route in CORE + CASE_ROUTES:
        path = site / route.lstrip('/') / 'index.html'
        if not path.exists():
            raise SystemExit(f'Missing required measured page: {path}')
        if is_redirect(path):
            raise SystemExit(f'Required editorial page became a redirect: {path}')
        result.append(path)
    # Scope is the frozen thirteen editorial routes, plus genuine new Writing
    # articles. Do not sweep legacy /projects/* continuation/redirect pages into
    # the measurement just because they reside below the same directory.
    for path in sorted((site / 'writing').glob('*/index.html')):
        if path not in result and not is_redirect(path):
            result.append(path)
    return result


def heading_for(node: Node, headings: list[Node]) -> str:
    latest = None
    for heading in headings:
        if heading.order >= node.order:
            break
        latest = heading
    return text_of(latest) if latest else 'Introduction'


def container_key(node: Node) -> str:
    # Repeated headings in different cards/chapters are different modules, while
    # consecutive paragraphs under one case/essay heading remain one module.
    for ancestor in node.ancestors():
        if ancestor.tag in {'article', 'section', 'details'}:
            return f'{ancestor.tag}-{ancestor.order}'
    return 'main'


class Dedupe:
    def __init__(self):
        self.exact = set()
        self.sentences: list[tuple[str, list[str], set[str]]] = []

    def accept(self, text: str) -> bool:
        key = signature(text)
        if key in self.exact:
            return False
        tokens = key.split()
        token_set = set(tokens)
        if len(tokens) >= 12:
            for prior, prior_tokens, prior_set in self.sentences:
                if len(prior_tokens) < 12:
                    continue
                ratio = len(tokens) / len(prior_tokens)
                if not .85 <= ratio <= 1.18:
                    continue
                if len(token_set & prior_set) / max(1, len(token_set | prior_set)) < .75:
                    continue
                if SequenceMatcher(None, tokens, prior_tokens, autojunk=False).ratio() >= .90:
                    return False
        self.exact.add(key)
        self.sentences.append((key, tokens, token_set))
        return True


def measure(site: Path) -> dict:
    dedupe = Dedupe()
    paragraph_keys = set()
    pages = []
    for path in page_files(site):
        source = path.read_text()
        doc = Document(source)
        mains = [n for n in doc.root.descendants() if n.tag == 'main']
        if len(mains) != 1:
            raise SystemExit(f'Expected exactly one main in {path}')
        main = mains[0]
        nodes = list(main.descendants())
        headings = [n for n in nodes if n.tag in {'h1', 'h2', 'h3', 'h4'} and not any(a.tag in {'nav', 'aside'} for a in n.ancestors())]
        blocks = []
        rejected = []
        modules: dict[str, dict] = {}
        for node in nodes:
            if node.tag not in BODY_TAGS or ignored(node):
                continue
            # Keep the smallest prose unit, avoiding nested <li><p>...</p></li>
            # and <blockquote><p>...</p></blockquote> double counting.
            if any(n.tag in BODY_TAGS and not ignored(n) for n in node.descendants()):
                continue
            text = text_of(node)
            block_words = len(words(text))
            if block_words < MIN_BLOCK_WORDS:
                continue
            if NONCONTENT.search(text):
                rejected.append({'text': text, 'reason': 'UI instruction or explicit placeholder'})
                continue
            key = signature(text)
            if key in paragraph_keys:
                rejected.append({'text': text, 'reason': 'Exact repeated body block'})
                continue
            paragraph_keys.add(key)
            accepted = []
            duplicates = []
            for sentence in SENTENCE_RE.split(text):
                sentence = sentence.strip()
                if not sentence:
                    continue
                if NONCONTENT.search(sentence):
                    duplicates.append({'text': sentence, 'reason': 'UI instruction or explicit placeholder'})
                elif dedupe.accept(sentence):
                    accepted.append(sentence)
                else:
                    duplicates.append({'text': sentence, 'reason': 'Repeated sentence or at least 90% token-sequence match'})
            unique_text = ' '.join(accepted)
            unique_words = len(words(unique_text))
            if not unique_words:
                rejected.append({'text': text, 'reason': 'All sentences repeated or UI/placeholder text'})
                continue
            label = heading_for(node, headings)
            module_key = f'{container_key(node)}:{label}'
            module = modules.setdefault(module_key, {'heading': label, 'words': 0, 'body_blocks': 0})
            module['words'] += unique_words
            module['body_blocks'] += 1
            blocks.append({'tag': node.tag, 'module': label, 'words': unique_words, 'source_text': text, 'counted_text': unique_text, 'excluded_sentences': duplicates})
        pages.append({
            'route': route_for(path, site), 'source_sha256': sha256(source.encode()).hexdigest(),
            'words': sum(b['words'] for b in blocks), 'body_blocks': len(blocks),
            'independent_modules': len(modules), 'modules': list(modules.values()),
            'blocks': blocks, 'excluded_body_blocks': rejected,
        })
    return {
        'method_version': METHOD_VERSION,
        'measured_at': datetime.now(ZoneInfo('Asia/Hong_Kong')).isoformat(timespec='seconds'),
        'method': {
            'scope': 'Main content of the frozen thirteen editorial routes (Home, About, Projects index, seven original project cases, Experience, Photography, Writing index), plus genuine new /writing/* articles. CV, contact, legacy/redirect and 404 excluded.',
            'eligible_tags': sorted(BODY_TAGS), 'minimum_body_block_words': MIN_BLOCK_WORDS,
            'word_rule': "Unicode alphanumeric tokens; internal apostrophes/hyphens remain one token. Headings and alt text are not counted.",
            'hidden_content': 'Unique content in hidden tabs/details is counted once; hidden state never removes real content from this audit.',
            'exclusions': 'Navigation/footer/buttons/TOC/status/role/date/eyebrow labels, explicit UI instructions/placeholders and data-content-ignore/data-animation-copy regions.',
            'deduplication': 'Across all measured pages in fixed route order: exact normalised paragraph/sentence duplicates removed. Sentences with at least 12 words also removed at >=90% token-sequence similarity, with comparable length and >=75% token-set overlap.',
            'modules': 'Each nearest article/section/details container plus preceding content heading with at least one accepted body block. Titles themselves add no words. Structural heading changes alone do not prove a new editorial topic.',
            'limitation': 'Same-word or near-copy inflation is suppressed; semantic information value and unsupported facts still require editorial review. The audit does not count photographs themselves as words.',
        },
        'total_words': sum(p['words'] for p in pages),
        'total_body_blocks': sum(p['body_blocks'] for p in pages),
        'total_independent_modules': sum(p['independent_modules'] for p in pages),
        'pages': pages,
    }


def table_for(baseline: dict, current: dict | None = None) -> str:
    old = {p['route']: p for p in baseline['pages']}
    new = {p['route']: p for p in (current or baseline)['pages']}
    rows = ['| Page | Before words | After words | Before modules | After modules | New heading/topic groups |', '| --- | ---: | ---: | ---: | ---: | --- |']
    for route in list(old) + [r for r in new if r not in old]:
        a = old.get(route, {'words': 0, 'independent_modules': 0, 'modules': []})
        b = new.get(route, {'words': 0, 'independent_modules': 0, 'modules': []})
        prior_labels = {m['heading'] for m in a['modules']}
        added = list(dict.fromkeys(m['heading'] for m in b['modules'] if m['heading'] not in prior_labels))
        rows.append(f"| `{route}` | {a['words']} | {b['words']} | {a['independent_modules']} | {b['independent_modules']} | {'; '.join(added).replace('|', '/')} |")
    total_new = (current or baseline)['total_words']
    rows.append(f"| **Total, globally deduplicated** | **{baseline['total_words']}** | **{total_new}** | **{baseline['total_independent_modules']}** | **{(current or baseline)['total_independent_modules']}** | |")
    return '\n'.join(rows)


def markdown_report(baseline: dict, current: dict | None = None) -> str:
    target = baseline['total_words'] * 4
    body = ['# Effective content audit', '', f"Method: `{METHOD_VERSION}`. Frozen baseline: {baseline['measured_at']}.", '', f"Baseline: **{baseline['total_words']} distinct body words**. Required final total: **{target} words** (4× baseline; new content must be at least 3× baseline).", '']
    if current:
        after = current['total_words']
        body += [f"Current total: **{after}**. Added: **{after - baseline['total_words']}**. Final/baseline: **{after / baseline['total_words']:.3f}×**. Target: **{'PASS' if after >= target else 'NOT YET MET'}**. Remaining word gap: **{max(0, target - after)}**.", '']
    body += [table_for(baseline, current), '', '## Fixed counting rules', '']
    body += [f"- **{key.replace('_', ' ')}:** {value}" for key, value in baseline['method'].items()]
    body += ['', 'Full accepted/excluded body text, module assignments, source HTML hashes and sentence-level decisions are retained in the JSON audit. Frozen source HTML is in ignored `output/product-iteration/baseline/`. A module count is a structural aid, not a substitute for reviewing unique information. New draft status and factual sources must be documented separately in the content inventory.', '']
    return '\n'.join(body)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--baseline', action='store_true', help='Freeze the first measurement. Refuses to overwrite an existing baseline.')
    mode.add_argument('--compare', action='store_true', help='Compare current built pages with the immutable baseline.')
    parser.add_argument('--site', type=Path, default=ROOT / '_site')
    parser.add_argument('--baseline-file', type=Path, default=BASELINE_FILE)
    parser.add_argument('--snapshot-dir', type=Path, default=SNAPSHOT)
    parser.add_argument('--output', type=Path, help='Comparison JSON path; default _project/CONTENT_GROWTH.json')
    parser.add_argument('--require-target', action='store_true', help='Exit nonzero when comparison has not reached four times the baseline.')
    args = parser.parse_args()
    if args.baseline:
        if args.baseline_file.exists():
            raise SystemExit(f'Refusing to overwrite baseline: {args.baseline_file}')
        if not args.snapshot_dir.exists():
            for path in page_files(args.site):
                target = args.snapshot_dir / path.relative_to(args.site)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
        result = measure(args.snapshot_dir)
        result['snapshot_directory'] = str(args.snapshot_dir.relative_to(ROOT))
        args.baseline_file.parent.mkdir(parents=True, exist_ok=True)
        args.baseline_file.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        args.baseline_file.with_suffix('.md').write_text(markdown_report(result))
        print(f"BASELINE: {result['total_words']} distinct body words; {result['total_independent_modules']} modules; {len(result['pages'])} pages. Required final total: {result['total_words'] * 4} words.")
    else:
        baseline = json.loads(args.baseline_file.read_text())
        if baseline['method_version'] != METHOD_VERSION:
            raise SystemExit('Baseline method version differs; do not silently change the counting method.')
        result = measure(args.site)
        result['baseline_words'] = baseline['total_words']
        result['target_words'] = baseline['total_words'] * 4
        result['added_words'] = result['total_words'] - baseline['total_words']
        result['final_multiplier'] = result['total_words'] / baseline['total_words']
        result['target_met'] = result['total_words'] >= result['target_words']
        output = args.output or ROOT / '_project/CONTENT_GROWTH.json'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        output.with_suffix('.md').write_text(markdown_report(baseline, result))
        print(f"CURRENT: {result['total_words']} words; BASELINE: {baseline['total_words']}; {result['final_multiplier']:.3f}x; ADDED: {result['added_words']}; REQUIRED: {result['target_words']}; {'PASS' if result['target_met'] else 'NOT YET MET'}")
        if args.require_target and not result['target_met']:
            raise SystemExit(1)


if __name__ == '__main__':
    main()
