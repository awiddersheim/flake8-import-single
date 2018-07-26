import ast
import os

import pytest

from flake8_import_single.linter import ImportFinder
from flake8_import_single.linter import Linter


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


def get_errors(errors):
    results = []

    for error in list(errors):
        assert len(error) == 4
        assert error[2] == 'IS001 found multiple imports on a single line.'
        assert error[3] == Linter

        results.append((error[0], error[1]))

    return results


def test_okay(parser):
    linter = Linter(load_test_case('okay.py'))

    assert not list(linter.run())


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
    linter = Linter(load_test_case(example))

    assert get_errors(linter.run()) == [
        (2, 0),
    ]


def test_multiple_errors(parser):
    linter = Linter(load_test_case('multiple_errors.py'))

    assert get_errors(linter.run()) == [
        (2, 0),
        (9, 0),
        (12, 0),
    ]
