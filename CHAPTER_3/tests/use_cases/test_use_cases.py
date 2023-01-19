import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_case import room_list_use_case as uc
from rentomatic.request_object.room_list_request_object import RoomListRequestObject
from rentomatic.response_object.response_types_enums import ResponseTypesEnums
from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException
from rentomatic.response_object.failed_response_builder import FailureResponseBuilder

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
    response_object = room_list_use_case.execute(request)
    
    """Run The Tests"""
    assert bool(request) is True
    repo.list.assert_called_with(filters=None)
    assert response_object.response_value == domain_rooms

def test_room_list_with_correct_filters(domain_rooms):
    """Create Moke Repo"""
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    
    """Inject Repo Into UseCase"""
    room_list_use_case = uc.RoomListUseCase(repo)
    """Create a Request Object with filters"""
    qry_filters = {'code__iq': 5}
    request = RoomListRequestObject.from_dict(dict_f={'filters': qry_filters})
    """Inject The Request Into The execute Method"""
    response_object = room_list_use_case.execute(request)
    
    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.response_value == domain_rooms

def test_room_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')
    
    room_list_use_case = uc.RoomListUseCase(repo)
    request = RoomListRequestObject.from_dict({})
    response_object = room_list_use_case.execute(request)
    
    
    assert bool(response_object) is False
    assert response_object.response_value == {
        'type': ResponseTypesEnums.FAILURE['label'],
        'cause': ResponseTypesEnums.SYSTEM_ERROR['label'],
        'message': 'Exception: Just an error message'
    }

def test_room_list_handles_bad_request():
    repo = mock.Mock()
    
    room_list_use_case = uc.RoomListUseCase(repo)
    """Use a bad request"""
    request = RoomListRequestObject.from_dict(dict_f={'filters': 5})
    response_object = room_list_use_case.execute(request)
    
    assert bool(response_object) is False
    assert response_object.response_value == {
        'type': ResponseTypesEnums.FAILURE['label'],
        'cause': ResponseTypesEnums.PARAMETERS_ERROR['label'],
        'message': 'filters: filters must be a dict'
    }