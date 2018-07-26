import ast
import os

import pytest

from flake8_import_single.linter import ImportFinder


@pytest.fixture()
def parser():
    return ImportFinder()


def load_test_case(filename):
    path = os.path.join(
        os.path.dirname(__file__),
        'test_cases',
        filename,
    )

    with open(path) as f:
        data = f.read()

    return ast.parse(data, path)


def test_okay(parser):
    parser.visit(load_test_case('okay.py'))

    assert not parser.errors


@pytest.mark.parametrize(
    'example',
    [
        'multiple_import.py',
        'multiple_import_with_parens1.py',
        'multiple_import_with_parens2.py',
        'multiple_import_with_slashes1.py',
        'multiple_import_with_slashes2.py',
    ],
)
def test_single_error(example, parser):
    parser.visit(load_test_case(example))

    assert len(parser.errors) == 1
    assert (2, 0) in parser.errors


def test_multiple_errors(parser):
    parser.visit(load_test_case('multiple_errors.py'))

    assert len(parser.errors) == 3
    assert (2, 0) in parser.errors
    assert (9, 0) in parser.errors
    assert (12, 0) in parser.errors
