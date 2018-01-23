---
layout: post
title:  "Add C++ Kernel for Jupyter Notebook"
date:   2017-04-01
categories: system
---

Sometimes, we want an interactive `C` or `C++` to test command. Here is the guide to add a `C++` kernel to jupyter notebook.

## Environments

- Mac OS X
- `pyenv` + `virtualenv` for a fresh `python3` environment.

## Cling

Cling is an interactive intepreter for `C++`. The guide is actually based on cling.

```bash
# Download a cling binary
wget https://root.cern.ch/download/cling/cling_2017-03-30_mac1012.tar.bz2

# unzip
tar -xvf cling_2017-03-30_mac1012.tar.bz2

# move to a suitable location
mv cling_2017-03-30_mac1012.tar.bz2 ~/local/cling

# softlink cling
ln -s ~/local/cling/bin/cling ~/bin/cling
```

You need change the location yourself. After that, `cling` is included in `PATH` and we can type

```bash
cling --version
```

to test it.

## python

We use `pyenv` to create a fresh python env.

```bash
pyenv global 3.6.0
pyenv virtualenv cpp
pyenv global cpp
pip install jupyter
```

Now we can type

```bash
jupyter notebook
```

and it should have a python kernel.

## C++ Kernel

`Cling` itself has a jupyter notebook kernel.

```bash
cd ~/local/cling/share/cling/Jupyter/kernel
pip install .

# You need choose the version you want.
jupyter kernelspec install cling-cpp14
```

Now you can use it.

## Reference

- [Cling](https://github.com/root-project/cling)
- [Cannot install Cling kernel into a virtualenv Jupyter application](https://github.com/root-project/cling/issues/1)
