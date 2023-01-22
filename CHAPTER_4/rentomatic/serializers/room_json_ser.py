import json

class RoomJsonEncoder(json.JSONEncoder):
    
    def default(self, o):
        try:
            o.code = str(o.code)
            return o.to_dict()
        except AttributeError:
            return super().default(o)