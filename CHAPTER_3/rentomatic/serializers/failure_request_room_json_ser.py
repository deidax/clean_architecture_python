import json


class FailureRequestRoomJsonSer(json.JSONEncoder):
    
    def default(self, o):
        try:
            """Get response to serialize"""
            err_resp = o.get_response() #this returns a dict object
            
            return err_resp
        except AttributeError:
            return super().default(o)
        
        