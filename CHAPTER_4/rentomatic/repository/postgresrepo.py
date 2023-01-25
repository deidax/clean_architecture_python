from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from rentomatic.domain import room
from rentomatic.repository.postgres_object import Base, Room
from .repo import Repo
class PostgresRepo(Repo):
    def __init__(self, connection_data) -> None:
        connection_string = "postgresql://{user}:{password}@{host}/{db}".format(
                user=connection_data['user'],
                password=connection_data['password'],
                host=connection_data['host'],
                db=connection_data['dbname']
            )
        
        self.engine = create_engine(connection_string, pool_size=20, max_overflow=0)
        Base.metadata.bind = self.engine
    
    def _create_room_object(self, results):
        return [
            room.Room(
                code=q.code,
                size=q.size,
                price=q.price,
                latitude=q.latitude,
                longitude=q.longitude
            )
            for q in results
        ]
    
    
    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query=session.query(Room)
        
        if filters is None:
            return self._create_room_object(query.all())
        if 'code__iq' in filters:
            query = query.filter(Room.code == filters['code__iq'])

        if 'price__iq' in filters:
            query = query.filter(Room.price == filters['price__iq'])
        
        if 'price__lt' in filters:
            query = query.filter(Room.price < filters['price__lt'])
        
        if 'price__gt' in filters:
            query = query.filter(Room.price > filters['price__gt'])
        
        return self._create_room_object(query.all())