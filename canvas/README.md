# Canvas source text

Text pasted into Canvas by hand: the course page blurb and the 14 lab assignment
descriptions. Kept here so Canvas content is version controlled alongside the site it
points at, and so the two stay consistent when links or wording change.

Nothing in this directory is published. `_quarto.yml` restricts `project.render` to
`.qmd` and `.ipynb`, so these files never reach the website or its search index.

## Files

| File | Purpose |
|---|---|
| `course-page-blurb.md` | Course description, where things live, syllabus pointer, course website section |
| `assignment-descriptions.md` | Name and description for each of the 14 lab assignments |
| `assignment-descriptions.docx` | Generated from the markdown, for pasting into Canvas with live links |

## Regenerating the Word file

The `.docx` is generated and is not tracked; `.gitignore` excludes `*.docx` repository-wide.
After editing the markdown:

```bash
pandoc canvas/assignment-descriptions.md -o canvas/assignment-descriptions.docx --standalone
```

Pasting from Word into the Canvas rich-text editor preserves the hyperlinks. If Word's fonts
and spacing come across too, paste with Cmd+Shift+V and re-add the links by hand.
