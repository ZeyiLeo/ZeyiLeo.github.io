# Project status

## 2026-11-13 — Cinematic homepage intro

The homepage now opens with a 3.04-second assembly of the L/O monogram into LEO. The same SVG moves and scales into its home-link position while the existing hero animation starts. At the end, desktop shows LEO and phones show the existing compact monogram. The intro plays on the first eligible homepage entry in a tab session. Internal navigation, repeat loads, deep links and reduced motion go directly to the page. The Skip intro button, Escape, or interacting with the page releases it immediately.

The owner reviewed and authorized the release to https://zeyileo.github.io/. The `?intro=replay` link is available on that hostname and on loopback for deliberate replay. The normal homepage retains its session and reduced-motion rules. The loopback Jekyll preview is available at http://127.0.0.1:4173/.

Published source `002700707db997b1d7eb46da05b3bee99792c593` through [the production build](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/43357305744). [Pages deployment](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/43357341652) succeeded for artifact `91f8b040bcbd031dff44545a23ad63cacddec807`. All 264 live files match the verified release build after normalizing asset-version timestamps. Chromium verified both production URLs, first-visit and replay behavior, the hero handoff, Skip, reduced motion, desktop and 390px touch layouts, and existing navigation, homepage, gallery and CV controls. The desktop Visual Story Browser image has a zero-width container at 1280px on both the local and live builds. The affected journal source and styles predate this release. The separate gallery lightbox works.

## 2026-11-13 — Animated LEO wordmark (local review)

The shared header now uses an original inline SVG wordmark. On desktop, the homepage opens from a compact L/O monogram into LEO. The existing scrolled header state draws the O back into the L and slides the E out of view behind a clip. Hover and keyboard focus expand the scrolled mark. The link keeps the same footprint and accessible name, “Zeyi Li home.” Phones use the compact mark. Reduced-motion users get static LEO on desktop and the static monogram on phones. The project uses CSS transitions and the existing header scroll state.

Chrome checks at 1440×900 and 390×844 covered the initial reveal, fixed header geometry, repeated hover and mouseout, keyboard focus, scroll and reversal, scrolled reload, menu navigation, home navigation, reduced motion and desktop script-disabled fallback. The production Jekyll build and the 27-page link, asset, and original CV check passed. Local changes are uncommitted and await owner review. Start a preview with `RBENV_VERSION=3.3.6 JEKYLL_ENV=production bundle exec jekyll serve --host 127.0.0.1 --port 4173`.

Updated 2026-11-10 (Asia/Hong_Kong). The global navigation now includes a visible “拾课” link to the owner's separate password-protected course planner at `https://hku-course-planner.leo070310.workers.dev/`. The personal website publishes only the link; course tasks and passwords are not stored in this repository. The planner uses a private GitHub source repository, a Cloudflare Worker and D1 storage. Its 20 imported tasks were checked after refresh; this is a separate copy from the old Sites and local data.

Local validation for this navigation update: production Jekyll build and whitespace check passed; actual Chrome desktop and 390px mobile menu exposed the link, with no horizontal overflow. The local site checker could not run because this machine lacks `pypdf`; the GitHub workflow installs that dependency and runs the checker on publication. Publication and production-domain verification for this update are recorded in the newest changelog entry.

## 2026-11-10 — Planner navigation update

Affected source: `site/_includes/global-navigation.html`. The existing homepage, portfolio, CV and design system remain in place. The link appears in the desktop header and mobile menu. The separate course planner asks for its access password before showing pages, scripts or task data. The password is configured as a Cloudflare secret and is absent from both repositories.

Updated 2026-11-06 (Asia/Hong_Kong). Latest scope: three distinct product interactions and a substantial, measured content expansion. Apple remains the shell/proportion reference. Original portrait and finished CV remain unchanged. Owner accepted this version and authorized public release on 2026-11-06; publication and production-domain verification completed at 11:32 HKT.

## Repository and source readiness

Canonical checkout: `https://github.com/ZeyiLeo/ZeyiLeo.github.io.git`. Accepted website source: `ed9cff85f85ac1f69b8d9887184bd7a2244c56f3`. Initial normal production merge: `7818a1aa75e4041b3a1ebc1c725d55348d30ad10`; deployed master source after runner repair: `7481a9ee173d0441547a12ecf35c9f797dd4f822`. Published artifact branch commit: `25aff098b4e148592c6784b011ee25b0a700ef60`. Development and production history are preserved; no force-push was used. Final documentation-only updates follow this deployed source and do not change website build inputs.

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

Current biographical/task facts come from confirmed records, the supplied CV and approved material. Creative roots use owner-provided historical clues and archived content. New explanatory case prose, About organisation, visual-story text and three essays were accepted by the owner for this release; no new qualifications, results, audiences or personal incidents are asserted. The essays are visibly labelled new drafts, with hypothetical examples identified. Original Global Times title/date remain unchanged.

