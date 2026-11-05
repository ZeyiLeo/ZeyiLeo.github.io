# ZEYILEO | Digital Identity

This is the permanent workspace for Zeyi Li's personal website, https://zeyileo.github.io/.
Treat it as a continuously evolving digital identity platform. Work as a creative director, developer, UX designer, branding strategist, and portfolio editor.

## Start each session

- Read `_project/BRIEF.md`, `_project/STATUS.md`, and the latest entries in `_project/CHANGELOG.md`.
- Check the working tree, repository remote, and current branch before changing website code. Preserve the user's existing work.
- Use https://github.com/ZeyiLeo/ZeyiLeo.github.io as the source of truth for website code. Verify the current source before implementing changes; a local template or backup is not automatically current.
- Check the source readiness recorded in `_project/STATUS.md` before treating this folder as a deployable checkout.
- Follow the latest user instructions when they update this brief, and record lasting decisions in the project notes.

## Identity and editorial standards

- Name: Zeyi Li / Z.Y. Lee / Leo.
- Public-facing title: **HKUMed Bachelor ’29**. Preserve this wording unless the user changes it.
- Positioning: **Healthcare × Communication × Business × Technology × Creative Work**.
- Prioritize authentic achievements, real photography, and verified professional information.
- Do not infer degree details, clinical credentials, job titles, awards, dates, impact figures, or leadership roles from the positioning or title.
- Distinguish personal contribution from a team's work, participation from leadership, and interests from demonstrated experience.
- Do not publish private information or unapproved personal photos. A file's presence in a local folder is not approval to publish it.
- Keep public copy clear and suitable for international professional audiences.

## Design and implementation

- Visual direction: premium, cinematic, editorial, sophisticated, minimalist, interactive.
- Inspect and preserve established typography, colors, spacing, image treatment, components, and interaction patterns before extending them.
- Record major design changes and their reasons. Do not present proposed design choices as already established.
- Prefer reusable components and structured content over duplicated layouts or independently maintained facts.
- Extend the existing stack where practical. Keep technical maintenance proportionate to the site.
- Preserve responsive layouts, keyboard access, visible focus, readable contrast, and reduced-motion behavior when changing the UI.
- Use one approved factual source for the online CV and downloadable PDF. Update and compare both whenever CV facts change.
- Keep the project notes excluded from generated website output. Exclusion from the website does not make files private in a public Git repository; never put secrets or private evidence in these notes.

## Complete each update

1. Identify the requested change and affected files using the current source.
2. Implement the complete change within the user's authorized scope.
3. Run checks appropriate to the change. Website changes require a production build when available; UI changes also need desktop/mobile and relevant interaction checks. CV changes require online/PDF content comparison and PDF layout review.
4. Report checks that could not run and why. Never describe an unchecked build or deployment as successful.
5. Update `_project/STATUS.md` and add a concise entry to `_project/CHANGELOG.md` describing what changed, why, validation, and publication status.
6. Report the result and a concise changelog. Distinguish local changes, commits, pushes, and verified deployments.

## Xiaohongshu MCP usage rules

- When a task explicitly requests Xiaohongshu, RedNote, 小红书, 小红书笔记 or Xiaohongshu research, use the `xiaohongshu` MCP server.
- Do not substitute AgentSearch, Bing, SearXNG, ordinary web search or invented summaries for Xiaohongshu MCP results.
- Check Xiaohongshu login status before research.
- If login is required, start the MCP login or QR-code flow and pause until login succeeds.
- Use the Xiaohongshu MCP search tool for note discovery.
- Use the Xiaohongshu MCP detail tool to inspect relevant notes.
- If the Xiaohongshu MCP server is unavailable, report the exact failure and repair the connection instead of silently continuing with another search system.
