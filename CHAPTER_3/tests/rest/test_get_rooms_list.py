import json
from unittest import mock
from rentomatic.response_object.success_response_builder import SuccessResponseBuilder
from rentomatic.domain.room import Room
import uuid


code=uuid.uuid4()
room1 = Room(code=code, size=200, price=10, longitude=-0.09983338, latitude=52.7477362)
room2 = Room(code=code, size=200, price=10, longitude=-0.09983338, latitude=52.7477362)
room3 = Room(code=code, size=200, price=10, longitude=-0.09983338, latitude=52.7477362)

rooms = [room1,room2,room3]

room_json_ser_expected_output1 = """{{"code": "{}", "size": 200, "price": 10, "longitude": -0.09983338, "latitude": 52.7477362}}""".format(room1.code)
room_json_ser_expected_output2 = """{{"code": "{}", "size": 200, "price": 10, "longitude": -0.09983338, "latitude": 52.7477362}}""".format(room1.code)
room_json_ser_expected_output3 = """{{"code": "{}", "size": 200, "price": 10, "longitude": -0.09983338, "latitude": 52.7477362}}""".format(room1.code)

rooms_json = [room_json_ser_expected_output1,room_json_ser_expected_output2,room_json_ser_expected_output3]


@mock.patch('rentomatic.use_case.room_list_use_case.RoomListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = SuccessResponseBuilder()\
                                            .set_value(rooms)\
                                            .default_type()\
                                            .set_response_message('Rooms List Data')\
                                            .build_response()
    http_response = client.get('/rooms')
    assert json.loads(http_response.data.decode('UTF-8')) == {"type": "Success","status_code": 200, "message": "Rooms List Data", 'response': rooms_json}
    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {}
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
    

@mock.patch('rentomatic.use_case.room_list_use_case.RoomListUseCase')
def test_get_with_filters(mock_use_case, client):
    mock_use_case().execute.return_value = SuccessResponseBuilder()\
                                                .set_value(rooms)\
                                                .default_type()\
                                                .set_response_message('Rooms List Data')\
                                                .build_response()
    http_response = client.get('/rooms?filter_price__gt=2&filter_price__lt=6')
    assert json.loads(http_response.data.decode('UTF-8')) == {'type': 'Success','status_code': 200, 'message': 'Rooms List Data', 'response': rooms_json}
    
    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {'price__gt': '2', 'price__lt': '6'}
    
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
