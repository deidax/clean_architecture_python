from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException

class RoomListRequestObject:
    
    _accepted_filters = ['code__iq', 'price__iq', 'price__lt', 'price__gt']
    
    
    def __init__(self, filters=None) -> None:
        self._req_exception = None
        try:
            self.filters = self._load_filters(filters)
        except InvalidRoomListRequestException as req_exception:
            self.filters = None
            self._req_exception = req_exception
            
    
    def __bool__(self):
        return not bool(self._req_exception)

    @classmethod
    def from_dict(cls, dict_f: dict):
        return cls(filters=dict_f)
    
    @property 
    def errors(self):
        return self._req_exception.errors

    def has_error(self):
        return bool(self._req_exception)
    
    def show_errors_message(self):
        return str(self._req_exception)
    
    def show_clean_errors_message(self):
        return str(self._req_exception.get_errors_messages())
    
    def _load_filters(self, filters):
        if filters == {}: return {}
        if not isinstance(filters, dict): return filters
        if 'filters' not in filters:
            raise InvalidRoomListRequestException({ next(iter(filters)): 'Not a valid filter key. use \'filters\' instead' })
        if not isinstance(filters['filters'], dict):
            raise InvalidRoomListRequestException({'parameter': 'filters', 'message': 'filters must be a dict'})
        
        
        f_keys = filters['filters'].keys()
        if not all(fk in self._accepted_filters for fk in f_keys):
            invalid_keys = list(set(f_keys).difference(self._accepted_filters))
            filters_keys_exception = InvalidRoomListRequestException()
            for inv_key_el in invalid_keys:
                filters_keys_exception.add_error(parameter=inv_key_el, message='\'{}\' is an invalid filter key'.format(inv_key_el))
            raise filters_keys_exception
        
        return filters['filters']
                
            