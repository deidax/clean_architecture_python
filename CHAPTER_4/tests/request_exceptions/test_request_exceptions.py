import pytest
from unittest import mock
from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException
def test_invalid_room_list_get_request_error():
    req = mock.Mock()
    
    req.errors = [{'parameter': 'filters', 'message': 'Invalid'}]
    
    ex = InvalidRoomListRequestException()
    
    ex.add_error('filters', 'Invalid')
    
    assert req.errors == ex.errors
    assert bool(ex) is True
    
    with pytest.raises(Exception):
        ex.errors = [{'parameter': 'filters'}]

def test_raise_room_list_request_error():
    req = mock.Mock()
    def mock_load_filter():
        req.filters = None
        if req.filters == None:
            raise InvalidRoomListRequestException(error={'filters': 'invalid'})
        return {}
    
    req.load_filters.side_effect = mock_load_filter
    with pytest.raises(InvalidRoomListRequestException, match="filters: invalid\n\n"):
        req.load_filters()