## Immutable assets

Original CV: one page, 235520 bytes, SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`. Original/source/build plus two actual downloads this round match. Desktop PDF.js display, phone open/zoom and both downloads verified. The original has existing parser index warnings; it renders and downloads, and is intentionally not repaired. CV generator remains removed.

Headshot: original `assets/img/02.jpg`, 2098×2937, copied unchanged to `site/assets/img/headshot-original.jpg`; SHA-256 `69c2aec2237ebfbb489f333552b6f90f0c561ef4568c2a3d8d3d574dbf9efb3d`. No new documentary imagery or retouching.

## Prior local acceptance validation

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

## Authorized release — 2026-11-06 (completed)

The owner explicitly accepted this version and authorized commits, pushes, normal merges, GitHub Pages deployment and live verification, including the complete unchanged original CV. Prior local-only decisions remain in the brief and changelog as historical records. The GitHub CLI permission prompt was resolved by the owner's explicit approval of the displayed scope. No credentials are stored in this repository.

### Source and publication

- `codex/digital-identity` pushed with accepted source commit [`ed9cff8`](https://github.com/ZeyiLeo/ZeyiLeo.github.io/commit/ed9cff85f85ac1f69b8d9887184bd7a2244c56f3). Master has no applicable branch rules requiring a PR; normal merge [`7818a1a`](https://github.com/ZeyiLeo/ZeyiLeo.github.io/commit/7818a1aa75e4041b3a1ebc1c725d55348d30ad10) was pushed. No PR was needed.
- First run `42155933460` stopped before build because `ubuntu-latest` selected Ubuntu 26.04, which has no Ruby 3.3.6 binary. Repair [`f1f38f1`](https://github.com/ZeyiLeo/ZeyiLeo.github.io/commit/f1f38f16344fc2cab9f10c19a9e1e24716e39b28) pins the existing job to Ubuntu 24.04; the official Ruby archive returned HTTP 200. Repair merged and pushed as [`7481a9e`](https://github.com/ZeyiLeo/ZeyiLeo.github.io/commit/7481a9ee173d0441547a12ecf35c9f797dd4f822). Website source/content unchanged.
- [Production build and artifact publication](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/42156187944): success, including the production Jekyll build, page/link/asset checks and original-CV integrity check.
- [GitHub Pages build and deployment](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/42156251293): success. Pages API confirms `built`, no error, artifact commit `25aff098b4e148592c6784b011ee25b0a700ef60`; deployed 2026-11-06 at 11:24 HKT. Existing configuration preserved: legacy branch publication from `gh-pages`, `/` root, HTTPS.
- All 281 accepted website source files remain tracked and hash-identical to the reviewed version. Original source/dependencies/runtime resources and third-party licenses are included. Recordings, screenshots, caches and generated output remain ignored.

### Production-domain verification — completed 11:32 HKT

Target: https://zeyileo.github.io/ . All checks below used the public production domain.

- Downloaded all 262 generated pages/resources from production and compared with the accepted local production build. All match; only numeric HTML asset-version build timestamps were normalized. This includes all CSS, JavaScript, images, original PDF, PDF.js modules, fonts, CMaps, WASM and licenses. The existing checker also passes against the downloaded production mirror: 27 pages, seven cases, internal links/anchors and original-PDF integrity. An unknown route returns HTTP 404; direct `/404.html` correctly returns 200.
- Actual Chrome desktop (1440×900) and mobile-size (390×844, touch emulation) inspection confirms latest homepage, approved white-background/black-shirt portrait, `HKUMed Bachelor ’29` and three essay draft labels. No horizontal overflow observed in checked core routes and articles.
- Navigation disclosure/close, grouped real links and 12px backdrop blur verified on desktop; phone root/child/Back/close/link navigation verified. About, Work, Experience, Journal, Writing, all seven case pages and all three article pages open. Article TOCs have six links and perform anchor navigation; cases have seven contents links.
- Homepage two-sided opening/closing/theme selection and work-layer button/tab/keyboard selection verified. The phone featured-project link reaches the correct public-speaking case. Experience Healthcare filter gives four entries and All resets to nine. Visual-story Next and photograph lightbox open/close work.
- Desktop original PDF reader renders one page; mobile original-file view opens and zooms to 120%. Actual desktop and phone browser downloads from production both verify as 235,520 bytes / one page / SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`. Separate direct production-domain download matches too. No rewriting or PDF repair.
- No application warning/error logs observed in checked production views. Screenshots, live-file comparison report and browser-download hashes are saved in ignored `output/release/`.

### Remaining limits

No unresolved release blocker. Mobile verification uses Chrome viewport/touch emulation; physical iOS/Android devices were not tested. Existing workflow versions produce a non-blocking Node 20 deprecation annotation; GitHub runs them on Node 24 and both workflows succeeded. A future routine maintenance change can update those actions separately.
