import json
import uuid

from rentomatic.domain import room as r
from rentomatic.serializers.room_json_ser import RoomJsonEncoder
from rentomatic.serializers.requests.http_flask_request_ser import HttpFlaskRequestSer
from unittest import mock

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
    
    json_room = json.dumps(room, cls=RoomJsonEncoder)
    assert json.loads(json_room) == json.loads(room_json_ser_expected_output)


def test_serializer_filters_params():
    
    request = mock.Mock()
    params = {'price__gt': '2', 'price__lt': '6'}
    """request.args.items is a generator"""
    request.args.items.return_value = (i for i in [('filter_price__gt', '2'), ('filter_price__lt', '6')])
    
    
    
    assert HttpFlaskRequestSer().filters(request.args.items()) == {'filters':{'price__gt': '2', 'price__lt': '6'}}

