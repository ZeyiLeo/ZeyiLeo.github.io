# Effective content audit

Method: `distinct-body-v1`. Frozen baseline: 2026-11-05T16:59:07+08:00.

Baseline: **1611 distinct body words**. Required final total: **6444 words** (4× baseline; new content must be at least 3× baseline).

Current total: **9058**. Added: **7447**. Final/baseline: **5.623×**. Target: **PASS**. Remaining word gap: **0**.

| Page | Before words | After words | Before modules | After modules | New heading/topic groups |
| --- | ---: | ---: | ---: | ---: | --- |
| `/` | 320 | 699 | 8 | 16 | Now, at HKU.; Work with a real setting.; Interests with a history.; Where the fields meet.; A subject becomes a public encounter.; The experience has an operational side.; A literary interest enters a conversation.; A launch is the start of an operating loop.; Three questions, taken a little further.; A message someone can use; What travels between languages; After the store goes live |
| `/about/` | 163 | 694 | 5 | 7 | A background with several points of view.; Here, now.; Before university, a wider set of interests.; Public expression, in different settings.; The detail behind an organised experience.; Business as an operating practice.; Questions I’m continuing to explore. |
| `/projects/` | 92 | 142 | 8 | 9 | Several routes through the work. |
| `/experience/` | 255 | 916 | 8 | 9 | Roles, in their working context.; The University of Hong Kong |
| `/photography/` | 23 | 924 | 1 | 11 | A frame. A wider story.; An outreach setting on campus; Information at a smaller scale; A demonstration as an opening; A contribution in a literary setting; Around the conversation; Gesture, microphone, audience; The collective setting of a forum; An HKU outreach moment; Read the setting and the detail.; Look a little closer. |
| `/writing/` | 23 | 81 | 1 | 2 | Questions worth staying with.; From a project to a question. |
| `/projects/digital-system/` | 98 | 510 | 3 | 7 | A website with several reading speeds; Interaction should reveal information; A maintainable factual record; Drafting is different from publication |
| `/projects/ecommerce-brand/` | 106 | 539 | 3 | 7 | Different stages, different decisions; Content and operations belong in the same picture; Reading a number with its boundary; An operating question for the writing room |
| `/projects/hku-academy/` | 102 | 485 | 3 | 7 | The participant journey has an administrative side; Working with records and discrepancies; Communication across working boundaries; Why this belongs beside speaking and outreach |
| `/projects/nursing-forum/` | 85 | 447 | 4 | 8 | A formal gathering, and its human flow; Hosting is one kind of communication; Support continues away from the microphone; The photograph as context |
| `/projects/orbis-glaucoma/` | 146 | 538 | 6 | 10 | Three ways into one subject; Planning an encounter, not only a poster; A communication question worth carrying forward; Continue through the material |
| `/projects/public-speaking/` | 90 | 463 | 3 | 7 | Two forms of public expression; Interest, preparation and the public occasion; What the photographs can add; A question beyond this event |
| `/projects/u21-ipe/` | 108 | 500 | 3 | 7 | A shared argument across disciplines; Research and recommendations have different jobs; A leadership role within collaborative work; Where the conversation continues |
| `/writing/execution-and-commerce/` | 0 | 682 | 0 | 7 | After the store goes live; A milestone changes the question; Separate three sentences; Make the next task small enough to understand; A ratio needs a business context; Content and fulfilment are connected, but distinct; Keep a record of the decision |
| `/writing/health-information/` | 0 | 726 | 0 | 7 | A message someone can use; Start with the encounter; Decide what the reader needs first; Give the formats different jobs; Preserve the distinction between an illustration and a conclusion; A next step should belong to the message; Leave room to listen |
| `/writing/languages-and-context/` | 0 | 712 | 0 | 7 | What travels between languages; Fluency does not settle every question; An explanation is also a choice; Keep a particular thing particular; An address and a conversation unfold differently; Images can offer context, with limits; A provisional standard for the conversation |
| **Total, globally deduplicated** | **1611** | **9058** | **56** | **128** | |

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
