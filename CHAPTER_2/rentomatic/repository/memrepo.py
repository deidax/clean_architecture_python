from rentomatic.domain import room
class MemRepo():
    
    def __init__(self, data_dict) -> None:
        self.data_dict = data_dict
        
    def list(self):
        return [room.Room.from_dict(r) for r in self.data_dict]