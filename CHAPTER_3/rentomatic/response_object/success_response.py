from .room_response import RoomResponse
import json
from rentomatic.serializers.success_request_room_json_ser import SuccessRequestRoomJsonSer

class SuccessResponse(RoomResponse):
    
    
    
    def json_ser(self, encoder=SuccessRequestRoomJsonSer):
        super().json_ser(encoder)
        return json.dumps(self, cls=encoder)
    
    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg