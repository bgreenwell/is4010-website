# TODO: IS 4010 Course Website Enhancements

This file tracks planned refinements and enhancements for the IS 4010 website repository.

## Curriculum & Content
- [ ] **Rust Content Parity (Weeks 09–14)**:
    - [ ] Update introductions and reading lists for Rust modules.
    - [ ] Add links to interactive examples in the [Rust Playground](https://play.rust-lang.org/).
    - [ ] Create a "Rust for Pythonistas" guide in `resources/rust-for-python.qmd`.
- [ ] **AI Co-Pilot Resource Center**:
    - [ ] Create a `resources/prompt-library.qmd` with optimized prompts for coding, debugging, and refactoring.
    - [ ] Add a page on AI Ethics and Disclosure guidelines for student submissions.
- [ ] **Interactive Self-Checks**:
    - [ ] Add collapsible "Knowledge Check" quizzes at the end of module pages.
    - [ ] Explore [Shinylive/Pyodide](https://quarto-ext.github.io/shinylive/) for live in-browser Python code blocks.

## Design & Branding
- [ ] **Visual Identity**:
    - [ ] Implement custom UC brand colors (Red: `#E01222`, Black: `#000000`) via a custom SCSS theme or `styles.css`.
    - [ ] Add high-resolution Lindner and UC logos to the footer and sidebar header.
- [ ] **Project Showcase**:
    - [ ] Create a `projects/gallery.qmd` to showcase high-quality student projects and provide inspiration.

## Maintenance
- [ ] **Automated Slide Management**:
    - [x] (Implemented) Automate rendering of Reveal.js slides in CI/CD.
    - [ ] Add automated generation of PDF versions of slides for offline study.
- [ ] **Link Checking**:
    - [x] (Implemented) Add automated link checking to ensure all external resources are reachable.
