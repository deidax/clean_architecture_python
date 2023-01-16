import json
import uuid

from rentomatic.domain import room as r
from rentomatic.serializers import room_json_ser

def test_serializer_domain_room():
    
    code=uuid.uuid4()
    room = r.Room(code=code, size=200, price=10, longitude=-0.09983338, latitude=52.7477362)
    room_json_ser_expected_output = """
    {{
        "code": "{}",
        "size": 200,
        "price": 10,
        "longitude": -0.09983338,
        "latitude": 52.7477362
    }}
    """.format(code)
    
    json_room = json.dumps(room, cls=room_json_ser.RoomJsonEncoder)
    assert json.loads(json_room) == json.loads(room_json_ser_expected_output)

