#!/usr/bin/env python3

import datetime
import pathlib
from types import SimpleNamespace

from pyfiglet import Figlet
from questionary import ValidationError, Validator, prompt

from eotw import get_template
from eotw.cli import app


@app.command()
def new(posts: pathlib.Path = pathlib.Path("VSCode Extension of the Week")):
    figlet = Figlet(font="slant")
    print(figlet.renderText("VSCode EotW"))

    if not (data := dialog()):
        exit(0)

    # split week into year and week
    data["year"] = data["week"].split(".")[0]
    data["week"] = data["week"].split(".")[1]

    new_post = get_template("post").render(data)
    # put data into namespace for more readable code below
    data = SimpleNamespace(**data)

    filename = f"{data.week}_{data.extension.split('.')[-1]}.md"
    fp_new_post: pathlib.Path = posts / data.year / filename

    fp_new_post.parent.mkdir(parents=True, exist_ok=True)
    with fp_new_post.open("w") as fp:
        fp.write(new_post)


def dialog():
    class WeekValidator(Validator):
        def validate(self, document):
            try:
                1900 <= int(document.text.split(".")[0]) <= 2100
            except ValueError:
                raise ValidationError(
                    message="Must provide year between 1900 and 2100.",
                    cursor_position=len(document.text.split(".")[0]),
                )
            try:
                1 <= int(document.text.split(".")[1]) <= 53
            except ValueError:
                raise ValidationError(
                    message="Please enter a valid calendar week",
                    cursor_position=len(document.text),
                )

    questions = [
        {
            "type": "input",
            "name": "week",
            "message": "What week do you want to create a post for?",
            "validate": WeekValidator,
            "filter": lambda val: f"{int(val.split('.')[0])}.{int(val.split('.')[1]):02d}",
            "default": ".".join(f"{d:02d}" for d in datetime.datetime.now().isocalendar()[:-1]),
        },
        {
            "type": "input",
            "name": "extension",
            "message": "What extension do you want to highlight? Extension ID:",
        },
        {
            "type": "input",
            "name": "extension_name",
            "message": "What is this extension called?",
            "default": lambda answers: answers["extension"].split(".")[-1],
        },
        {
            "type": "checkbox",
            "name": "labels",
            "message": "Any labels you want to assign?",
            "choices": [
                "python",
                "documentation",
                "shell",
                "macOS",
                "git",
                "markdown",
            ],  # TODO: load labels from previous posts
        },
    ]
    return prompt(questions)
