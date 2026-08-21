# Agent context for the IS4010 course website

This repository is the public course website for **IS4010: AI-enhanced application development**, taught by Brandon M. Greenwell, PhD, at the University of Cincinnati. Treat this file as the definitive context and operating contract for work in this repository.

## Course model

IS4010 is a 14-week course built around modern software development with AI assistants as collaborators:

- Week 01: terminal basics, `uv`, Git, GitHub, and repository setup
- Week 02: browser AI chats, GitHub Copilot in VS Code, GitHub Copilot CLI, and Antigravity CLI
- Weeks 03–08: Python fundamentals and application development
- Weeks 09–14: Rust fundamentals and application development

`slides/IS4010_Advanced_AI_Workflows.qmd` is an optional appendix, not a fifteenth week. It is
linked from the Resources section of the sidebar and from the end of the Week 14 deck. Do not
reintroduce a Week 15 into the schedule, the navigation, or the slide filenames.

The course has 14 labs and one final solo project. There is no midterm. Students fork `bgreenwell/is4010-labs` in Lab 01 and use that single repository for the semester. Each lab is worth 10 points; a green badge in the repository README represents full credit.

Students are expected to install and try both Copilot CLI and Antigravity CLI in Week 02. After comparing them on the same task, they may use whichever combination of browser chat, Copilot in VS Code, Copilot CLI, and Antigravity CLI best fits their work.

## Source-of-truth boundaries

- **Official syllabus:** Simple Syllabus is authoritative, published at <https://uc.simplesyllabus.com/doc/mkhmypnvx/2026-Fall-IS-4010-%2822%29-001-%2810885%29-Application-Development-with-Artificial-Intelligence> for Fall 2026 section 001. `syllabus.qmd` is a convenience copy and must defer to it; never invent or infer a URL for a different term or section.
- **Course schedule and public teaching content:** The Quarto sources in this repository control the website.
- **Lab requirements and grading behavior:** `bgreenwell/is4010-labs` is authoritative.
- **Instructor implementations:** `bgreenwell/is4010-labs-solutions` is private and must never be exposed here.
- **Canvas handouts:** Sources and generated DOCX files live in the sibling `../is4010-canvas/` directory.

When a change affects both teaching content and a lab contract, update the public and private lab repositories first or alongside this website so instructions, tests, workflows, and examples remain aligned.

## Repository map

- `_quarto.yml`: website navigation, metadata, and global format configuration
- `index.qmd`: course landing page
- `syllabus.qmd`: link to the authoritative Simple Syllabus record plus a non-authoritative planning reference
- `project.qmd`: final solo project requirements
- `weeks/`: weekly module pages, plus `weekNN-notebook.ipynb` companion notebooks that are
  **generated** from the Python decks by `scripts/build-notebooks.py`. Never edit a notebook by
  hand; edit the deck and regenerate, or the next build silently discards the change
- `slides/`: Reveal.js lecture sources. Shared deck configuration lives in `slides/_metadata.yml`;
  per-deck front matter carries only `title`, `subtitle`, and `author`. Never add a `slides/_quarto.yml`,
  because a nested project there excludes the decks from the parent render and makes local
  output diverge from what CI publishes.
- `resources/`: setup, troubleshooting, and Python environment guides
- `_site/`: local render output. Ignored by Git; the publish workflow renders fresh from
  source and deploys that, so never commit it and never treat it as the published state
- `.github/workflows/publish.yml`: render, link-check, and GitHub Pages deployment workflow

The Week 01 instructor introduction should point to the instructor's GitHub profile README at <https://github.com/bgreenwell> rather than maintaining a separate biography in the deck.

## Current development standards

### Python

