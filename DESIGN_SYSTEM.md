# ZEYILEO interface system

Latest decision: 2026-11-06, three-mechanism product iteration. The owner's Apple-reference direction supersedes the previous serif/terracotta editorial design. The old website is a content/photo source only. This round is local review only.

## Current product iteration — 6 November 2026

This section supersedes older homepage interaction specifications below. Preserve the established Apple-reference system typography, colours, compact shell, original portrait and immutable CV.

| Reference | What was actually observed | Current translation |
| --- | --- | --- |
| `IMG_7437.MOV`, 6.2867s, HEVC 10-bit, 3840×2160, about 60fps | Around 2.1–2.6s: dark panel expands under a stationary global nav, grouped links become readable in sequence, underlying visual darkens/blurs. Around 3.2s the menu withdraws during navigation, then the destination page appears. Approximate 0.4–0.6s reveal from camera frames. | Global About/Work/Explore disclosures on every standard page. A 460ms clip reveal, 380ms group entrances with 90ms + 65ms offsets, and a 400ms backdrop fade with 12px blur. These are chosen implementation values, not claimed source CSS measurements. |
| `截屏2026-11-05 16.37.35.png` | Centred heading/actions and a connected wide, two-sided subject in its expanded state. | Homepage material/context leaves start at .68 scale with opposing 165px offsets, then reach two full columns through a 505px scroll progress range. The photo itself remains geometrically intact. Motion/reversal is the owner's requested interpretation of the static composition. |
| `截屏2026-11-05 16.37.48.png` | A clear centre subject with offset layers behind it. | Three real project layers: active at x/y/rotation=0 and scale1; side layers ±65px, −28/−14px, ±6°, scale .91; 680ms `cubic-bezier(.2,.75,.25,1)` reordering. Phones use ±20px/±3°/.94. Motion is newly designed, not inferred from the screenshot. |

**A — navigation.** Mouse hover waits 130ms; leaving the whole header/panel hierarchy waits 220ms before closing. Crossing from the trigger to the panel does not close it. Click keeps an explicit disclosure open; keyboard activation/ArrowDown enters its links. Escape/close/outside actions restore state. Covered phone root navigation and all closed panels are inert, including during exit. Group switching clears old timers. Desktop width stays stable through `scrollbar-gutter:stable`; the overlay does not push body layout. Phone panels slide 35px over 400ms, with Back and Close. The original MOV did not show these independent keyboard/phone/close behaviours; they are locally verified additions.

**B — connections.** Desktop pin threshold is 1100×680. Scene height is viewport + 440px, sticky frame viewport − 65px at top54, giving a 505px content progress range. Text appears as space is formed, and links remain inert until readable. Manual opening/selection remains fully readable during forward scrolling; reverse input rejoins native progress. At tablet/short dimensions both sides are visible with theme tabs; an ineffective open button is hidden. Phones use a compact/open toggle and ordinary flow. Four topics carry distinct materials/tasks, not repeating field labels.

**C — selected work.** A measured deck reserves the tallest real card height. All three content layers are unique; inactive copies/links are inert and aria-hidden. Tabs, previous/next, selected underline, live position, keyboard and horizontal touch choose the focus. Vertical touch remains page scrolling. The settled card is stable; no auto rotation or autoplay. Commerce shows documented workstreams, not a fabricated dashboard.

The experience filter and visual-story browser support the expanded content. Reading TOCs and discrete controls have at least 44px touch targets; body text links keep normal inline typography. Images are lazy-loaded where appropriate and space is reserved. Native scroll uses a passive listener/rAF with cached geometry and skips unchanged story writes; there is no continuous animation loop or animation dependency.

Reduced motion removes introduction/transform/pinning and shows all four connections and all three projects in normal flow. With scripts disabled, direct navigation fallbacks and full static content remain. New CSS and scripts use a per-build query version to avoid stale local-preview assets. Reference materials and recordings remain outside the generated site in ignored `output/product-iteration/`.

## Actual reference inspection

Inspected https://www.apple.com/ and the linked https://www.apple.com/iphone-18-pro/ in the browser on 2026-11-05, at desktop and 390px mobile widths. These are structural and motion references; the site uses Zeyi's own name, content and approved photographs, without Apple trademarks or product assets.

