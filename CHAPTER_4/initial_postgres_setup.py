import os
from dotenv import load_dotenv
load_dotenv()

import sqlalchemy
import sqlalchemy_utils
from rentomatic.repository.postgres_object import Base, Room
from rentomatic.domain import room


setup = {
            'dbname':os.getenv('POSTGRES_DB', ''),
            'user':os.getenv('POSTGRES_USER', ''),
            'password':os.getenv('POSTGRES_PASSWORD', ''),
            'host':'localhost'
        }

con_str = "postgresql://{user}:{password}@{host}/{db}".format(
                user=setup['user'],
                password=setup['password'],
                host=setup['host'],
                db=setup['dbname']
            )
print('--> CREATING ENGINE... \n')
engine = sqlalchemy.create_engine(con_str)

if not sqlalchemy_utils.database_exists(engine.url):
        print('--> CREATING DATABASE... \n')
        sqlalchemy_utils.create_database(engine.url)
else:
    print('--> DATABASE EXISTS ALREADY!... \n')

print('--> CONNECTING TO ENGINE!... \n')
conn = engine.connect()

Base.metadata.create_all(engine)
Base.metadata.bine = engine
print('--> CREATING SESSION!... \n')
DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
session = DBSession()

data = [
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
            'price': 160,
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

for r in data:
    new_room = Room(
        code = r['code'],
        size = r['size'],
        price = r['price'],
        longitude=r['longitude'],
        latitude=r['latitude']
    )
    #This for printing created elements
    room_repo = room.Room(   
        code = r['code'],
        size = r['size'],
        price = r['price'],
        longitude=r['longitude'],
        latitude=r['latitude']
    )
    session.add(new_room)
    session.commit()
    print(f'--> ROOM {room_repo.to_dict()} ADDED TO DB! \n')