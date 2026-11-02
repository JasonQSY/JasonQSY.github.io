# JasonQSY.github.io

My personal website has been rewritten. It has been migrated from pelican to Jekyll. The old code can be found at `legacy` branch.

## Environment

The site uses Ruby 4, Bundler 4, and Jekyll 4.

On mac, 

```bash
brew install ruby # you may need to add ruby to PATH
bundle config set --local path 'vendor/bundle'
bundle install
```

On ubuntu, refer to https://jekyllrb.com/docs/installation/ubuntu/.

Install Ruby 4 and Bundler 4 using your preferred Ruby version manager, then run:

```bash
bundle config set --local path 'vendor/bundle'
bundle install
```

## Development

```bash
bundle exec jekyll serve --config _config.yml
```

## Content

News and publications are data-driven: edit `_data/news.yml` (news items) and `_data/publications.yml` (publications), rendered by `_includes/publication.html`. Do not hand-edit the News and Publications sections in `index.html`; they are loops over the data files. Work Experience and Teaching are still written directly in `index.html`.

Images live in `resources/` and `static/`. Keep their filenames and formats stable so existing references keep working.

## Deploy

Pushing to `master` triggers the CI workflow (`.github/workflows/ci.yml`), which builds the site with `bundle exec jekyll build --strict_front_matter`, and GitHub Pages deploys the result. Changes should go through a pull request for review, not a direct push to `master`.

## Reference

The website is powered by Jekyll.

- [Jekyll](https://jekyllrb.com). The framework.