Observed homepage: fixed 44px desktop navigation, a 1024px navigation content box, centered product heading/copy/actions, large visual bands separated by narrow white gutters, paired desktop modules that stack on mobile, filled blue/outlined buttons, and a compact grey directory footer. Mobile navigation was 48px high, expanded to the viewport, and used 28px/600-weight links. Its computed content transition was 422ms with `cubic-bezier(.4,0,.6,1)`.

Observed product page: a large introductory visual, local project/product navigation that stays visible after scrolling, separate highlights, large section headings and a pinned camera presentation. The sampled pinned section was 1584px tall in a 720px viewport (2.2 screens), with a 721px sticky frame. At document offsets 5040 and 5400 the frame remained at viewport top; at 5760 it moved to -144px and exited naturally. Other sampled image treatments included 1.2 scale and 80px translation before entering their final composition.

Source-media availability varied between inspections: several source videos did not play initially, while some short videos loaded during the homepage-interaction revision. Exact frame-by-frame playback and all source timings were not measurable. Do not claim pixel-perfect reproduction or independently verified source video speeds. Chosen durations are implementation tuning based on observable rhythm and the measured mobile menu transition. In this revision, the Highlights controls were actively operated (Colors → Camera on desktop; Battery on mobile), and the page was scrolled forward and back.

## Page mapping

- Home: Apple homepage centered introduction and compact shell; product-page reversible image composition, short pinned narrative and actively selectable Highlights-style work presentation. Original headshot is sized to its photographic format, rather than stretched into a wide event banner. See the latest homepage specification below.
- Work: the same paired module organisation, using real project roles and useful underlined category filters.
- Project detail: product-page overview, a 56px translucent local navigation surface inset 8px from the top while sticky (72px including surrounding spacing), large photograph and contribution narrative. Orbis additionally uses three process stages with a pinned photo area on desktop.
- CV: the owner's untouched PDF, with clear open/download actions; desktop document reader, phone-first full-size opening. No CV typesetting or generation.
- Existing About, Experience, Journal, Writing and Connect retain their factual content and paths inside the shared new shell.

## Typography and colours

System sans-serif only: `-apple-system`, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial. No external font requests. Default body 17px; main desktop headings 56–72px, phone headings 40–48px; paired module headings 32–40px. Normal case, restrained negative tracking. No large serif titles, uppercase tag clouds, or decorative quote treatment.

| Use | Colour |
| --- | --- |
| Main background | `#ffffff` |
| Secondary surface | `#f5f5f7` |
| Primary text | `#1d1d1f` |
| Secondary text | `#6e6e73` |
| Rules | `#d2d2d7` |
| Links | `#0066cc` |
| Filled action | `#0071e3` |
| Dark module | `#000000` with `#f5f5f7` text |
| Links on dark | `#2997ff` |

Photographs retain natural colour; no desaturation/colour filter. Square visual bands and modules are the default. Rounded treatment is reserved for action buttons, the photo dialog and small document controls.

## Motion specifications

- Navigation: subtle translucent background on scroll. On phones the full-height menu transitions for 422ms; links remain keyboard accessible, the background is inert while expanded, and Escape returns focus to the toggle.
- Case introductions retain the existing timed arrival. Homepage introduction now follows the sequence and geometry in the latest specification below. Neither uses a scroll lock.
- Key photos: passive scroll listener with requestAnimationFrame. Composition changes by up to 28px vertically and scale 1.035 → 1.0 across viewport passage; phones reduce translation to 10px.
- Two major section headings enter once when 40% visible over 750–850ms. This treatment is not applied to every section.
- Orbis: three 75vh desktop stages, approximately 2.25 screens overall. The image stays visible while the adjacent narrative advances; 450ms image crossfades and 650ms settling. The pinned region exits through normal layout at the end. All three image/text pairs display sequentially on phones and with reduced motion.
- Links/buttons: 180ms colour/press feedback; project image hover scales by 1.025 over 500ms.

No wheel interception, scroll snapping, autoplay carousel or forced section navigation. `prefers-reduced-motion` removes intro/reveal/scroll transforms and transitions, and replaces pinning with ordinary document flow. Core text, links and all process photographs remain available without JavaScript.

