# ZEYILEO | Digital Identity

Zeyi Li / Z.Y. Lee / Leo — **HKUMed Bachelor ’29**.

Healthcare × Communication × Business × Technology × Creative Work.

Personal website: https://zeyileo.github.io/

Canonical source: https://github.com/ZeyiLeo/ZeyiLeo.github.io

The active website is a lightweight Jekyll site in `site/`. It replaces the al-folio presentation while retaining Jekyll and the existing GitHub Pages destination. Historical theme files at the repository root are outside the configured Jekyll source and are not published. Do not edit those retired files to update the live experience.

## Local setup

Use Ruby 3.3.6 and the Bundler version recorded in `Gemfile.lock`:

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

Preview: http://127.0.0.1:4173/ . The existing system Ruby or Node installation may be different; use a working Ruby environment. The active site has no Node build requirement, third-party JavaScript, remote fonts, analytics, or runtime API dependency.

## Content updates

- Pages: `site/*.html`.
- Case studies: `site/_projects/*.md`, with category filters, order, approved image, and role in front matter.
- Navigation, professional links, and journal captions: `site/_data/`.
- Design: `site/assets/css/identity.css`; interactions: `site/assets/js/identity.js`.
- Images: approved WebP variants in `site/assets/img/`; preserve provenance in `CONTENT_INVENTORY.md` and strip EXIF when adding derivatives.
- All public CV facts: **`site/_data/cv.json`**. This is shared by the online CV, experience page, and PDF generator. Never maintain a second independent CV.

After editing CV records:

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/generate_cv.py
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
```

Render both PDF pages and review their layout after regeneration. Check the corresponding project narrative when changing a fact used in a case study. The PDF contains a fingerprint of the exact CV data, and validation rejects a stale download.

## Validation and publication

`scripts/check_site.py` checks internal links and anchors, all seven case pages, page headings, image alt attributes, exclusion of internal/template files, and online/PDF content parity. Browser checks are also required for UI changes: desktop/mobile layouts, menu, filters, themes, details, lightbox, keyboard access, and reduced motion.

The production workflow is `.github/workflows/deploy.yml`. Pull requests build and validate without deploying. Pushes to `master` or `main` and manually dispatched runs deploy `_site/` to the existing `gh-pages` branch. Deployment access is unchanged. Review and owner authorization are required before a public release. A successful local build is not proof of a completed GitHub Pages deployment.

## Project continuity

Read `AGENTS.md`, `_project/BRIEF.md`, `_project/STATUS.md`, and the latest `_project/CHANGELOG.md` entry at session start. Additional references:

- [Design system](DESIGN_SYSTEM.md)
- [Content inventory](CONTENT_INVENTORY.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

Only `site/` is emitted. Project notes are excluded from website output, but repository files can still be public. Keep original private CVs, phone numbers, unpublished media, evidence, and credentials outside this repository.
