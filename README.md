# JasonQSY.github.io

My personal website has been rewritten. It has been migrated from pelican to Jekyll. The old code can be found at `legacy` branch.

## Environment

We need `ruby` and `gem`.

```bash
brew install ruby # you may need to add ruby to PATH
bundle config set --local path 'vendor/bundle'
gem install bundler jekyll
bundle install --path vendor/bundle # you may need to remove Gemfile.lock
```

## Development

```bash
bundle exec jekyll serve --config _config.yml
```

## Deploy

Just push to the Github repo.

## Reference

The website is powered by Jekyll.

- [Jekyll](https://jekyllrb.com). The framework.
