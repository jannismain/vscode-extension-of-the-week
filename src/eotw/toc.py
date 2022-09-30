#!/usr/bin/env python3

import pathlib
import datetime
import re
from typing import Tuple
import frontmatter

from eotw import get_template
from eotw.cli import app

MARKER = "<!-- toc-begin -->{}<!-- toc-end -->"
PATTERN = MARKER.format(r"(.|\n)*")


@app.command(name="update-toc")
def update(
    posts: pathlib.Path,
    toc_file="README.md",
    target=None,
    strip_labels=("vscode",),
    url_ref="{fp_markdown}",
    backup_original: bool = True,
):
    if target is None:
        target = toc_file
    posts_metadata = []
    years = sorted([d.name for d in posts.glob("*") if d.is_dir()], reverse=True)
    for post in sorted(posts.glob("*/*.md"), key=lambda x: x.name, reverse=True):
        fm = frontmatter.load(post).to_dict()
        if "labels" in fm:
            fm["labels"] = [label for label in fm["labels"] if label not in strip_labels]
        if "links" in fm:
            fm["links"] = [
                f"[![][{name[1:-1]}]]({url})" if name[0] == ":" else f"[{name}]({url})"
                for name, url in fm["links"].items()
            ]
        posts_metadata.append(
            {
                "year": post.parent.name,
                "week": post.name[0:2],
                "extension": fm["title"][4:],
                "fn_markdown": post.name,
                "fp_markdown": post.relative_to(post.parent.parent.parent),
                **fm,
            }
        )
    toc = get_template("toc").render(
        {
            "posts": posts_metadata,
            "years": years,
            "ref": url_ref,
        }
    )
    with open(toc_file) as fp:
        in_toc = False
        readme_content = fp.read()
        result = re.search(PATTERN, readme_content)
        readme_new = re.sub(
            pattern=r"<!-- toc-begin -->(.|\n)*<!-- toc-end -->",
            repl=MARKER.format(f"{toc}"),
            string=readme_content,
        )

    if readme_new != readme_content:
        if backup_original and toc_file == target:
            # save previous README file as backup, in case something goes wrong.
            pathlib.Path(toc_file).rename(f"{toc_file}.{datetime.datetime.now().isoformat()}")
        with open(target, "w") as fp:
            fp.write(readme_new)
        print(f"toc has been updated!")
        exit(0)
    else:
        print(f"toc has not changed!")
        # even if toc didn't change, write file to target location
        if toc_file != target:
            with open(target, "w") as fp:
                fp.write(readme_new)
            print(f"{toc_file} has been copied to {target}")
    exit(1)
