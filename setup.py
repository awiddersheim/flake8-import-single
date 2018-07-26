import io

from setuptools import find_packages
from setuptools import setup


def clean_scheme(version):
    return '{}.{}'.format(version.tag, version.distance or 0)


with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='flake8-import-single',
    use_scm_version={
        'version_scheme': clean_scheme,
        'local_scheme': lambda *args, **kwargs: '',
        'write_to': 'flake8_import_single/version.py'
    },
    setup_requires=[
        'setuptools_scm',
    ],
    author='Andrew Widdersheim',
    author_email='amwiddersheim@gmail.com',
    description='Flake8 plugin that requires single line imports.',
    long_description=long_description,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'flake8',
    ],
    extras_require={
        'dev': [
            'flake8',
            'flake8-bandit',
            'flake8-commas',
            'flake8-import-order',
            'flake8-print',
            'flake8-quotes',
            'pytest',
            'pytest-cov',
            'pytest-sugar',
        ],
    },
    entry_points={
        'flake8.extension': [
            'IS = flake8_import_single.linter:Linter',
        ],
    },
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Operating System :: OS Independent'
    ],
)
