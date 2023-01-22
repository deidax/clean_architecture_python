from types import GeneratorType
from rentomatic.serializers.requests.room_input_request_ser import RoomListInputRequestSeria

class HttpFlaskRequestSer(RoomListInputRequestSeria):
    
    
    
    def filters(self, flask_request_args: GeneratorType):
        if not isinstance(flask_request_args, GeneratorType): return None
        query_filter =  {
            'filters': {}
        }
        
        for arg, value in flask_request_args:
            if(arg).startswith('filter_'):
                query_filter['filters'][arg.replace('filter_', '')] = value
        
        return query_filter
                
    
