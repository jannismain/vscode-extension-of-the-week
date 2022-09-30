#!/usr/bin/env python3

import logging
import pathlib
import subprocess

import frontmatter

from eotw import get_template


def generate_index(
    src: pathlib.Path,
    title="VSCode Extension of the Week",
    url_ref="{year}/{week}",
    strip_labels=("vscode",),
):
    posts_metadata = []
    years = sorted([d.name for d in src.glob("*") if d.is_dir()], reverse=True)
    for post in sorted(src.glob("*/*.md"), key=lambda x: x.name, reverse=True):
        fm = frontmatter.load(post).to_dict()
        fm["labels"] = [label for label in fm["labels"] if label not in strip_labels]
        posts_metadata.append(
            {"year": post.parent.name, "week": post.name[0:2], "extension": fm["title"][4:], **fm}
        )
    index = get_template("index").render(
        {"posts": posts_metadata, "title": title, "years": years, "ref": url_ref}
    )
    with (src / "index.md").open("w") as fp:
        fp.write(index)


def convert_posts(src: pathlib.Path):
    for post in src.glob("*/*.md"):
        target_filename = post.stem.split("_")[0] + ".html"
        print(f"Converting {post.name} -> {target_filename}")
        _pandoc(
            src=str(post.relative_to(src.parent)),
            dest=str(post.with_name(target_filename).relative_to(src.parent)),
        )


def convert_indices(src: pathlib.Path):
    for index in src.glob("**/index.md"):
        _pandoc(
            src=index.relative_to(src.parent),
            dest=index.with_suffix(".html").relative_to(src.parent),
            args=[
                "--css",
                "style.css",
            ],
        )


def _pandoc(src, dest, args=tuple()):
    cmd = ["pandoc", "-s", "--sandbox", *args, "-o", str(dest), str(src)]
    logging.info(" ".join(cmd))
    result = subprocess.run(cmd, capture_output=True)
    if result.stdout:
        logging.info(result.stdout.decode())
    if result.stderr:
        logging.error(result.stderr.decode())