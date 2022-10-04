import logging
import pathlib
import shutil
from typing import Optional

import typer

from eotw import md2html

app = typer.Typer()

here = pathlib.Path.cwd()


@app.callback()
def main(ctx: typer.Context):
    """Tiny markdown-based blog."""
    logging.basicConfig(level=logging.DEBUG, format="%(message)s", stream=open("eotw.log", "w+"))
    logging.debug(f"About to execute command: {ctx.invoked_subcommand}")


@app.command()
def create_indices(
    dir_posts: pathlib.Path,
    custom_index: Optional[pathlib.Path] = None,
    pattern: str = "*/*.md",
    force: bool = False,
):
    # create main index
    index_target = dir_posts / "index.md"
    if index_target.exists() and not force:
        print(f"Skipping '{index_target}': already exists")
    elif custom_index is not None:
        shutil.copy(custom_index, dir_posts / "index.md")
    else:
        md2html.create_index(src=dir_posts)

    # create index for first-level subdirectories
    for subdirectory in [d for d in dir_posts.glob("*") if d.is_dir()]:
        md2html.create_index(
            src=subdirectory,
            title=subdirectory.name,
            url_ref="{week}",
            pattern=pattern.split("/", maxsplit=1)[1],
            template="subindex",
        )


@app.command()
def build(
    dir_posts: pathlib.Path,
    pattern: str = "*/*.md",
):
    if not dir_posts.is_dir():
        raise typer.BadParameter("dir_posts must exist already!")
    md2html.convert_posts(src=dir_posts)
    md2html.convert_indices(src=dir_posts)


# import commands defined in other modules (required!)
from .post import new
from .toc import update
