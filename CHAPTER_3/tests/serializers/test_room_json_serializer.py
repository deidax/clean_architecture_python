import json
import uuid

from rentomatic.domain import room as r
from rentomatic.serializers import room_json_ser
from rentomatic.serializers.requests.http_flask_request_ser import HttpFlaskRequestSer

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


def test_serializer_filters_params():
    
    
    params = {'price__gt': '2', 'price__lt': '6'}
    args_params = [('filter_price__get', '2'), ('filter_price__lt', '6')]
    
    
    
    assert HttpFlaskRequestSer().filters(filters=args_params) == {'price__gt': '2', 'price__lt': '6'}

