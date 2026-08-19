#!/usr/bin/env python3
"""Generate the weekly companion notebooks from the Python lecture decks.

The decks are the single source. Each ``weeks/weekNN-notebook.ipynb`` is generated
output and must never be edited by hand: run this script instead.

Speaker notes are instructor-only and are stripped by ``slides/strip-notes.lua``.
This script re-checks every generated file and fails if any survive.

Usage:
    python3 scripts/build-notebooks.py          # all Python weeks
    python3 scripts/build-notebooks.py 03 05    # only these weeks
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT / "slides"
WEEKS = ROOT / "weeks"

# Weeks that ship a companion notebook. Rust weeks (09-14) do not.
PYTHON_WEEKS = ("02", "03", "04", "05", "06", "07", "08")

KERNELSPEC = {"display_name": "Python 3", "language": "python", "name": "python3"}
LANGUAGE_INFO = {
    "codemirror_mode": {"name": "ipython", "version": 3},
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.12",
}
FORBIDDEN = ("TEACHING NOTES", "::: {.notes}", "::: notes")
MIN_CODE_CELLS = 2  # a deck whose fences were never made executable yields one markdown cell


def deck_for(week: str) -> Path:
    matches = sorted(SLIDES.glob(f"IS4010_W{week}_*.qmd"))
    if len(matches) != 1:
        sys.exit(f"expected exactly one deck for week {week}, found {matches}")
    return matches[0]


def build(week: str) -> None:
    deck = deck_for(week)
    target = WEEKS / f"week{week}-notebook.ipynb"

    # Quarto resolves -o against the project output-dir, so render then move.
    subprocess.run(
        ["quarto", "render", str(deck.relative_to(ROOT)), "--to", "ipynb",
         "-o", target.name, "--metadata", 'filters:["strip-notes.lua"]'],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    produced = next(
        (p for p in (ROOT / "_site" / target.name, deck.with_name(target.name)) if p.exists()),
        None,
    )
    if produced is None:
        sys.exit(f"week {week}: quarto did not produce {target.name}")

    nb = json.loads(produced.read_text())
    nb.setdefault("metadata", {})["kernelspec"] = dict(KERNELSPEC)
    nb["metadata"]["language_info"] = dict(LANGUAGE_INFO)

    text = "".join("".join(c["source"]) for c in nb["cells"])
    for marker in FORBIDDEN:
        if marker in text:
            sys.exit(f"week {week}: instructor speaker notes leaked into {target.name}")

    code_cells = sum(1 for c in nb["cells"] if c["cell_type"] == "code")
    if code_cells < MIN_CODE_CELLS:
        sys.exit(
            f"week {week}: only {code_cells} code cells. The deck's fences are probably still "
            "```python rather than ```{python}, which gives a single markdown cell."
        )

    target.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
    produced.unlink()
    print(f"  week{week}: {len(nb['cells'])} cells, {code_cells} code -> {target.relative_to(ROOT)}")


def main() -> None:
    weeks = sys.argv[1:] or list(PYTHON_WEEKS)
    unknown = [w for w in weeks if w not in PYTHON_WEEKS]
    if unknown:
        sys.exit(f"not Python weeks: {unknown}")
    if not shutil.which("quarto"):
        sys.exit("quarto not found on PATH")
    print(f"generating {len(weeks)} notebook(s)")
    for week in weeks:
        build(week)


if __name__ == "__main__":
    main()
