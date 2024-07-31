import os

import click
from alembic import command
from alembic.config import Config
from app.settings import settings
from flask.cli import AppGroup

cmd = AppGroup(help="Initialization commands.")


@cmd.command(name="fs")
def init_filesystem():
    """Initialize filesystem for user directories."""
    if os.path.exists(settings.STORAGE_BASE_PATH):
        raise Exception(f"Path {settings.STORAGE_BASE_PATH} already exits.")

    users_path = os.path.join(settings.STORAGE_BASE_PATH, "users")
    os.makedirs(users_path)
    click.echo(f"Created {users_path}")


@cmd.command(name="db")
def init_db() -> None:
    config = Config("app/migrations/alembic.ini")
    command.upgrade(config, "head")
