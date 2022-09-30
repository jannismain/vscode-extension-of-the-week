import pathlib

import jinja2

here = pathlib.Path(__file__).parent
templates = here / "templates"


def get_template(name: str) -> jinja2.Template:
    environment = jinja2.Environment(
        trim_blocks=True, autoescape=True, loader=jinja2.FileSystemLoader(templates)
    )
    return environment.get_template(f"{name}.md")
