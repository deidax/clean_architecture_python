import os
import tempfile
import yaml

import pytest

from rentomatic.app import create_app
from rentomatic.flask_settings import TestConfig



def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration: mark test to run only Postgres integration test"
    )

@pytest.fixture(scope="function")
def app():
    return create_app(TestConfig)

@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "CHAPTER_4/tests/", "docker-compose.yaml")