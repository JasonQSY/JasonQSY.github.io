# AGENTS.md

Instructions for AI agents working on this repository. The repository owner reviews all changes through pull requests.

## Workflow

- Work on a branch and open a pull request against `main`. Never push directly to `main`.
- Describe what changed and how it was verified in the pull request body.
- Do not commit generated output (`_site/`, `vendor/`); both are git-ignored.

## Build and verify

- Install dependencies with `bundle install`, then build with:

  ```bash
  bundle exec jekyll build --strict_front_matter
  ```

- The CI workflow (`.github/workflows/ci.yml`) runs the same build on pushes and pull requests to `main`, and GitHub Pages deploys `main`.
- When changing templates or data files, compare the rendered output against the previous build (page text, links, and images) and report any differences; whitespace-only differences are fine.

## Content

- News lives in `_data/news.yml`; publications live in `_data/publications.yml` and are rendered by `_includes/publication.html`. Edit the data files, not the loop sections in `index.html`.
- Work Experience and Teaching are still written directly in `index.html`.
- `AGENTS.md` itself is excluded from the built site (see `exclude` in `_config.yml`); it is contributor documentation, not a page.

## Images

- Optimize images losslessly only (for example `optipng` or `jpegoptim` with default settings). Do not change filenames or formats.
- Lossy compression and conversion to another format (for example WebP) require the owner's explicit approval, because they change rendered quality and every reference to the file.
- Verify optimized images are still valid and pixel-identical to the originals before opening a pull request.
