import pathlib
import shutil
import logging
from typing import Optional

import typer

from eotw import md2html

app = typer.Typer()

here = pathlib.Path.cwd()


@app.command()
def to_html(
    dir_posts: pathlib.Path = (here / "VSCode Extension of the Week").relative_to(here),
    index: pathlib.Path = (here / "README.md").relative_to(here),
    overwrite_index: bool = False,
    pattern: str = "*/*.md",
):
    skip_index_creation = False
    if (dir_posts / "index.md").exists():
        print(
            "index.md already exists"
            + (" and will be overwritten" if overwrite_index else ". skip index creation")
        )
        if not overwrite_index:
            skip_index_creation = True
    if not skip_index_creation:
        if index.is_file():
            shutil.copy(index, dir_posts / "index.md")
        else:
            logging.warn(f"Given index '{index}' is not a file. Will generate index based on template.")
            md2html.generate_index(src=dir_posts)
    md2html.convert_posts(src=dir_posts)
    md2html.convert_indices(src=dir_posts)


# import commands defined in other modules (required!)
from .post import new
from .toc import update
