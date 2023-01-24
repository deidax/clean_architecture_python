import json
from .room_json_ser import RoomJsonEncoder


class SuccessRequestRoomJsonSer(json.JSONEncoder):
    
    def default(self, o):
        try:
            """Get response to serialize"""
            resp = o.get_response() #this returns a dict object
            
            """Make sure to serialize Room objects 
            before adding them to the final serialized response"""
            resp['response'] = [json.dumps(r, cls=RoomJsonEncoder) for r in resp['response']]
            return resp
        except AttributeError:
            return super().default(o)
        
        