import io

from setuptools import find_packages
from setuptools import setup


def local_scheme(version):
    result = []

    if version.branch != 'master' or version.dirty:
        result.append('+{}'.format(version.node))

        result.append(
            '.d{}'.format(
                version.time.strftime('%Y%m%d%H%M%S'),
            ),
        )

    return ''.join(result)


with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='flake8-import-single',
    use_scm_version={
        # 'local_scheme': 'node-and-timestamp',
        'local_scheme': local_scheme,
        'write_to': 'flake8_import_single/version.py'
    },
    setup_requires=[
        'setuptools_scm',
    ],
    author='Andrew Widdersheim',
    author_email='amwiddersheim@gmail.com',
    url='https://github.com/awiddersheim/flake8-import-single',
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
