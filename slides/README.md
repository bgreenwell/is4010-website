# Slides

This directory contains the Quarto (`.qmd`) source files for all course lecture slides.

## Shared configuration

Every deck inherits its Reveal.js configuration from `_metadata.yml` in this directory:
theme, transition, slide numbers, chalkboard, footer, and `custom.css`. Per-deck front
matter should contain only `title`, `subtitle`, and `author`.

Do not add a `_quarto.yml` here. That would make this directory a nested project, which
excludes the decks from the parent website render and causes local and published output
to diverge.

## Rendering

The decks are part of the parent website project, so render from the repository root:

```bash
cd ..
quarto render
```

Output lands in `_site/slides/`. To render a single deck while iterating:

```bash
quarto render slides/IS4010_W03_Python_Basics.qmd
```
