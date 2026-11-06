# Project status

Updated 2026-11-06 (Asia/Hong_Kong). Latest scope: three distinct product interactions and a substantial, measured content expansion. Apple remains the shell/proportion reference. Original portrait and finished CV remain unchanged. Owner accepted this version and authorized public release on 2026-11-06; publication is in progress.

## Repository and source readiness

Canonical checkout: `https://github.com/ZeyiLeo/ZeyiLeo.github.io.git`. Branch `codex/digital-identity`, committed HEAD `854b458`. The preceding implementation and the owner's prompt-guideline documentation were already uncommitted at the start; that work is preserved. Remote HEAD/master rechecked before editing and at handoff: `3d65738ad1dbab8a597f8d87b32ddcd9323d968e`. No commit, push, merge or deployment was performed.

Active Jekyll source remains `site/`; project notes and historical root theme files remain excluded from output. Preview: http://127.0.0.1:4173/ . Existing core routes, seven cases and legacy continuation routes remain. The three draft essays bring the generated HTML count to 27.

## Product state

- **A / global navigation:** About, Work and Explore disclosures open a grouped directory of real pages. A 460ms overlay reveal, staggered groups and a dimmed/blurred backdrop follow the supplied MOV's observed opening pattern. Click, keyboard/ArrowDown, hover, Escape, close and outside actions work. Mobile uses a root menu and child panel with Back. Covered/closed links are inert; focus returns appropriately. Menu changes do not change page width. Build-versioned assets prevent stale scripts during local review.
- **B / homepage connections:** four factual themes connect a material/workflow to its background and contribution. Desktop at least 1100×680 uses a short 505px progress range; two compact leaves expand into photo/workflow and text. It reverses with native scrolling. Explicit opening/selection remains readable while scrolling forward; reverse movement resumes scroll progress. Tablet/short windows show both sides with theme tabs; phones use a compact/open control and no long pin.
- **C / homepage selected work:** real Orbis, Speaking and Commerce layers change position, angle, scale and z-order over 680ms. One project remains in focus with synchronised title, role, contribution and link. Previous/next, tabs, Left/Right/Home/End and touch swipe work. Inactive layers are inert and excluded from accessibility focus. No autoplay or continuous movement.
- **Further exploration:** a five-theme experience filter plus All with nine expandable records and related links; eight contextual visual stories with topic/previous/next controls and photograph enlargement; generated article/case contents links. Existing project filters remain.
- **Fallbacks:** reduced motion shows all four connections and all three works in ordinary flow; navigation and controls remain usable without transitions. With script execution disabled, all connections/works and three direct navigation fallbacks remain visible. Scrolling is native. CSS/native JavaScript only; no animation dependency added. Hero keeps the approved original portrait and existing sequenced introduction.

## Content and editorial state

Fixed baseline: 1,611 globally deduplicated body words, 56 structural body modules, 13 existing core pages. Final: 9,058 words, 128 modules, 16 content pages. Added 7,447 words; final/baseline 5.623× against required 4× (6,444 words). Original 13 pages alone contain 6,938 effective words (4.31× baseline), so growth is not concentrated in the three essays. Exact method, paragraph/sentence decisions and before/after headings are in `_project/CONTENT_BASELINE.json/.md` and `CONTENT_GROWTH.json/.md`.

Counts exclude CV, navigation/footer/buttons, pure-link directions, TOCs, duplicate prose and identified review/UI instructions. Near-copy sentences are excluded with the same rule before and after. Module counts describe structure, not an independent guarantee of information quality. Editorial review removed repetitive source-boundary language and corrected the overlapping 2025 assistant/founder periods.

Current biographical/task facts come from confirmed records, the supplied CV and approved material. Creative roots use owner-provided historical clues and archived content. New explanatory case prose, About organisation, visual-story text and three essays are local editorial drafts for owner review; no new qualifications, results, audiences or personal incidents are asserted. The essays are visibly labelled new drafts, with hypothetical examples identified. Original Global Times title/date remain unchanged.

## Immutable assets

