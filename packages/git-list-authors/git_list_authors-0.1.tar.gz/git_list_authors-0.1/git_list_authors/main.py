#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Michael Pöhn <michael@poehn.at>
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import shutil
import argparse
import datetime
import subprocess


def main():
    p = argparse.ArgumentParser(
        description="Go through the entire git history of a git repository "
        "checkout and list contributors of files. (Note: Adding or editing a "
        "file in git doesn't necessarily imply authorship.)"
    )
    p.add_argument(
        "FILE",
        nargs="*",
        help="select for which files you'd like to see git authorship info",
    )
    p.add_argument(
        "--all",
        "-a",
        default=False,
        action="store_true",
        help="show authorship info for all files",
    )
    p.add_argument(
        "--yaml",
        default=False,
        action="store_true",
        help="do a full dump of pared information in yaml format",
    )
    args = p.parse_args()

    if not args.FILE and not args.all:
        print("error: supply either FILE(s) you're interested in, or `--all`")
        sys.exit(69)

    git_bin = shutil.which("git")
    if not git_bin:
        print(
            "error: can't find git executable, make sure it's installed (e.g.: apt install git)"
        )
        sys.exit(69)

    try:
        subprocess.check_call(
            [git_bin, "status"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except:
        print("error: not a git repository")
        sys.exit(69)

    finds = {}
    git_commits = [
        x
        for x in str(
            subprocess.check_output([git_bin, "rev-list", "HEAD"]), encoding="utf8"
        ).split("\n")
        if x
    ]

    for c in git_commits:
        if c == git_commits[-1]:
            # initial commit needs special treatment, because git ... :/
            changed_files = [
                x
                for x in str(
                    subprocess.check_output(
                        [git_bin, "ls-tree", "-r", "--name-only", git_commits[-1]]
                    ),
                    encoding="utf8",
                ).split("\n")
                if x
            ]
        else:
            changed_files = [
                x
                for x in str(
                    subprocess.check_output(
                        [git_bin, "diff-tree", "--no-commit-id", "--name-only", "-r", c]
                    ),
                    encoding="utf8",
                ).split("\n")
                if x
            ]
        # print(c, changed_files)
        for f in changed_files:
            if args.all or f in args.FILE:
                if f not in finds:
                    finds[f] = []
                finds[f].append({"ref": c})

    for ffind in finds.values():
        for find in ffind:
            find["author"] = str(
                subprocess.check_output(
                    [git_bin, "log", "--format=%an", "-n", "1", find["ref"]]
                ),
                encoding="utf8",
            ).strip()
            find["date"] = datetime.datetime.fromisoformat(
                str(
                    subprocess.check_output(
                        [git_bin, "log", "--format=%ai", "-n", "1", find["ref"]]
                    ),
                    encoding="utf8",
                ).strip()
            )
            find["email"] = str(
                subprocess.check_output(
                    [git_bin, "log", "--format=%ae", "-n", "1", find["ref"]]
                ),
                encoding="utf8",
            ).strip()

    if args.yaml:
        try:
            import yaml
        except:
            print("error: could not import yaml module (e.g.: `pip install PyYAML`)")
            sys.exit(69)
        print(yaml.dump(finds))
    else:
        for filename, commits in finds.items():
            authors = {}
            for commit in commits:
                if commit["author"] not in authors:
                    authors[commit["author"]] = {
                        "email": commit["email"],
                        "years": set(),
                    }
                authors[commit["author"]]["years"].add(str(commit["date"].year))
            print(f"\n{filename}:")
            author_lines = []
            for name, d in authors.items():
                author_lines.append(
                    "{} {} <{}>".format(", ".join(sorted(d["years"])), name, d["email"])
                )
            for author_line in sorted(author_lines):
                print("   ", author_line)
        print()


if __name__ == "__main__":
    main()
