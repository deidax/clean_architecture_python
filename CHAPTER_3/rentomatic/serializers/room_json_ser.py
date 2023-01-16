import json

class RoomJsonEncoder(json.JSONEncoder):
    
    def default(self, o):
        try:
            o_to_dict = o.to_dict()
            o_to_dict['code'] = str(o_to_dict['code'])
            return o_to_dict
        except AttributeError:
            return super().default(o)
        