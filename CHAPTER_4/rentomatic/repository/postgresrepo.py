from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from rentomatic.domain import room
from rentomatic.repository.postgres_object import Base, Room

class PostgresRepo:
    def __init__(self, connection_data) -> None:
        connection_string = "postgresql://{user}:{password}@{host}/{db}".format(
                user=connection_data['user'],
                password=connection_data['password'],
                host=connection_data['host'],
                db=connection_data['dbname']
            )
        
        self.engine = create_engine(connection_string)
        Base.metadata.bind = self.engine
    
    def list(self):
        pass