## Original CV contract

`site/assets/pdf/Zeyi_Li_CV.pdf` is copied byte-for-byte from the owner's provided original. Its size, one-page count and SHA-256 are recorded in `site/_data/cv_asset.json`. The desktop reader uses self-hosted Mozilla PDF.js to display that same PDF; the original binary is neither modified nor regenerated. This addresses the in-app browser's blank native PDF surface. The open action provides a full-window reader of the same original PDF, avoiding native viewer inconsistencies; download returns the original PDF URL directly.

Below 768px the embedded reader is hidden and its PDF library/document are not loaded; large open/download actions are shown. Reader zoom affects only display scale. Website experience records remain separate from the immutable CV. The old generator is removed.


## Prior homepage specification — superseded on 6 November 2026

The homepage has three different interaction patterns, implemented only with CSS and one native JavaScript module (`home.css`, `home.js`). No animation dependency is added. Shared navigation, buttons, footer, route structure and case components remain reusable.

1. **Portrait introduction.** Alias/name/title/introduction/actions enter at 0/70/140/220/300ms; the original portrait starts at 360ms. Text runs 650ms and portrait 800ms with `cubic-bezier(.2,.7,.25,1)`. This plays on entry, not on every return to the viewport; restored pages skip the intro. At desktop sizes at least 1024×680, the hero is viewport + 200px with a sticky composition. Its 244px progress range shifts text by up to −60/−38px and scale .93, and the whole portrait/caption by +140/−58px and scale .82; corners settle from 0 to 22px. Scrolling backward restores the composition. It exits via ordinary document flow. Smaller screens use up to 12–14px vertical movement and .95 image scale, without a long pin.
2. **Personal background.** Three chapters: current HKU/U21 background; specific ACT/Orbis/e-commerce work; pre-university creative roots and current bilingual/literary interests. Above 1100×680, a viewport + 520px scene contains a sticky viewport − 88px frame, leaving a 608px scroll range for the three chapters. The frame has a natural exit. Scroll progress selects 0 → 1 → 2 and reverses; a visible count/line follows progress. Images settle from 1.025 to 1.0 within each stage; visual switch 400ms, copy switch 300ms/8px. Explicit tabs work too; an explicit choice is held until the next scroll chapter boundary. Mobile/short screens use tabs in ordinary flow, without extra scroll distance.
3. **Selected work.** Orbis, Speaking and Commerce tabs change the visual, role, contribution and detail link together. Previous/next buttons, a selected underline, a live position label, keyboard Left/Right/Home/End, and touch swipe all have real effects. No autoplay. On desktop photographs fill an intrinsically stable 535px panel; mobile stacks the photograph and contribution. The commerce visual is documented workstreams rather than fabricated photography or store results.

Original headshot: 2098×2937 JPEG, displayed at 230×322 on roomy desktop, 193×270 on short desktop, and 190×266 on mobile. The JPEG bytes are untouched; natural white background blends into the page. Head, face and shoulders remain intact. Homepage social preview uses the same photo.

All layout-changing content panels disable browser scroll anchoring so native anchoring does not compete with intentional state changes; keyboard tab focus uses `preventScroll`. No wheel interception, forced page jumps or scroll snapping. Geometry is measured on resize/load/pageshow and scroll updates use one passive listener plus requestAnimationFrame.

Reduced motion removes all introduction, image/copy transforms and pinning. It displays all three biography chapters and all three projects as ordinary content, including every detail link. Without JavaScript the same complete content is available; enhancement controls remain hidden.

Validation: actual desktop forward/reverse scrolling, 0/1/2 chapter states, refresh at y=1445, fast skip/return, resize, mouse selection and keyboard selection; phone menu/Escape/focus, 320/375/390/768/1024/1280/1440px layouts; Chrome emulated touch swipe both directions and vertical scrolling; desktop/mobile reduced motion. The in-app browser could not dispatch touch events, so this specific check was completed in native Chrome's phone emulation. Physical devices were not tested. A 15-second GIF is encoded from the actual browser screencast frames, not staged screenshots. Artifacts are in ignored `output/home-interactions/`.
