import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_case import room_list_use_case as uc
from rentomatic.request_object.room_list_request_object import RoomListRequestObject

@pytest.fixture
def domain_rooms():
    room_1 = r.Room(
        code=uuid.uuid4(),
        size=215,
        price=39,
        longitude=-0.92939283,
        latitude=51.030399483
    )
    room_2 = r.Room(
        code=uuid.uuid4(),
        size=400,
        price=100,
        longitude=-0.929339283,
        latitude=49.030399483
    )
    room_3 = r.Room(
        code=uuid.uuid4(),
        size=100,
        price=40,
        longitude=-0.848920,
        latitude=89.0399388
    )
    room_4 = r.Room(
        code=uuid.uuid4(),
        size=90,
        price=30,
        longitude=-0.7388299,
        latitude=29.03003994
    )
    
    return [room_1, room_2, room_3, room_4]

def test_room_list_without_parameters(domain_rooms):
    """Create Moke Repo"""
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    
    """Inject Repo Into UseCase"""
    room_list_use_case = uc.RoomListUseCase(repo)
    """Create a Request Object"""
    request = RoomListRequestObject()
    
    """Inject The Request Into The execute Method"""
    result = room_list_use_case.execute(request)
    
    """Run The Tests"""
    assert bool(request) is True
    repo.list.assert_called_with()
    assert result == domain_rooms