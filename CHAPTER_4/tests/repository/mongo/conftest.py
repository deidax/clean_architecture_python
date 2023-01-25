import os
from dotenv import load_dotenv
load_dotenv('../../.env')

import pytest
import pymongo

@pytest.fixture(scope="session")
def mg_env(docker_ip):
    return {
        'mongo':
            {
                'dbname':os.getenv('MONGO_DB', ''),
                'user':os.getenv('MONGO_USER', ''),
                'password':os.getenv('MONGO_PASSWORD', ''),
                'host':docker_ip
            }
    }

def is_mongo_ready(mg_env):
    try:
        client = pymongo.MongoClient(
            host=mg_env['mongo']['host'],
            username=mg_env['mongo']['user'],
            password=mg_env['mongo']['password'],
            authSource='admin'
        )
        client.admin.command('ismaster')
        return True
    except pymongo.erros.ServiceSelectionTimeoutError:
        return False