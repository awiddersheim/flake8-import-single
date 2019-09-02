# Flake8 Single Line Import Plugin

A Flake8 plugin that requires single line imports.

[![PyPI version](https://img.shields.io/pypi/v/flake8-import-single.svg)]( https://pypi.org/project/flake8-import-single)
[![Python Versions](https://img.shields.io/pypi/pyversions/flake8-import-single.svg)](https://pypi.org/project/flake8-import-single)
[![Build Status](https://img.shields.io/circleci/project/github/awiddersheim/flake8-import-single/master.svg)](https://circleci.com/gh/awiddersheim/flake8-import-single)
[![License](https://img.shields.io/pypi/l/flake8-import-single.svg)](https://github.com/awiddersheim/flake8-import-single/blob/master/LICENSE)

## Introduction

The following will result in an error:

```
from foo import bar, baz
```

It should be rewritten as:

```
from foo import bar
from foo import baz
```

## Installation

```
$ pip install flake8-import-single
$ pip install --upgrade flake8-import-single
```

## Plugin for Flake8

```
$ flake8 --version
3.5.0 (flake8-import-single: 0.1.2, mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.6.0)
```

## Thanks

Much thanks goes out to [flake8-print][flake8-print] as the basis for
this plugin.

[flake8-print]: https://github.com/JBKahn/flake8-print
