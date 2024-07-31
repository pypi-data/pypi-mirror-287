import importlib.metadata

from app.app import create_app  # noqa
from app.const.app import APP_NAME
from app.logging import setup_logging
from flask_migrate import Migrate

__version__ = importlib.metadata.version(APP_NAME)

setup_logging()

migrate = Migrate(compare_type=True)
