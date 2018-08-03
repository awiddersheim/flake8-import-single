#!/usr/bin/env python

import os
import subprocess

from github import Github


github = Github(os.environ['GITHUB_TOKEN'])

repo = github.get_user().get_repo(
    os.path.basename(
        os.path.dirname(
            os.path.realpath(__file__),
        ),
    ),
)

tag = subprocess.check_output(
    'python setup.py --version',
    shell=True,
).strip().decode('utf-8')

repo.create_git_release(
    tag=tag,
    name=tag,
    message=subprocess.check_output(
        'git show --no-patch --pretty=format:"%s%n%b" {}'.format(
                os.environ['CIRCLE_SHA1'],
            ),
            shell=True,
        ).strip().decode('utf-8'),
    draft=True,
    prerelease=os.environ.get('CIRCLE_TAG') is None,
    target_commitish=os.environ.get('CIRCLE_TAG', os.environ['CIRCLE_SHA1'])
)
