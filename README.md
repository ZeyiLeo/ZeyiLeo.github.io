# ZEYILEO | Digital Identity

Zeyi Li / Z.Y. Lee / Leo — **HKUMed Bachelor ’29**.

Healthcare × Communication × Business × Technology × Creative Work.

Personal website: https://zeyileo.github.io/

Canonical source: https://github.com/ZeyiLeo/ZeyiLeo.github.io

The active website is a lightweight Jekyll site in `site/`. It replaces the al-folio presentation while retaining Jekyll and the existing GitHub Pages destination. Historical theme files at the repository root are outside the configured Jekyll source and are not published. Do not edit those retired files to update the live experience.

## Current product iteration

The latest local review uses the owner-confirmed original headshot, grouped global navigation, four reversible material/context connections, and a layered Orbis/Speaking/Commerce browser. About, seven cases, experience, visual stories and three marked writing drafts provide deeper content. The old website is a content/photo provenance source only; Apple remains the interface reference. `home_profile.json`, `connections.json`, `mega_navigation.json`, `experience_notes.json`, `journal_stories.json` and `essays.json` provide structured content; native CSS/JS enhance shared templates. Reduced motion and no-JavaScript views expose all content.

The original finished CV stays unchanged. No CV generation step is part of the build. Current local review is at http://127.0.0.1:4173/ while its preview server is running. See `_project/STATUS.md` for current verification and publication state.

## Local setup

Use Ruby 3.3.6 and the Bundler version recorded in `Gemfile.lock`:

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

Preview: http://127.0.0.1:4173/ . The existing system Ruby or Node installation may be different; use a working Ruby environment. The site has no Node build requirement, remote font requests, analytics, or live API dependency. The desktop CV reader uses a self-hosted Mozilla PDF.js package, loaded only on desktop CV visits.

## Content updates

- Pages: `site/*.html`.
- Case studies: `site/_projects/*.md`, with category filters, order, approved image, and role in front matter.
- Navigation, professional links, and journal captions: `site/_data/`.
- Design: `site/assets/css/identity.css`; interactions: `site/assets/js/identity.js`.
- Images: approved WebP variants in `site/assets/img/`; preserve provenance in `CONTENT_INVENTORY.md` and strip EXIF when adding derivatives.
- Website experience records: `site/_data/experience.json`, used by the Experience page. These do not typeset or replace the CV.
- Original CV: **`site/assets/pdf/Zeyi_Li_CV.pdf`**, with immutable file metadata in `site/_data/cv_asset.json`.

## Original CV policy

Use the owner's original finished PDF as provided. Do not rewrite, redact, re-typeset, translate, or regenerate it. The previous two-page replacement and generation process are retired. Desktop CV display reads the original file through a self-hosted PDF reader; the open action provides a full-window view of that same file and download points directly to the original PDF. Phones prioritize full-size opening and download rather than an embedded window.

The current one-page original is 235520 bytes. SHA-256:

```text
156c588fa40dacefd97129154c3ef4adac1519d1665682bf844159fa0ea4b1b4
```

The reader's display scaling does not change PDF bytes. To replace the CV in a future authorized update, copy the new owner-approved original without modification and record its actual hash, byte count and page count. Do not edit the document to match website summaries.

```sh
python3 -m pip install -r scripts/requirements.txt
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
```

Mozilla PDF.js 6.5.438 is vendored under `site/assets/vendor/pdfjs/`, with Apache-2.0 license and source information. The library only reads the same-origin document locally; no CV is sent to another service. There is no PDF-generation script.

## Validation and publication

`scripts/check_site.py` checks internal links and anchors, all seven case pages, page headings, image alt attributes, exclusion of internal/template files, and exact original-PDF hash/size/page integrity. Browser checks are also required for UI changes: desktop/mobile layouts, menu, filters, scroll/intro/pinned motion, details, lightbox, keyboard access, and reduced motion.

The production workflow is `.github/workflows/deploy.yml`. The owner accepted the reviewed version and explicitly authorized publication on 2026-11-06; see `_project/STATUS.md` for actual release progress. Pull requests build and validate without deploying. Pushes to `master` or `main` and manually dispatched runs deploy `_site/` to the existing `gh-pages` branch. Deployment access is unchanged. Review and owner authorization are required before a public release. A successful local build is not proof of a completed GitHub Pages deployment.

## Project continuity

Read `AGENTS.md`, `_project/BRIEF.md`, `_project/STATUS.md`, and the latest `_project/CHANGELOG.md` entry at session start. Additional references:

- [Design system](DESIGN_SYSTEM.md)
- [Content inventory](CONTENT_INVENTORY.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

Only `site/` is emitted. Project notes are excluded from website output, but repository files can still be public. Keep unpublished media, private evidence, and credentials outside this repository. The owner explicitly authorized publishing the complete unchanged original CV, including its existing contacts, in the accepted 2026-11-06 release.


## Content growth audit

The baseline is frozen; do not recalculate it after edits. After a production build run `python3 scripts/measure_content.py --compare --require-target` to produce the per-page audit with the same exclusions/deduplication. The current baseline is 1,611 effective words, required final total 6,444. See `_project/CONTENT_GROWTH.md` and ignored `output/product-iteration/REVIEW.html` for the current review. The accepted release preserves the existing essay draft labels; the essays are not presented as past publications. Original CV verification is separate from content generation.
