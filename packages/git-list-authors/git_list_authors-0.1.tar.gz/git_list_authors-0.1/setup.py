# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_list_authors']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['git-list-authors = git_list_authors.main:main']}

setup_kwargs = {
    'name': 'git-list-authors',
    'version': '0.1',
    'description': 'Git plugin for listing authors of all commits by file.',
    'long_description': '<!--\nSPDX-FileCopyrightText: 2024 Michael Pöhn <michael@poehn.at>\nSPDX-License-Identifier: GPL-3.0-or-later\n-->\n\n# git-list-authors\n\nCLI tool for listing git committers by file.\n\nNote: since this is always scanning the full git history, expect some waiting\ntimes when using on repositories with lots of commits.\n\n## usage\n\nusage and output example:\n\n```\n$ git list-authors README.md some/other.file\n\nREADME.md:\n    2020 Carl Contributor <carl@example.com>\n    2021 Grammer Prof <gp@example.com>\n\nsome/other.file:\n    2020 Carl Contributor <carl@example.com>\n\n```\n',
    'author': 'Michael Pöhn',
    'author_email': 'michael@poehn.at',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
