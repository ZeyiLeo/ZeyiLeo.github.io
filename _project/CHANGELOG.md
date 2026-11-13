# Project changelog

Record substantive updates newest first. Use dates in Asia/Hong_Kong.
For each update, include the reason, affected files, validation results, and publication status.

## 2026-11-13 — Move the opening wordmark into the live header

Reason: extend the local LEO motion study into a short opening that physically becomes the navigation logo. Compared a separated letter assembly with a compact symbol unfolding into LEO. Chose the symbol because its existing geometry can assemble, expand and dock as a single object. Rechecked the Anthropic roadshow header in Chrome. Its scroll transition informed the shared letter geometry and easing, while the opening sequence is original to the portfolio.

Changes: added homepage-only `brand-intro.js` and `brand-intro.css`, wired them into the shared layout, and gave the existing SVG stem an animation hook. The Web Animations API moves the actual navigation SVG from the center to its measured resting position. The existing portrait and copy reveal start during the flight. Session rules, a keyboard-accessible skip and bounded failure cleanup return control to the page. Retired the former standalone desktop wordmark entrance.

Validation: Chromium desktop and 390px touch emulation showed the centered hold, continuous flight, existing hero reveal and exact resting geometry. Checked first entry, repeat refresh, direct and internal navigation, pointer and keyboard skip, Escape, reduced motion, and the JavaScript-disabled homepage. The production Jekyll build, 27-page site checker, all application script syntax checks and whitespace checks passed. The added CSS and JavaScript total about 2.3 KB gzipped, and the intro requests no fonts or media. Review frames are in ignored `output/brand-intro-review/`.

Publication: the owner reviewed and authorized the release through the existing `master` → `gh-pages` workflow. Enabled `?intro=replay` on the production hostname for the requested live verification. The animation itself uses the reviewed assets and timing.

Production verification: [source build](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/43357305744) succeeded for `0027007`, and [Pages deployment](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/43357341652) succeeded for `91f8b04`. Compared all 264 public files to the release build. Both live URLs passed intro playback and browser checks, including skip, repeat navigation, reduced motion, and the mobile handoff. Existing homepage controls, a case route, experience filter, gallery lightbox and CV reader worked. The older desktop Visual Story Browser image layout issue is recorded in status.

## 2026-11-13 — Add the animated LEO header identity

Reason: give the portfolio an animated home mark that fits the existing navigation. Verified GitHub `master` and the starting checkout at `ca09914`.

