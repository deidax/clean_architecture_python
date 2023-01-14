import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_case import room_list_use_case as uc

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
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = uc.RoomListUseCase(repo)
    result = room_list_use_case.execute()
    repo.list.assert_called_with()
    assert result == domain_rooms