# ZEYILEO | Digital Identity

Established: 2026-11-05 (Asia/Hong_Kong).
Authority: the owner's project instructions supplied on this date. Later owner instructions supersede this brief.

## Purpose

Develop and maintain a lasting personal website at https://zeyileo.github.io/ that can evolve with Zeyi's education, professional work, creative practice, and interests.
The GitHub repository is the source of truth for website code: https://github.com/ZeyiLeo/ZeyiLeo.github.io.

## Core identity

| Element | Owner-supplied direction |
| --- | --- |
| Names | Zeyi Li / Z.Y. Lee / Leo |
| Public-facing title | HKUMed Bachelor ’29 |
| Positioning | Healthcare × Communication × Business × Technology × Creative Work |
| Visual direction | Apple.com as the direct structural and interaction reference; system sans-serif, black/white/grey, large media and restrained blue actions |
| Audience | International professional audiences |

These are approved identity directions, not evidence of additional qualifications or achievements.
Use the exact public-facing title; do not expand it into a degree, registration, or professional credential without supporting information.
The existing public homepage uses the label “ZY LEE · Leo”; reconcile any future naming update deliberately across the site and CV.

## Working principles

1. Maintain continuity across website development sessions through repository instructions, current-state notes, and a change history.
2. Use the existing GitHub repository as the source of truth for website code.
3. Preserve established design decisions and record major changes with their reasons.
4. Prioritize authentic achievements, real photography, and verified professional information.
5. Show and download the original CV PDF unchanged; do not regenerate it from website data.
6. Fit new sections to the established visual system.
7. Prefer reusable components and structured content to simplify future updates.
8. Test changes before deployment and protect existing functionality.
9. Do not publish private information or unapproved personal photos.
10. Keep the site technically maintainable, visually ambitious, and suitable for international professional audiences.

## Editorial approach

Use specific contributions, relevant context, and supported outcomes to explain the work.
Preserve the distinction between a personal role and a team result, participation and leadership, an ongoing project and completed work, and an interest and established expertise.
Do not fill gaps with invented achievements, dates, impact figures, affiliations, or credentials.
An existing public claim can guide a source audit but does not independently verify itself.

For future portfolio updates, keep reusable records of the project title, dates, context, exact role, contribution, outcome, public evidence, and approved media where applicable.
Keep private supporting evidence outside the public repository.

## Design continuity

Before changing visual design, inspect the current repository and rendered pages and identify the actual typography, palette, spacing, imagery, layout, and interaction behavior.
The owner's direction is established; an exact typeface, palette, animation system, or layout is not newly approved by this document.
Use authentic photography with publication approval, deliberate hierarchy, readable content, restrained motion, and accessible interactions to express that direction.

## CV continuity — latest owner decision

The owner-provided original PDF is authoritative as a complete finished document. Directly display it on desktop and provide clear open/download actions on all devices. Preserve every word, date, contact, font, layout and page count. Validate the downloaded file against the original SHA-256. Do not recreate, redact or typeset it; do not alter it to match website experience summaries. The former shared JSON/PDF generation policy is superseded.

## Initial decision

2026-11-05: Establish the project brief, session instructions, status notes, and changelog in this workspace.
This update records the owner's direction and repository findings. It does not select a new visual system or redesign the published site.

## Prior review decisions — superseded by the latest decisions below

- Latest owner-provided finished CV is the factual source for roles, dates, and contributions. Public records live in `site/_data/cv.json`; original private CV remains outside the repository.
- Keep the supplied Global Times publication title and date unchanged, as explicitly instructed after a linked-page discrepancy was identified. Do not attach the mismatched hyperlink.
- Use the existing public institutional email in the public CV. Omit the original private phone number and personal email.
- Retain Jekyll, with a dedicated `site/` source directory and a minimal dependency set. Old root-level theme files do not generate pages.
- Implement an editorial dark/paper dual-theme direction for owner review. Do not describe this local direction as an approved or published brand system.
- Public release requires the owner's authorization under the current brief. Local implementation and tests do not authorize a push or deployment.

## Latest decisions — Apple reference and original CV

2026-11-05: The owner explicitly superseded the previous serif/terracotta editorial direction. Use actual inspected Apple homepage and product-detail structure, scale, navigation and motion as references, with Zeyi's own identity, content and approved photos. See DESIGN_SYSTEM.md for measurements and observed limitations.

The original one-page CV is restored byte-for-byte, including its existing contacts. No privacy edits, wording changes or new layout are authorized. The previous two-page PDF generator is removed. This round is exclusively local review: no push, merge or deployment.


## Latest homepage decisions — interactive biography and original headshot

2026-11-05, subsequent local review: strengthen the homepage itself with three distinct experiences: a sequenced portrait introduction with reversible scroll composition, a short desktop-pinned biography with three factual chapters, and actively selectable featured projects. Keep native scrolling, keyboard controls and a complete reduced-motion fallback. Mobile uses ordinary-flow chapters with explicit controls.

The owner confirmed the white-background, black-shirt front-facing photograph. Use the original `assets/img/02.jpg` (2098×2937) unchanged as `site/assets/img/headshot-original.jpg`. Remove the rejected activity photograph from the homepage hero and homepage social preview. Its project-page use can remain. Never substitute an AI portrait or enlarged screenshot crop.

The old website is a content/history and photo-source reference only; it does not set typography, colour, navigation or layout. The Apple homepage/product-page reference remains authoritative. Distinguish current CV-supported work from early creative interests; omit unverified old event details and old private contacts from homepage copy. Keep the original finished CV binary unchanged. Local modification/review only; no commit, push, merge or deployment requested.


## Latest product iteration — three mechanisms and measured depth

2026-11-06: Complete the owner's product iteration locally. A uses the supplied MOV's navigation reveal/background treatment; B translates the Duo screenshot's two-sided composition into a reversible content expansion; C translates the Upgrade screenshot's centre/layers into an actively selected work stack. Static screenshots do not establish source motion. All mechanisms must have useful real content, phone controls and complete reduced-motion/fallback access.

Content baseline is frozen at 1,611 effective body words across 13 core pages. Required final total is at least 6,444 with the unchanged counting method. This iteration reaches 9,058 across 16 pages; the three new essays are visibly marked drafts for owner review, not past publications. Preserve original article metadata, CV binary, approved portrait, all working routes and existing user documentation. Continue to distinguish recorded facts from editorial interpretation and hypothetical examples.

The latest homepage connection/work-stack implementation replaces the preceding three-chapter pinned biography/tabbed-work implementation. Experience and visual stories provide further active exploration. No commit, push, merge or deployment is authorised for this iteration.


## Publication authorization — 2026-11-06

The owner has reviewed and accepted the current local version and explicitly authorized public release to https://zeyileo.github.io/, including the necessary commits, development-branch push, normal merge to the existing production source branch, GitHub Pages deployment and live verification. This supersedes earlier local-review-only restrictions for this accepted version; those historical decisions remain recorded above. No further publication confirmation is required for this release. Preserve accepted content, interactions, images, draft labels and the complete original CV unchanged. Follow existing branch protection, preserve history and never force-push.
