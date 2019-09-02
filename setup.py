import io

from setuptools import find_packages
from setuptools import setup


def local_scheme(version):
    from pkg_resources import iter_entry_points

    # NOTE(awiddersheim): Modify default behaviour slightly by not
    # adding any local scheme to a clean `master` branch.
    if version.branch == 'master' and not version.dirty:
        return ''

    for item in iter_entry_points(
        'setuptools_scm.local_scheme',
        'node-and-timestamp',
    ):
        return item.load()(version)


with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='flake8-import-single',
    use_scm_version={
        'git_describe_command': 'git describe --dirty --tags --long --match "v*.*" --exclude "*.dev*" --first-parent',
        'local_scheme': local_scheme,
        'write_to': 'flake8_import_single/version.py',
    },
    setup_requires=[
        'setuptools_scm',
    ],
    author='Andrew Widdersheim',
    author_email='amwiddersheim@gmail.com',
    url='https://github.com/awiddersheim/flake8-import-single',
    description='Flake8 plugin that requires single line imports',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Operating System :: OS Independent',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
)
