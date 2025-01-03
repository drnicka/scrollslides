# Presentation Slides

This repository contains markdown-based presentations using mkslides and reveal.js.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install mkslides
```

## Development

- Add markdown files to the `markdown_files` directory
- Run `python convert.py` to build the slides
- Run `python serve.py` to preview locally

## Deployment

The slides are automatically deployed to GitHub Pages when pushing to the main branch.
