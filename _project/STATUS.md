# Project status

Updated: 2026-11-05 (Asia/Hong_Kong).
Scope: first complete local redesign, based on the canonical repository and the owner's supplied finished CV.

## Source readiness

This permanent workspace now has valid canonical Git history and remote `origin` at `https://github.com/ZeyiLeo/ZeyiLeo.github.io.git`. The current branch is `codex/digital-identity`, based on `master` at `3d65738ad1dbab8a597f8d87b32ddcd9323d968e`, verified through a live fetch. The independent canonical download in the sibling `web/zeyileo-source-20261105` folder provides an unchanged reference.

The original starter had no valid HEAD or remote. Its project records were preserved. Starter material is retained in sibling `web/archives/zeyileo-starter-20261105`, `zeyileo-starter-extras-20261105`, and `zeyileo-unused-starter-20261105`. Existing Git metadata was retained, then connected to remote history; no history was force-replaced. An initial broad move was rejected by automatic approval review; files were restored and the reconciliation was completed without deleting metadata or backups.

The active Jekyll source is exclusively `site/`. Root-level al-folio pages, sample posts, theme assets, plugins, and the unrelated Valentine pages remain historical files outside the source directory and are not emitted. Starter-only extra files and retired theme workflows have been moved to the external archive without deletion. The only active workflow is the revised GitHub Pages build/validation/deployment workflow.

## Implemented locally

- Home with exact HKUMed Bachelor ’29 branding, existing public portrait, selected work, interdisciplinary narrative and visual journal preview.
- About, filterable Work, Experience, Visual Journal, Writing, CV, Connect, and 404.
- Seven case studies: Orbis, U21, e-commerce, HKU ACT programme operations, public speaking, nursing forum, and this website.
- Seven legacy URL continuation pages, including the previous research and impact routes; unsupported claims are not carried forward.
- Dark/paper themes, responsive menu, native expandable experience entries, project filters, native dialog lightboxes, keyboard close/focus return, and reduced-motion support.
- Six journal photographs plus case-study media, using only imagery from the existing public repository, with metadata-free WebP derivatives.
- Shared `site/_data/cv.json` for CV, Experience, and two-page PDF. Exact degree is not inferred. No original private phone or personal email is included.
- Publication remains “Pros and cons of social media”, 21 Nov 2024 at the owner's explicit request. The differing embedded article URL is omitted. The mismatch is documented in the content inventory.
- README, design system, content inventory, roadmap, root changelog and session notes.

## Validation completed

- Production Jekyll build passes using Ruby 3.3.6 and Bundler 4.0.13. The broken system Node/Ruby paths were avoided using existing working runtimes; no system installation was altered.
- Linux/platform dependency records added to the committed lockfile. GitHub Actions itself has not run on this branch.
- Content checks pass for 23 generated HTML pages, local links/anchors, all seven case studies, one h1 per page, image alt attributes, and exclusion of internal/template content.
- 56 CV facts match between the online page and PDF; PDF source fingerprint agrees with JSON. All two PDF pages rendered with PDFium and visually reviewed. Poppler's generated-PDF rendering encountered a local font-cache problem, so PDFium supplied the verified renders.
- Actual browser PDF download succeeded; its bytes match the generated PDF. Original supplied CV is intact and unmodified.
- Browser checks: 40 route/viewport combinations across 375, 768, 1024 and 1440px. Main pages and all seven case studies checked at phone and desktop widths. No horizontal overflow or failed loaded images in final checks.
- Filters, timeline expansion, mobile navigation, theme persistence, lightbox close/Escape/focus restoration verified.
- Emulated reduced motion produces `scroll-behavior: auto` and zero transition duration; emulation reset afterwards.
- No page JavaScript warnings/errors observed. JavaScript syntax check passes.
- Main, muted and accent text all exceed WCAG AA 4.5:1 against both theme backgrounds; lowest measured pair is 5.02:1.
- Browser screenshots and layout-check JSON are in ignored `output/qa/`. This is a focused browser/accessibility review, not a full automated accessibility audit or formal performance benchmark.

## Publication status and remaining review

Local review version only. No push, merge, GitHub Actions run, or public deployment by this redesign session. The original public website remains unchanged. A local review commit has been saved on `codex/digital-identity`; inspect Git for its exact revision. Publication requires owner authorization under the supplied brief.

Before release, review the visual direction and public CV. The writing page awaits a matching original article URL. Additional private photographs, business screenshots, and research claims require appropriate evidence and publication approval. Existing LinkedIn and Instagram URLs are retained verbatim from the canonical site, with current ownership not independently reconfirmed.

See `README.md` for build/preview commands and `CONTENT_INVENTORY.md` for sources and publication decisions.
