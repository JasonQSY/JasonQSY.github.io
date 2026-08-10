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

## Deploy

Just push to the Github repo.

## Reference

The website is powered by Jekyll.

- [Jekyll](https://jekyllrb.com). The framework.
