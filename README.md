# IS 4010 course website

Quarto source for the public course website for IS 4010: Application Development with Artificial Intelligence at the University of Cincinnati.

- Weekly module pages for all 14 weeks
- Reveal.js lecture decks, one per week, plus an optional advanced AI workflows appendix
- Companion Jupyter notebooks for the Python weeks, generated from the decks
- Setup, troubleshooting, and AI tool guides
- Final solo project requirements

Published at <https://bgreenwell.github.io/is4010-website/>.

## Requirements

- [Quarto](https://quarto.org/docs/get-started/)
- Python 3.12, only for regenerating the companion notebooks

The site itself renders without executing code, so no Python environment is needed to build it.

## Building locally

```bash
# Render the full site to _site/
quarto render

# Live preview with reload on save
quarto preview

# Render a single deck
quarto render slides/IS4010_W03_Python_Basics.qmd
```

`_site/` is generated output and is not committed. The publish workflow renders fresh from source on every push to `main`.

## Companion notebooks

The Python decks in `slides/` are the single source for both the lecture slides and the weekly notebooks in `weeks/`. Never edit a notebook by hand, since the next build discards the change.

```bash
# Regenerate every Python week
python3 scripts/build-notebooks.py

# Regenerate specific weeks
python3 scripts/build-notebooks.py 03 05
```

## Layout

| Path | Contents |
| --- | --- |
| `_quarto.yml` | Navigation, metadata, and render configuration |
| `index.qmd`, `project.qmd` | Landing page and final project requirements |
| `weeks/` | Weekly module pages and generated notebooks |
| `slides/` | Reveal.js decks and their shared configuration |
| `resources/` | Setup, troubleshooting, packages, and AI tool guides |
| `canvas/` | Text pasted into Canvas by hand, versioned but never published |
| `scripts/` | Notebook build script |

## Related repositories

- Student labs: <https://github.com/bgreenwell/is4010-labs>
- Canvas modules: maintained in the sibling `is4010-canvas` directory

The official syllabus lives in Simple Syllabus and is linked from the sidebar. It is deliberately not duplicated here.

## Development

Edit source files rather than rendered HTML, then render and inspect the result before committing. A change to tooling or terminology usually touches several surfaces at once: slides, notebooks, weekly pages, setup resources, and the lab repository.

Commits follow [Conventional Commits](https://www.conventionalcommits.org/). Pushes to `main` trigger the render, link check, and GitHub Pages deployment in `.github/workflows/publish.yml`. The link checker does not fail the build, so read its output in the workflow log rather than trusting a green check.

`AGENTS.md` carries the full operating contract for this repository, including content conventions and the validation checklist. `CLAUDE.md` points to it.
