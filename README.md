# JasonQSY.github.io

This is [@JasonQSY](https://jasonqsy.github.io)'s blog.

## Installation

### By `pip`

We solve dependencies with `pip`.

```bash
pip install pelican
pip install Markdown
pip install typogrify
pip install beautifulsoup4
pip install ghp-import2
```

### By `pyenv`

In this way, we need `pyenv` and `pyenv-virtualenv`.

```bash
pyenv install 3.6.0
pyenv virtualenv 3.6.0 blog
pyenv global blog
pip install pelican Markdown typogrify beautifulsoup4 ghp-import2
```

## Usage

The main branch is the `develop` branch. Write `*.md` in `/content` of develop branch. In order to preview,

```bash
make html
make serve
```

In order to publish

```bash
make github
```

and contents will automatically push to the `master` branch. Meanwhile, you may also want to commit the latest change to the `develop` branch if the website seems okay. To achieve this, type

```bash
make commit
```

## Reference

The website is powered by Pelican including its theme `elegant` and the plugin `render_math`. Note that their code in this repo may not be corresponding to the original one since I make some changes to fit my blog better.

- [Pelican](https://github.com/getpelican/pelican) the framework of static blog.
- [render_math](https://github.com/barrysteyn/pelican_plugin-render_math) enable mathjax support.
- [pelican-elegant](https://github.com/talha131/pelican-elegant) the theme
