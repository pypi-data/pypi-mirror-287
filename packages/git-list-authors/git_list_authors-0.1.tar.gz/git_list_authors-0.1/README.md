<!--
SPDX-FileCopyrightText: 2024 Michael Pöhn <michael@poehn.at>
SPDX-License-Identifier: GPL-3.0-or-later
-->

# git-list-authors

CLI tool for listing git committers by file.

Note: since this is always scanning the full git history, expect some waiting
times when using on repositories with lots of commits.

## usage

usage and output example:

```
$ git list-authors README.md some/other.file

README.md:
    2020 Carl Contributor <carl@example.com>
    2021 Grammer Prof <gp@example.com>

some/other.file:
    2020 Carl Contributor <carl@example.com>

```
