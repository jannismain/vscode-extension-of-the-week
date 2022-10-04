#!/usr/bin/env python3

import datetime
import logging
import pathlib
import re
from enum import Enum

import frontmatter

from eotw import get_template
from eotw.cli import app

MARKER = "<!-- toc-begin -->{}<!-- toc-end -->"
PATTERN = MARKER.format(r"(.|\n)*")


class TocTemplate(str, Enum):
    toc = "toc"
    toc_multi = "toc_multi"


@app.command(name="update-toc")
def update(
    toc_file: pathlib.Path,
    posts: pathlib.Path,
    template: TocTemplate = "toc_multi",
    target=None,
    strip_labels=("vscode",),
    url_ref="{fp_markdown}",
    title_ref="{year}",
    backup_original: bool = True,
    pattern="*/*.md",
):
    if target is None:
        target = toc_file
    posts_metadata = []
    years = sorted([d.name for d in posts.glob("*") if d.is_dir()], reverse=True)
    for post in sorted(posts.glob(pattern), key=lambda x: x.name, reverse=True):
        if post.name == "index.md":
            continue
        logging.debug("Found %s", post)
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
    logging.debug("Render these posts in toc: %s", posts_metadata)
    toc = get_template(template).render(
        {
            "posts": posts_metadata,
            "years": years,
            "ref": url_ref,
            "title_ref": title_ref,
            "include_markers": True,
        }
    )
    with open(toc_file) as fp:
        in_toc = False
        readme_content = fp.read()
        result = re.search(PATTERN, readme_content)
        readme_new = re.sub(
            pattern=MARKER.format("(.|\n)*"),
            repl=toc,
            string=readme_content,
        )

    if readme_new != readme_content:
        if backup_original and toc_file == target:
            # save previous README file as backup, in case something goes wrong.
            pathlib.Path(toc_file).rename(f"{toc_file}.{datetime.datetime.now().isoformat()}")
        with open(target, "w") as fp:
            fp.write(readme_new)
        print(f"toc has been updated!")
        return 0
    else:
        print(f"toc has not changed!")
        # even if toc didn't change, write file to target location
        if toc_file != target:
            with open(target, "w") as fp:
                fp.write(readme_new)
            print(f"{toc_file} has been copied to {target}")
            return 0
        # nothing happened, which is probably not what was intended when running this command
        return 1
