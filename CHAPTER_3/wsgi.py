from rentomatic.app import create_app
from rentomatic.flask_settings import TestConfig

app = create_app(config_object=TestConfig)