Original CV: one page, 235520 bytes, SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`. Original/source/build plus two actual downloads this round match. Desktop PDF.js display, phone open/zoom and both downloads verified. The original has existing parser index warnings; it renders and downloads, and is intentionally not repaired. CV generator remains removed.

Headshot: original `assets/img/02.jpg`, 2098×2937, copied unchanged to `site/assets/img/headshot-original.jpg`; SHA-256 `69c2aec2237ebfbb489f333552b6f90f0c561ef4568c2a3d8d3d574dbf9efb3d`. No new documentary imagery or retouching.

## Completed validation

- Production build; 27-page/seven-case internal links, content exclusions, assets and original-PDF checks; five JavaScript syntax checks; content target check; git whitespace check pass.
- 38 actual browser page/viewport checks (19 routes at 1440×900 and 390×844), plus five homepage widths 320/375/768/1024/1280: no page horizontal overflow or failed loaded photographs.
- Desktop clicks, keyboard, native Chrome hover bridge/leave, rapid close/reopen, phone hierarchical menu, touch return/close and focus isolation tested. Touch menu completion was checked after transition completion, rather than inferred from an intermediate sample.
- B compact/middle/open, forward/backward progress, manual interruption/readability, resize, refresh at y=1793/p=.501, and fast skip/return tested. C button/tab/keyboard/reverse selection, inactive focus isolation and two-way Chrome touch swipe tested. Vertical touch changes page position without changing the selected work.
- Timeline filtering returns four Healthcare entries and resets to all nine; expansion, story filtering/next, lightbox Escape/focus return and article TOC tested.
- Desktop/mobile reduced motion and native Chrome script-disabled fallback tested. Page logs show no application warnings/errors in inspected routes. Temporary viewport/media/cache/device/script overrides cleared; disposable native Chrome test tabs closed.
- Three actual-browser MP4 recordings and key desktop/mobile screenshots are in ignored `output/product-iteration/`. MP4s use real screencast frames with recorded timing; no staged screenshots stand in for motion verification.

## Limits, review and publication

No observed local functional blocker remains. Native browser mobile/touch emulation was used; physical iOS/Android devices, formal accessibility certification and a performance benchmark were not tested. MOV timing is a camera-recording estimate, not extracted CSS. Static Duo/Upgrade screenshots establish composition only; B/C motion is this iteration's requested interpretation. Source MOV did not show independent close/Escape/phone states; these were implemented and tested locally.

The owner accepted the current essays and expanded editorial explanations for this release; existing draft labels remain. More specific case evidence would require approved ACT/U21 outputs, a speech transcript or publishable store materials; none was fabricated. Earlier local-only restrictions are superseded by the owner's explicit 2026-11-06 release authorization. The publication record below tracks actual progress. See the local review package and `CONTENT_INVENTORY.md` for sources and remaining evidence gaps.

## Authorized release — 2026-11-06 (in progress)

- Owner explicitly accepted the local version and authorized commit, push, normal merge, Pages deployment and production verification. Historical local-review-only records are retained.
- Remote default/source branch: `master`, at `3d65738ad1dbab8a597f8d87b32ddcd9323d968e`; local `854b458` is one commit ahead with no divergence. Existing delivery path: build `site/` on master, push `_site/` to `gh-pages`, then GitHub Pages. The latest existing Pages run used `gh-pages`. Authenticated Pages settings verification is pending.
- Release preflight: Ruby 3.3.6 production build passes; existing 27-page/seven-case links, anchors, asset and original-CV checks pass; content target passes (9,058 words / 5.623× baseline); all five application scripts parse. Staged whitespace inspection finds only upstream PDF.js/license formatting and an existing blank line in home.js; these accepted/vendor files remain unchanged. Source has no local-only runtime URL or application debug logging. Original CV remains one page, 235,520 bytes, SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`.
- Accepted website source committed as `ed9cff85f85ac1f69b8d9887184bd7a2244c56f3` on `codex/digital-identity`; all 281 accepted source files are tracked and hash-identical to the reviewed files. Generated build contains 262 files. Ignored output/caches/recordings remain excluded.
- Push, production merge and deployment are pending GitHub account authentication. `gh auth status` reports: `You are not logged into any GitHub hosts.` Git credential lookup reports `fatal: could not read Username for 'https://github.com': terminal prompts disabled`. Browser also shows GitHub's sign-in form. Official GitHub CLI device login is open, including the workflow scope needed for the existing workflow update. No credentials or device codes are stored in repository files.
- Actual production-domain visit still displays the former `ZY LEE` homepage, confirming this release is not yet live. New deployment/live interaction checks and production CV download remain pending. Only account login is needed to continue; release authorization is already granted.
