import os

import django
import pytest
from django.contrib.auth.hashers import make_password
from django.core import management


# region fixtures
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
# endregion


# region startup
def pytest_addoption(parser):
    parser.addoption(
        "--staticfiles",
        action="store_true",
        default=False,
        help="Run tests with static files collection, using manifest "
        "staticfiles storage. Used for testing the distribution.",
    )


def pytest_configure(config):
    os.environ["DJANGO_ENV"] = "test"
    os.environ["DJANGO_SETTINGS_MODULE"] = "server.settings"

    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    os.environ["CACHE_URL"] = "locmem://"

    django.setup()

    if config.getoption("--staticfiles"):
        management.call_command("collectstatic", verbosity=0, interactive=False)


# endregion