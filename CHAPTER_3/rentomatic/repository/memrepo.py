from rentomatic.domain import room
class MemRepo():
    
    def __init__(self, data_dict) -> None:
        self.data_dict = data_dict
        
    def list(self, filters={}):
        result = [room.Room.from_dict(r) for r in self.data_dict]
        if 'code__iq' in filters:
            return [r for r in result if r.code == filters['code__iq']]
        return result
