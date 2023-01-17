import pytest
from rentomatic.request_object.room_list_request_object import RoomListRequestObject
from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException

def test_build_room_list_request_object_without_parameters():
    request = RoomListRequestObject()
    
    assert request.filters is None
    assert bool(request) is True

def test_build_room_list_request_object_from_empty_dict():
    request = RoomListRequestObject.from_dict({})
    
    assert request.filters is None
    assert bool(request) is True

def test_build_room_list_request_object_from_dict_with_empty_filters():
    request = RoomListRequestObject.from_dict({'filters': {}})
    
    assert request.filters == {}
    assert bool(request) is True

def test_build_room_list_request_object_from_dict_with_filters_wrong():
    request = RoomListRequestObject.from_dict({'filters': {'a': 1}})
    
    assert request.has_error()
    assert request.errors == [{'parameter': 'a', 'message': '\'a\' is an invalid filter key'}]
    assert bool(request) is False

def test_build_room_list_request_object_from_dict_with_invalid_filters():
    request = RoomListRequestObject.from_dict({'filters': 5})
    
    assert request.has_error()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False

@pytest.mark.parametrize(
    'key',
    ['code__iq', 'price__iq', 'price__lt', 'price__gt']
)
def test_build_room_list_request_object_accepted_filters(key):
    filters = {key: 1}
    request = RoomListRequestObject.from_dict({'filters': filters})
    
    assert request.filters == filters
    assert bool(request) is True

@pytest.mark.parametrize(
    'key',
    ['code__iq', 'price__iq', 'price__lt', 'price__gt']
)
def test_build_room_list_request_object_from_dict_with_invalid_filter_key_name_and_valid_filters(key):
    filters = {key: 1}
    request = RoomListRequestObject.from_dict({'invald_filters_key_name': filters})
    
    assert request.has_error()
    assert request.errors[0]['invald_filters_key_name'] == 'Not a valid filter key. use \'filters\' instead'
    assert "invald_filters_key_name: Not a valid filter key. use 'filters' instead\n\n" == request.show_errors_message()
    assert bool(request) is False

@pytest.mark.parametrize(
    'key',
    ['code__lt', 'code__gt']
)
def test_build_room_list_request_object_rejected_filters(key):
    filters = {key: 1}
    request = RoomListRequestObject.from_dict({'filters': filters})
    
    assert request.has_error()
    k=next(iter(filters))
    assert request.errors[0] == {'parameter': k, 'message': '\'{}\' is an invalid filter key'.format(k)}
    assert bool(request) is False