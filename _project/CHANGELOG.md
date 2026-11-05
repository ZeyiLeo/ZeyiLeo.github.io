# Project changelog

Record substantive updates newest first. Use dates in Asia/Hong_Kong.
For each update, include the reason, affected files, validation results, and publication status.

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
