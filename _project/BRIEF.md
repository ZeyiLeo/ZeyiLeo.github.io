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
| Visual direction | Premium, cinematic, editorial, sophisticated, minimalist, interactive |
| Audience | International professional audiences |

These are approved identity directions, not evidence of additional qualifications or achievements.
Use the exact public-facing title; do not expand it into a degree, registration, or professional credential without supporting information.
The existing public homepage uses the label “ZY LEE · Leo”; reconcile any future naming update deliberately across the site and CV.

## Working principles

1. Maintain continuity across website development sessions through repository instructions, current-state notes, and a change history.
2. Use the existing GitHub repository as the source of truth for website code.
3. Preserve established design decisions and record major changes with their reasons.
4. Prioritize authentic achievements, real photography, and verified professional information.
5. Keep the online CV and downloadable PDF consistent.
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

## CV continuity

Maintain one approved factual source for both the online CV and downloadable PDF.
Whenever a role, date, qualification, achievement, or contact detail changes, update both outputs and compare the facts before publication.
PDF layout and download behavior also need verification. Record the source and generation/export process once the current production implementation is confirmed.

## Initial decision

2026-11-05: Establish the project brief, session instructions, status notes, and changelog in this workspace.
This update records the owner's direction and repository findings. It does not select a new visual system or redesign the published site.

## 2026-11-05 implementation decisions

- Latest owner-provided finished CV is the factual source for roles, dates, and contributions. Public records live in `site/_data/cv.json`; original private CV remains outside the repository.
- Keep the supplied Global Times publication title and date unchanged, as explicitly instructed after a linked-page discrepancy was identified. Do not attach the mismatched hyperlink.
- Use the existing public institutional email in the public CV. Omit the original private phone number and personal email.
- Retain Jekyll, with a dedicated `site/` source directory and a minimal dependency set. Old root-level theme files do not generate pages.
- Implement an editorial dark/paper dual-theme direction for owner review. Do not describe this local direction as an approved or published brand system.
- Public release requires the owner's authorization under the current brief. Local implementation and tests do not authorize a push or deployment.