Reference: inspected the [Anthropic roadshow page](https://www.anthropic.com/news/roadshow-launch) in Chrome, including a 390px viewport. The [header playback code](https://www.anthropic.com/_next/static/chunks/0x79jairvdy42.js) initializes directly at the relevant Lottie frame and reverses direction as the header state changes. The [state logic](https://www.anthropic.com/_next/static/chunks/387qbv7yhyi21.js) uses 15px of scroll and keeps the mark compact at widths of 870px or below. Desktop hover and mouseout left the logo still. Observed collapse and reversal keep the same link width while individual letter groups converge or separate. The [animation asset](https://www.anthropic.com/_next/static/chunks/0-c74pgbjyzf4.js) uses a 30 fps timeline and reaches the compact state at frame 18, with a position easing segment of `cubic-bezier(.77, 0, .175, 1)`.

Changes: added `site/_includes/wordmark.html` and wired it into `site/_includes/global-navigation.html`. In `site/assets/css/identity.css`, reused the reference’s roughly 600ms travel and measured easing for the custom L and O. Added a clipped, staggered E, a desktop homepage entrance, and desktop hover and focus expansion. Followed the portfolio’s existing 8px scroll trigger and 767px mobile breakpoint. The inline artwork uses the header ink color and the link occupies 56×44px on desktop and 56×48px on mobile.

Validation: Chrome verified 1440px and 390px layouts, initial transition, settled and reversed states, rapid hover re-entry, mouseout, focus, deep-scroll reload, menu and home navigation, reduced motion, and desktop script-disabled links. Production Jekyll build, five JavaScript syntax checks, whitespace, and the 27-page site checker passed. Browser screenshots are in ignored `output/wordmark-review/`. Mobile testing used Chrome touch emulation.

Publication: uncommitted local review on `master`. No commit, push, merge or deployment.

## 2026-11-10 — Add private course planner entry

Reason: the owner requested a visible link on the existing personal website to the independent online “拾课” planner, with password access before course information is shown.

Changes: added the “拾课” link to the shared global navigation and updated project status. The link points to the separate Cloudflare Worker; no task data, password or credential was added to this public repository.

Validation: local production Jekyll build and whitespace check passed. Chrome desktop navigation and 390px mobile menu showed the link without horizontal overflow. Local site checker was unavailable because `pypdf` is not installed on this machine; the deployment workflow runs it with its pinned dependency. The planner's login, 20-task import, cloud save, refresh persistence and unauthenticated data/asset denial were verified separately.

Publication: source pushed to `master`; production GitHub Actions and live-domain navigation checked after push. The planner remains on its own private repository and cloud database, separate from the old Sites and local copies.

## 2026-11-06 — Production release completed and verified

Reason: fulfill the owner's explicit authorization to publish the accepted local version. Accepted source `ed9cff8` was pushed, normally merged to master as `7818a1a`, and published after the runner-only repair (`f1f38f1`, merged as `7481a9e`). No PR required by repository rules; no force push. The accepted 281 website source files remain hash-identical, with original portrait, complete original CV, draft labels, copy and interactions preserved.

Production [build/publication run 42156187944](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/42156187944) and [Pages deployment run 42156251293](https://github.com/ZeyiLeo/ZeyiLeo.github.io/actions/runs/42156251293) succeeded. Existing `master → gh-pages → Pages` structure retained; artifact `25aff098b4e148592c6784b011ee25b0a700ef60` deployed at 11:24 HKT.

Live verification completed at 11:32 HKT: all 262 production files match the local accepted build after normalizing build-version timestamps; the existing 27-page/seven-case link/asset/CV checker passes on the downloaded production mirror. Actual desktop/mobile browser checks cover the latest homepage, approved portrait, global menu, two-sided themes, layered works, core routes, seven cases, three essays and TOCs, experience filtering, stories/lightbox, CV rendering/open/zoom and actual downloads. Both browser downloads and a direct production download preserve the one-page, 235,520-byte CV SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`.

Publication: https://zeyileo.github.io/ is live with the accepted version. No release blocker remains. Mobile uses browser emulation. Non-blocking action-runtime deprecation annotation is recorded for future maintenance. Final documentation-only status updates do not change or redeploy website content. Earlier local-only, login-pending and first-run-failure records below remain historical evidence.

## 2026-11-06 — Production runner compatibility repair

The first authorized production run `42155933460` stopped before building: `ubuntu-latest` now selects Ubuntu 26.04, where the pinned Ruby 3.3.6 binary is unavailable. Pin the existing job to `ubuntu-24.04`; the official Ruby 3.3.6 archive for that runner returns HTTP 200. Keep Ruby, dependencies, accepted website content and deployment structure unchanged. Remote production build and deployment will validate the repair.

## 2026-11-06 — Owner-authorized production release (in progress)

The owner accepted the reviewed local version and explicitly authorized all normal publication steps to https://zeyileo.github.io/. Earlier local-only history is retained. Preserve accepted copy, draft labels, approved portrait, original CV and interactions.

Preflight passes: Ruby 3.3.6 production build, 27 pages/seven cases, internal links/anchors/assets, original PDF hash/size/page integrity, five application script syntax checks and content target. Staged whitespace findings are upstream vendor/license formatting and an existing blank line; no functional change is needed. Confirmed remote master is unchanged at `3d65738`; local committed base is one commit ahead without divergence. Runtime sources contain no local preview dependencies. PDF.js runtime resources and licenses are included; ignored recordings, screenshots, caches and generated build output remain excluded.

Publication: accepted source committed locally as `ed9cff85f85ac1f69b8d9887184bd7a2244c56f3`; all 281 accepted source files remain hash-identical and tracked. GitHub CLI and browser are not signed in, so push, merge, deployment and new-version live checks await account authentication. Actual production-domain visit still shows the old homepage. Official device login is open; no repeated release consent is required.

## 2026-11-06 — Three product interactions and measured content expansion

Reason: implement the owner's supplied MOV/two-screenshot brief, grow effective content to at least four times the frozen baseline and make the additional material actively explorable. Local review only.

Changes:

- Preserved the inherited dirty tree, branch/history, existing routes, user prompt-guideline notes, original portrait and CV. Rechecked remote master/HEAD unchanged at `3d65738`.
- Added grouped global disclosures with staged entrances/backdrop blur, mobile hierarchy, keyboard/hover/click operation and inert/focus management. Added asset build versions after detecting stale preview scripts during validation.
- Replaced the previous home chapter/tab presentation with four two-sided material/context stories and a true three-layer work browser. B has reversible short-distance scroll geometry and a phone open control; C reorders real content with synchronised roles/links and touch/keyboard selection. Reduced motion/no-script retain complete content.
- Deepened About, all seven cases, experience and visual storytelling. Added topic filtering/expansion, eight image stories and reading TOCs. Three complete essays are labelled new drafts for owner review. Preserved the existing article title/date and original PDF binary.
- Froze 13-page baseline HTML before edits and added `measure_content.py`. Final globally deduplicated body content: 1,611 → 9,058 words (5.623×; +7,447), 56 → 128 structural modules across 16 content pages. Original 13 pages alone: 6,938 words. Excluded duplicated/UI/review prose and legacy redirects; no counting-method change to the frozen baseline.

Validation:

- Production build, 27-page/seven-case links/assets/original-PDF checks, five script syntax checks, content target and whitespace checks pass.
- Actual browser A/B/C forward/reverse/interruption checks; hover bridge/leave; keyboard/focus; phone hierarchy; Chrome touch swipe/vertical scroll; timeline, image viewer/lightbox and TOC checks pass. Refresh at y=1793 retains B progress .501. Manual opening stays readable going forward and rejoins reverse scrolling.
- 38 route/device checks plus five home widths show no page horizontal overflow or failed loaded photos. Desktop/mobile reduced motion and Chrome script-disabled static fallback pass. No inspected application errors/warnings. Temporary overrides cleared; native test tabs closed.
- Desktop/phone original PDF display/open/zoom and new actual downloads match original/source/build SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`, one page/235520 bytes. Original headshot bytes also match.
- Three real-browser MP4 clips, key state screenshots, full measurement report and a review HTML are in ignored `output/product-iteration/`. Camera-video timing is approximate; static references do not establish source motion. Physical devices, a formal accessibility audit and performance benchmark remain untested.

Publication: uncommitted local changes only. No commit, push, merge, deployment or Actions run. Preview remains at http://127.0.0.1:4173/.

## 2026-11-05 — Record product-manager framing for future prompts

Reason: the owner requested detailed, logical website prompts written from an experienced product manager's perspective, including future prompt updates.

Changes: added `_project/PROMPT_GUIDELINES.md` and linked it from `AGENTS.md`. The guidance covers user intent, reference interpretation, animation behavior, content expansion metrics, factual boundaries, continuity, and observable acceptance criteria.

Validation: checked that the guidance file exists and the session instruction points to it. No website source, CV, portrait, or runtime behavior changed in this documentation update.

Publication: local documentation changes only; no commit, push, merge or deployment.

## 2026-11-05 — Interactive homepage, confirmed original headshot and fuller introduction

Reason: the owner requested three substantial homepage interactions, removal of the blurry event hero, and a fuller factual biography. The owner explicitly confirmed the original white-background, black-shirt headshot. Apple remains the visual/interaction reference; old-site design is not reused. Local-only scope.

Changes:

- Rechecked canonical remote/branch and preserved the preceding uncommitted work. Replaced the homepage with a sequenced original-portrait introduction, reversible desktop scroll composition, three short biography stages with progress, and a selectable Orbis/Speaking/Commerce showcase.
- Added `home_profile.json`, `home.css` and `home.js`, loaded only on home. Native scroll/rAF, responsive pin thresholds, keyboard tabs, button controls, touch swipe, explicit selection state and complete reduced-motion/no-JavaScript content. No new animation dependency.
- Copied original `assets/img/02.jpg` unchanged to the active site: 2098×2937, 107410 bytes, SHA-256 `69c2aec2237ebfbb489f333552b6f90f0c561ef4568c2a3d8d3d574dbf9efb3d`. Historic Git/backup/source copies match. Updated homepage social preview too. Rejected activity photo is absent from homepage.
- Added current HKU/U21, ACT internship, Orbis and e-commerce contributions; added early creative interests from owner-supplied historical clues, clearly separated from current roles. No old private contacts or unverified old news/awards copied. Updated brief, design system, content inventory, README and session direction.
- Original finished CV binary, reader, download and retired generator state remain unchanged.

Validation:

- Production build, 24-page/seven-case links/content/PDF checks, three script syntax checks and whitespace checks pass. Source, built and desktop/phone downloaded original PDFs all match SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4` (one page, 235520 bytes).
- Actual browser scrolling verified hero progress/reversal, all three story stages/reversal/natural exit, refresh at y=1445 and fast skip/return. Mouse selection, keyboard tabs and all three featured detail paths work. Healthcare filtering still returns three projects. Phone menu/Escape/focus/navigation and PDF opening/zoom/download checked.
- Desktop/mobile reduced motion exposes every chapter/project without pinning or entrance/scroll transforms. 320–1440px sampled layouts have no horizontal overflow or failed loaded photos. Application browser logs show no errors/warnings.
- Chrome phone emulation verifies swipe both directions and normal vertical touch scrolling. Physical phones were not tested; exact Apple source video timing is not claimed. All temporary overrides cleared.
- Screenshots and an approximately 15-second GIF encoded from real browser screencast frames are in ignored `output/home-interactions/`. MP4 export was unsuccessful; no substitute video is claimed. Screenshot images described in the request were unavailable, so unseen text was not transcribed.

Publication: uncommitted local changes on `codex/digital-identity` only. No commit, push, merge or deployment; preview remains at http://127.0.0.1:4173/.

## 2026-11-05 — Apple reference interface and original CV restoration

Reason: the owner explicitly requested the original finished CV without any rewriting, plus an Apple.com-based visual and interaction direction. Local-only implementation; no push, merge or deployment.

Changes:

- Verified clean starting tree on `codex/digital-identity`, HEAD `854b458`, and canonical remote HEAD `3d65738` before editing. Existing Jekyll source and public routes retained.
- Restored the original one-page `Zeyi_Li_CV.pdf` byte-for-byte (235520 bytes; SHA-256 `156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4`), including all original wording, dates, article entry, contacts, fonts and layout.
- Removed `scripts/generate_cv.py`, retired the generated-CV JSON and ReportLab dependency. Existing confirmed website records moved to `site/_data/experience.json`; they no longer generate or replace the CV.
- Rebuilt CV as an original-file display with large open/download actions. Self-hosted Mozilla PDF.js reads the original on desktop and in the full-window `/cv/original/` view, addressing native PDF rendering failures in the inspected browser environment. Download remains the original binary. Phone CV landing does not embed/load a small reader.
- Actually inspected Apple homepage and its linked iPhone 18 Pro page on desktop/mobile. Replaced the prior serif/terracotta design with system sans typography, compact navigation, black/white/grey bands, blue actions, paired modules, natural-colour photos and a directory footer.
- Added measured-menu-style phone transitions, sequenced intro, moderate scroll-linked photo composition, sticky case navigation and three Orbis process stages. Phone/reduced-motion presentation uses normal document flow with all process images.
- Preserved work filters, case URLs, experience entries and photo dialog behaviour. Added already-public Orbis media derivatives. Updated README, design system, content inventory, roadmap, brief and session instructions to make the latest decisions authoritative.

Validation:

- Production Jekyll build passes. Content checks pass for 24 HTML pages, seven cases, local links/anchors, internal/template exclusions, required reader assets and original-PDF hash/size/page count. Both application scripts pass syntax checks.
- Actual browser download completed; downloaded `Zeyi_Li_CV (2).pdf` has the same hash and byte count as the original source and served website file. Original source PDF remains unchanged.
- Desktop embedded PDF, zoom/fit controls and phone full-window original-PDF opening/zoom verified. Six requested desktop/mobile screenshots and additional reader/menu/story evidence are saved in ignored `output/apple-review/`.
- 46 browser layout checks across 375, 390, 768, 1024 and 1440px pass, including all main/case pages at phone/desktop widths and additional full-reader checks. No horizontal page overflow, failed loaded images, or page-script warnings/errors observed.
- Project filtering, project entry, full-height phone menu, Escape/focus return, experience expansion and lightbox closing verified. Native scrolling samples show story stage 0 → 1 → 2, stable pinned position, then natural exit. Intro delays and scroll image transforms verified through computed styles.
- Reduced-motion emulation confirms no intro animation, automatic scroll behaviour and unpinned complete process images. Viewport/media emulation reset afterwards.
- Some reference-site videos did not play, so exact source video timing/frame sequences could not be measured. No physical iPhone/Android certification, full automated accessibility audit, or production deployment is claimed.

Publication: uncommitted local changes on the existing branch only; no new commit, push, merge, deployment, or GitHub Actions run in this round. Live site unchanged.

## 2026-11-05 — Build the first complete editorial review version

Reason: implement the owner's long-term digital identity brief using current canonical code and the subsequently supplied finished CV.

Changes:

- Reconciled the permanent workspace with canonical Git history at `3d65738`, preserving existing metadata and starter material; created `codex/digital-identity`.
- Added the dedicated `site/` Jekyll source, shared layouts, editorial dual-theme CSS, and lightweight accessible interaction script. Replaced active al-folio output without changing hosting providers.
- Built eight core pages, seven factual case studies, 404, sitemap/robots metadata, and seven continuation pages for older public routes.
- Added approved public-image WebP derivatives, journal lightboxes, project filters, responsive navigation, and expandable experience records.
- Adopted the owner-supplied CV for supported roles/dates; one JSON record renders online CV/Experience and generates the public two-page PDF. Omitted private phone/personal email and retained the existing public contact. Original CV remains unmodified outside the repository.
- Kept the publication title/date unchanged at the owner's request and documented the differing embedded article link without publishing it.
- Added build/content/PDF checks, a cross-platform dependency lock, the updated GitHub Pages workflow, and complete project/design/content/roadmap documentation. Archived unrelated theme workflows and unchanged starter extras outside the checkout.

Validation:

- Production build and JavaScript syntax pass. Local checks validate 23 HTML pages, seven case pages, local links/anchors, internal/template exclusions, and 56 shared online/PDF CV facts.
- Two-page PDF rendered and visually reviewed. Actual browser download verified byte-for-byte against the generated file; original supplied PDF intact.
- Forty browser layout checks pass at 375/768/1024/1440px after fixing a mobile typographic cover overflow. Project filters, menu, themes, expandable entries and lightbox keyboard/focus behaviour verified.
- Reduced-motion emulation confirmed disabled transitions/smooth scrolling and was reset. No page JS warnings/errors observed. Theme text contrast meets AA; lowest checked ratio 5.02:1.
- No GitHub Actions execution or public deployment verified because the branch has not been pushed. No formal automated accessibility audit/performance benchmark claimed.

Publication: local review commit saved on `codex/digital-identity`; no push, merge or deployment. Public release awaits the owner's authorization in accordance with the supplied brief.

## 2026-11-05 — Establish the permanent project brief

Purpose: preserve the owner's identity, creative direction, and maintenance standards across future development sessions.

Changes:

- Added `AGENTS.md` with session guidance, editorial and design standards, CV consistency requirements, the update workflow, and the supplied Xiaohongshu MCP rules.
- Added `_project/BRIEF.md` with the owner-supplied identity, exact public-facing title, positioning, visual direction, and working principles.
- Added `_project/STATUS.md` with the source mismatch, canonical repository revision observed today, separate backup checkout, starter file map, and verification limits.
- Added this changelog and linked the project notes from `README.md`, preserving the original theme documentation below it.
- Added `AGENTS.md` and `_project/` to the Jekyll exclusions so project guidance is not copied into the generated site.

Validation:

- Passed YAML parsing and comparison against the original configuration: only the two intended exclusions changed.
- Passed project-document structure and local-link checks, including the README links.
- Confirmed that the public-facing title and positioning match exactly across the instructions, brief, and README.
- Confirmed that the original README remains intact below the new introduction.
- Verified the current canonical GitHub HEAD with a live remote check and recorded its difference from the backup checkout.
- Node-based formatting could not run because the local Node executable cannot start.
- Full site build and browser preview were not run. The local Ruby/Bundler setup cannot start the required build, and the local Node executable has a missing library; details are recorded in `STATUS.md`.

Publication: local workspace changes only. No commit, push, or deployment.
