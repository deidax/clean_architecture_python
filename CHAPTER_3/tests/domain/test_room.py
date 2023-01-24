import uuid
from rentomatic.domain import room as r

def test_room_model_init():
    code = uuid.uuid4()
    room = r.Room(code=code, size=200, price=10, longitude=-0.09983338, latitude=52.7477362)
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09983338
    assert room.latitude == 52.7477362

def test_room_model_from_dict():
    code = uuid.uuid4()
    room = r.Room.from_dict(
        dict_data= {
                'code': code,
                'size': 200,
                'price': 10,
                'longitude': -0.09983338,
                'latitude': 52.7477362
            }
    )
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09983338
    assert room.latitude == 52.7477362

def test_room_model_to_dict():
    room_dict = {
        'code': '1245454875',
        'size': 200,
        'price': 10,
        'longitude': -0.09983338,
        'latitude': 52.7477362
    }
    
    room_model = r.Room.from_dict(room_dict)
    assert room_model.to_dict() == room_dict
    
def test_room_model_comparison():
    room_dict = {
        'code': '1245454875',
        'size': 200,
        'price': 10,
        'longitude': -0.09983338,
        'latitude': 52.7477362
    }
    
    room_1 = r.Room.from_dict(room_dict)
    room_2 = r.Room.from_dict(room_dict)
    
    assert room_1 == room_2

def test_room_model_is_not_equal():
    room_dict_1 = {
        'code': '1245454875',
        'size': 200,
        'price': 10,
        'longitude': -0.09983338,
        'latitude': 52.7477362
    }
    
    room_dict_2 = {
        'code': '12457854875',
        'size': 200,
        'price': 50,
        'longitude': -0.09983338,
        'latitude': 52.7477362
    }
    
    room_1 = r.Room.from_dict(room_dict_1)
    room_2 = r.Room.from_dict(room_dict_2)
    
    assert not room_1 == room_2