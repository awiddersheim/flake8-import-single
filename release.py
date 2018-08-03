#!/usr/bin/env python

import os
import subprocess

from github import Github


def run_command(command):
    return subprocess.check_output(
        command,
        shell=True
    ).strip().decode('utf-8')


github = Github(os.environ['GITHUB_TOKEN'])

repo = github.get_user().get_repo(
    run_command('python setup.py --name'),
)

tag = run_command('python setup.py --version')

repo.create_git_release(
    tag=tag,
    name=tag,
    message=run_command(
        'git show --no-patch --pretty=format:"%s%n%b" {}'.format(
                os.environ['CIRCLE_SHA1'],
            ),
        ),
    draft=True,
    prerelease=os.environ.get('CIRCLE_TAG') is None,
    target_commitish=os.environ.get('CIRCLE_TAG', os.environ['CIRCLE_SHA1'])
)
