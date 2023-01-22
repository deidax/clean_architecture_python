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

