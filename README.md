# Flake8 Single Line Import Plugin

A Flake8 plugin that requires single line imports. For example, the
following will result in an error:

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
3.5.0 (import-single: 0.0.1, mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.6.0)
```

## Thanks

Much thanks goes out to [flake8-print][flake8-print] as the basis for
this plugin.

[flake8-print]: https://github.com/JBKahn/flake8-print