- Use Python 3.12 managed by [`uv`](https://docs.astral.sh/uv/).
- Use `uv sync --locked` to reproduce the course environment.
- Run scripts with `uv run python path/to/script.py`.
- Run tests with `uv run python -m pytest` or the lab-specific documented command.
- Use `uv add PACKAGE` in examples that intentionally add a dependency to a student's own project.
- Do not teach `pip install`, manual `venv` creation, environment activation, `requirements.txt`, or bare `python`/`pytest` commands as the course workflow.

### Rust

- Rust begins in Week 09; do not require its toolchain during Weeks 01–08.
- Use Cargo for builds, tests, formatting, and linting.
- Standard validation is `cargo test`, `cargo fmt --check`, and `cargo clippy -- -D warnings`.

### AI tools

- Browser chat may be ChatGPT, Gemini, Claude, or another suitable interface.
- GitHub Copilot is the editor assistant used in VS Code.
- The two course CLI agents are GitHub Copilot CLI (`copilot`) and Antigravity CLI (`agy`).
- Gemini CLI is not the individual-user course tool; Antigravity CLI replaced it.
- Link to current official setup documentation instead of copying installer commands that may become stale.
- Teach students to start agents inside the intended repository, review proposed commands, inspect `git diff`, and keep credentials out of prompts and committed files.

## Content conventions

1. Use sentence case for every title, heading, subheading, table label, and navigation label.
2. Maintain an encouraging, professional tone that treats AI as a collaborator while making the student responsible for the submitted result.
3. Prefer plain language and concrete, testable examples.
4. Keep terminology, commands, dates, lab names, and tool expectations consistent across the website, slides, notebooks, labs, and Canvas handouts.
5. Prefer authoritative documentation for setup and technical instructions.
6. Preserve accessible link text, image alt text, readable contrast, and sensible heading hierarchy.
7. Never include API keys, access tokens, passwords, private instructor material, or solution code.

## Editing workflow

1. Edit source files, not generated HTML, as the primary change.
2. Update every affected surface. A tooling change may require edits to setup resources, slides, notebooks, weekly pages, syllabus references, and Canvas sources.
3. Render the complete site from the repository root:

   ```bash
   quarto render
   ```

4. Inspect the rendered `_site/` changes and resolve errors or unexpected omissions.
5. For slide-specific work, confirm the relevant Reveal.js output renders correctly.
6. Run `git diff --check` and scan changed sources for stale commands, obsolete tool names, placeholders that should have been filled, credentials, and private content.
7. Commit source only. `_site/` is ignored.

Do not edit generated files under `_site/` as a substitute for changing their source. The publishing workflow renders the website and slides, runs a link checker, and deploys to GitHub Pages on pushes to `main`.

## Companion notebooks are generated from the decks

`slides/IS4010_W0{2..8}_*.qmd` are the single source for both the lecture slides and the weekly
notebooks. Four pieces make that work, and all four must stay in place:

- Code fences are ` ```{python} ` with `#| eval: false`. Quarto splits notebook cells at
  executable blocks, so a plain ` ```python ` fence collapses the whole deck into one markdown
  cell. `scripts/build-notebooks.py` fails rather than write such a notebook.
- `slides/_metadata.yml` sets `execute: enabled: false`. Without it every render, including the
  revealjs one, fails with `Jupyter is not available in this Python installation`.
- `slides/strip-notes.lua` drops `::: {.notes}` divs for every format except revealjs. Speaker
  notes are instructor-only; the build script re-checks each generated notebook and fails on any
  that survive.
- Notebook-only material, meaning the exercises and the header, lives in
  `::: {.content-visible when-format="ipynb"}` blocks so it never reaches the slides.

Regenerate with `python3 scripts/build-notebooks.py`, optionally naming weeks. The publish
workflow runs it before rendering and commits any changes back to `main`.

## GitHub Actions pinning policy

- `actions/checkout` stays on a major version tag. It is GitHub-owned and its tags are trusted.
- Every third-party action is pinned to a full commit SHA with the version in a trailing comment,
  so a moved tag cannot change what runs in the instructor repositories or in student forks.
- `dtolnay/rust-toolchain` is pinned to a `master` SHA with an explicit `toolchain: stable` input,
  which is that action's documented form for pinned use. Do not revert it to `@stable`; that is a
  moving branch reference on a third-party repository.
- When bumping an action, resolve the new SHA with
  `gh api /repos/OWNER/REPO/commits/TAG --jq .sha` and update the trailing version comment to match.

## Validation checklist

- `quarto render` completes successfully for the full 42-item project.
- `_site/` contains no HTML rendered from repository documentation. `_quarto.yml` restricts
  `project.render` to `**/*.qmd` and `**/*.ipynb` so that `AGENTS.md`, `CLAUDE.md`, `TODO.md`,
  and `README.md` are never published or indexed in `search.json`.
- Modified notebooks remain valid JSON.
- Changed slides render without missing assets.
- The Simple Syllabus link resolves and points at the correct term and section.
- Python examples use `uv` and Python 3.12 consistently.
- AI-tool references use Copilot CLI and Antigravity CLI consistently.
- Lab names, commands, and grading language match `is4010-labs`.
- `git diff --check` reports no whitespace errors.
- The GitHub Actions render, publish, and Pages deployment jobs pass after publishing.
- The link checker runs with `fail: false`, so it never fails the build. Read its output in the
  workflow log and fix broken links by hand; a green workflow is not evidence that links resolve.

## Related repositories and protected areas

- Public labs: <https://github.com/bgreenwell/is4010-labs>
- Private solutions: <https://github.com/bgreenwell/is4010-labs-solutions>
- Published website: <https://bgreenwell.github.io/is4010-website/>

Sibling `is4010-python*` and `is4010-rust*` repositories are legacy migration sources. Do not add current course content to them. The sibling `../archived/` directory is frozen and must not be edited.
