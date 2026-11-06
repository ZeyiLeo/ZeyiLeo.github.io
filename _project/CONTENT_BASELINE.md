# Effective content audit

Method: `distinct-body-v1`. Frozen baseline: 2026-11-05T16:59:07+08:00.

Baseline: **1611 distinct body words**. Required final total: **6444 words** (4× baseline; new content must be at least 3× baseline).

| Page | Before words | After words | Before modules | After modules | New heading/topic groups |
| --- | ---: | ---: | ---: | ---: | --- |
| `/` | 320 | 320 | 8 | 8 |  |
| `/about/` | 163 | 163 | 5 | 5 |  |
| `/projects/` | 92 | 92 | 8 | 8 |  |
| `/experience/` | 255 | 255 | 8 | 8 |  |
| `/photography/` | 23 | 23 | 1 | 1 |  |
| `/writing/` | 23 | 23 | 1 | 1 |  |
| `/projects/digital-system/` | 98 | 98 | 3 | 3 |  |
| `/projects/ecommerce-brand/` | 106 | 106 | 3 | 3 |  |
| `/projects/hku-academy/` | 102 | 102 | 3 | 3 |  |
| `/projects/nursing-forum/` | 85 | 85 | 4 | 4 |  |
| `/projects/orbis-glaucoma/` | 146 | 146 | 6 | 6 |  |
| `/projects/public-speaking/` | 90 | 90 | 3 | 3 |  |
| `/projects/u21-ipe/` | 108 | 108 | 3 | 3 |  |
| **Total, globally deduplicated** | **1611** | **1611** | **56** | **56** | |

## Fixed counting rules

- **scope:** Main content of Home, About, Projects index/all project case routes, Experience, Photography, Writing index/all Writing article routes. CV, contact, legacy and 404 excluded.
- **eligible tags:** ['blockquote', 'dd', 'figcaption', 'li', 'p']
- **minimum body block words:** 8
- **word rule:** Unicode alphanumeric tokens; internal apostrophes/hyphens remain one token. Headings and alt text are not counted.
- **hidden content:** Unique content in hidden tabs/details is counted once; hidden state never removes real content from this audit.
- **exclusions:** Navigation/footer/buttons/TOC/status/role/date/eyebrow labels, explicit UI instructions/placeholders and data-content-ignore/data-animation-copy regions.
- **deduplication:** Across all measured pages in fixed route order: exact normalised paragraph/sentence duplicates removed. Sentences with at least 12 words also removed at >=90% token-sequence similarity, with comparable length and >=75% token-set overlap.
- **modules:** Each nearest article/section/details container plus preceding content heading with at least one accepted body block. Titles themselves add no words. Structural heading changes alone do not prove a new editorial topic.
- **limitation:** Same-word or near-copy inflation is suppressed; semantic information value and unsupported facts still require editorial review. The audit does not count photographs themselves as words.

Full accepted/excluded body text, module assignments, source HTML hashes and sentence-level decisions are retained in the JSON audit. Frozen source HTML is in ignored `output/product-iteration/baseline/`. A module count is a structural aid, not a substitute for reviewing unique information. New draft status and factual sources must be documented separately in the content inventory.
