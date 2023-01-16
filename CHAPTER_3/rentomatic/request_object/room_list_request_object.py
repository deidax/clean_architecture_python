
class RoomListRequestObject:
    
    _accepted_filters = ['code__iq', 'price__iq', 'price__lt', 'price__gt']
    
    
    def __init__(self, filters=None) -> None:
        self.errors = []
        self.filters = self._load_filters(filters)
    
    def __bool__(self):
        return not self.has_error()

    @classmethod
    def from_dict(cls, dict_f):
        return cls(filters=dict_f)

    def has_error(self):
        return len(self.errors) > 0
    
    def _load_filters(self, filters):
        if filters == {}: return None
        if not isinstance(filters, dict): return filters
        
        if 'filters' in filters:
            f_keys = filters['filters'].keys()
            if not all(fk in self._accepted_filters for fk in f_keys):
                self.errors.append({'parameter': 'filters'})
                return None
            
            return filters['filters']
        
        return None
                
            