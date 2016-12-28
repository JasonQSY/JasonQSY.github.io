# jasonqsy-blog

This is [@JasonQSY](http://blog.jasonqian.me/)'s blog.

## Installation

We solve dependencies with `pip`.

```
pip install pelican
pip install Markdown
pip install typogrify
pip install beautifulsoup4
```

## Usage

Write `*.md` in `/content`. In order to preview,

```
make html
make serve
```

> Maybe some problem now, TODO

In order to publish

```
make publish
```

and push to this repo.

## Reference

Note that I may make several changes on them.

- [Pelican](https://github.com/getpelican/pelican) the framework of static blog.
- [render_math](https://github.com/barrysteyn/pelican_plugin-render_math) enable mathjax support.
- [pelican-elegant](https://github.com/talha131/pelican-elegant) the theme
