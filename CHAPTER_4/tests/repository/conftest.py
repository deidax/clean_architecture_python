import os
from dotenv import load_dotenv
load_dotenv()
import psycopg2
import sqlalchemy
import sqlalchemy_utils


import pytest

from rentomatic.repository.postgres_object import Base, Room


def is_postgresql_ready(docker_ip):
    try:
        psycopg2.connect(
            "postgresql://{user}:{password}@{host}/{db}".format(
                user=os.getenv('POSTGRES_USER', ''),
                password=os.getenv('POSTGRES_PASSWORD', ''),
                host=docker_ip,
                db=os.getenv('POSTGRES_DB', '')
            )
        )
        print('CONNECTION READY!!')
        return True
    except:
        return False

@pytest.fixture(scope="session")
def database_service(docker_ip, docker_services):
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_postgresql_ready(docker_ip)
    )
    return





@pytest.fixture(scope='session')
def pg_engine(docker_ip, docker_services):
    print("Waiting until responsive (60s)..")
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_postgresql_ready(docker_ip)
    )

    conn_str = "postgresql://{user}:{password}@{host}/{db}".format(
                user=os.getenv('POSTGRES_USER', ''),
                password=os.getenv('POSTGRES_PASSWORD', ''),
                host=docker_ip,
                db=os.getenv('POSTGRES_DB', '')
            )
    engine = sqlalchemy.create_engine(conn_str)
    if not sqlalchemy_utils.database_exists(engine.url):
        sqlalchemy_utils.create_database(engine.url)
        
    print(f'Engine Connected !!: {sqlalchemy_utils.database_exists(engine.url)}')
    conn = engine.connect()

    yield engine

    print("Engine Closed !!")
    conn.close()


@pytest.fixture(scope='session')
def pg_session_empty(pg_engine):
    Base.metadata.create_all(pg_engine)

    Base.metadata.bind = pg_engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=pg_engine)

    print('Empty Session...')
    session = DBSession()

    yield session

    print('Close Session...')
    session.close()


@pytest.fixture(scope='function')
def pg_data():
    return [
        {
            'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
            'size': 215,
            'price': 39,
            'longitude': -0.09998975,
            'latitude': 51.75436293,
        },
        {
            'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
            'size': 405,
            'price': 66,
            'longitude': 0.18228006,
            'latitude': 51.74640997,
        },
        {
            'code': '913694c6-435a-4366-ba0d-da5334a611b2',
            'size': 56,
            'price': 60,
            'longitude': 0.27891577,
            'latitude': 51.45994069,
        },
        {
            'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
            'size': 93,
            'price': 48,
            'longitude': 0.33894476,
            'latitude': 51.39916678,
        }
    ]



@pytest.fixture(scope='function')
def pg_session(pg_session_empty, pg_data):
    for r in pg_data:
        new_room = Room(
            code=r['code'],
            size=r['size'],
            price=r['price'],
            longitude=r['longitude'],
            latitude=r['latitude']
        )
        pg_session_empty.add(new_room)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(Room).delete()
