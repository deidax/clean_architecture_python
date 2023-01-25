import pytest

from rentomatic.domain import room as r
from rentomatic.repository.memrepo import MemRepo
from rentomatic.services.room_list_service import RoomListService
from rentomatic.domain.room import Room
import uuid

room1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': -0.09998975,
    'latitude': 51.75436293,
}
room2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': 0.18228006,
    'latitude': 51.74640997,
}
room3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': 0.27891577,
    'latitude': 51.45994069,
}
room4 = {
    'code': 'k13694c4-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 160,
    'longitude': 0.27891577,
    'latitude': 51.45994069,
}

rooms = [room1,room2,room3, room4]

rs_rooms = [Room.from_dict(room1), Room.from_dict(room2), Room.from_dict(room3), Room.from_dict(room4)]
    
def test_room_list_service():
    
    
    r_service = RoomListService(
                    MemRepo(rooms)
                )
    
    result = r_service.list_with_filters()
    
    assert result.get_response() == {"type": "Success","status_code": 200, "message": "Rooms List Data", 'response': rs_rooms}
    
    