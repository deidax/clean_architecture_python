from rentomatic.request_object.room_list_request_object import RoomListRequestObject

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
    print(request.errors)
    assert bool(request) is True

def test_build_room_list_request_object_from_dict_with_filters_wrong():
    request = RoomListRequestObject.from_dict({'filters': {'a': 1}})
    
    assert request.has_error()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False