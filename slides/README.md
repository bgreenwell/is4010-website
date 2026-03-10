# Slides

This directory contains the Quarto (`.qmd`) source files for all course lecture slides.

## Rendering all slides to HTML

To generate individual, self-contained HTML presentations for each slide deck (for distribution on Canvas), run the following command from within this `slides/` directory.

```bash
quarto render . --output-dir html
```

This will create a new `html/` subdirectory and place all the rendered `.html` presentation files inside it.

### For macOS or Linux

```bash
cat *.qmd > combined_slides.md
```

### For Windows (PowerShell)

```powershell
Get-Content -Path *.qmd | Set-Content -Path combined_slides.md
```

