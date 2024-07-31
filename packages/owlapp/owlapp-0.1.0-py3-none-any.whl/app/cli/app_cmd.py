import secrets
from inspect import cleandoc
from textwrap import indent

import click
from flask.cli import AppGroup

cmd = AppGroup(help="App commands.")


@cmd.command(name="generate-secret")
def generate_secret():
    value = secrets.token_urlsafe(32)
    click.echo(value)


@cmd.command(name="generate-env")
def generate_env():
    from app.settings import settings

    content: list[str] = []
    for key, field in settings.model_fields.items():
        if not key.isupper():
            continue

        if (
            str(field.annotation) == "typing.Optional[str]"
            and field.default is not None
        ):
            value = f'"{field.default}"'
        elif field.default is None:
            value = ""
        else:
            value = field.default

        if field.description:
            content.append(indent(cleandoc(field.description), "# "))

        if not value:
            content.append(f"# {key}={value}")
        else:
            content.append(f"{key}={value}")
        content.append("\n")

    click.echo("\r\n".join(content))
