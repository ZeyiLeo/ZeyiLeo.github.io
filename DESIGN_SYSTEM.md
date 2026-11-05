# ZEYILEO design system

Established in the local redesign on 2026-11-05; pending owner review and public release.

## Direction and rationale

An editorial portfolio with cinematic photographic framing. The prior site used a dark background, sans-serif typography, blue accents, rounded panels, and static category labels. This redesign retains the dark foundation and authentic images, introduces a warm paper theme, and uses serif display typography, fine rules, open layouts, and restrained terracotta accents to express the owner's premium editorial direction. This is a new implementation decision, not a previously approved brand specification.

## Typography

Display: system Baskerville, Iowan Old Style, Palatino, or Georgia. Body: Helvetica Neue, Helvetica, Arial. Local fonts avoid remote network requests; appearance can vary by operating system. Display titles use tight tracking and generous scale. Body copy uses 1.65–1.85 line height and controlled line lengths. Small uppercase labels identify sections without competing with headings.

## Colour tokens

| Token | Dark | Light | Purpose |
| --- | --- | --- | --- |
| `--bg` | `#171916` | `#f2efe7` | Page surface |
| `--surface` | `#20231e` | `#e8e4da` | Secondary surface |
| `--ink` | `#f2eee5` | `#23271f` | Primary text |
| `--muted` | `#b1b4a9` | `#626858` | Supporting text |
| `--accent` | `#e49b82` | `#963e28` | Emphasis and focus |
| `--line` | `#41453b` | `#c5c6b8` | Non-text rules |

Text and focus colours must remain legible in both themes. Fine divider colours are not used as body text. The initial theme is dark, with a saved user choice restored on later visits. Theme storage failure must not prevent switching.

## Layout and components

Maximum content width: 1400px. Page gutters: 52px desktop, 32px tablet, 20px phone. Layout breakpoints: 1100, 900, and 600px. Project lists use two columns before collapsing to one. The journal uses three, two, then one column. The mobile menu is a disclosure with Escape support; navigation remains available without JavaScript.

Components: shared header/footer, project card, typographic cover artwork, section label, text action, filled action, expandable timeline entry, CV section, photo link, native dialog lightbox. Abstract project covers are explicitly visual design, not photographs or evidence. They carry no invented metrics.

## Photography

Use existing publicly displayed images only until further media is approved. Hero and portfolio frames are deliberately cropped; full images are available in the journal lightbox. New derivatives are WebP, with 640 and 1280px variants where useful. Strip EXIF and provide descriptive alt text, accurate intrinsic dimensions, and lazy loading below the fold. Do not imply that an event photo was taken by Zeyi unless a credit is verified.

## Interaction and accessibility

Use transform/opacity for small hover feedback, generally 200–450ms. No scroll hijacking, automatic slideshows, parallax, page-blocking intro, or motion-dependent content. `prefers-reduced-motion` disables transitions and smooth scrolling. Native `<details>` and `<dialog>` preserve keyboard behaviour. Dialog close restores focus to the photo. Filters announce the visible count. All JS enhancements leave core content and photo links usable without JavaScript.
