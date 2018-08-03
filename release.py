#!/usr/bin/env python

import glob
import os
import subprocess
import sys

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

tag = 'v{}'.format(run_command('python setup.py --version'))

release = repo.create_git_release(
    tag=tag,
    name=tag,
    message=run_command(
        'git show --no-patch --pretty=format:"%s%n%b" {}'.format(
                os.environ['CIRCLE_SHA1'],
            ),
        ),
    prerelease=os.environ.get('CIRCLE_TAG') is None,
    target_commitish=os.environ.get('CIRCLE_TAG', os.environ['CIRCLE_SHA1'])
)

for item in glob.glob(sys.argv[1]):
    release.upload_asset(item)
