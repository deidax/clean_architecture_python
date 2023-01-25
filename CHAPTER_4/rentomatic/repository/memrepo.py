from rentomatic.domain import room
from .repo import Repo
class MemRepo(Repo):
    
    def __init__(self, data_dict) -> None:
        self.data_dict = data_dict
        
    def list(self, filters={}):
        result = [room.Room.from_dict(r) for r in self.data_dict]
        if 'code__iq' in filters:
            result = [r for r in result if r.code == filters['code__iq']]

        if 'price__iq' in filters:
            result = [r for r in result if r.price == int(filters['price__iq'])]
        
        if 'price__lt' in filters:
            result = [r for r in result if r.price < int(filters['price__lt'])]
        
        if 'price__gt' in filters:
            result = [r for r in result if r.price > int(filters['price__gt'])]

        return result