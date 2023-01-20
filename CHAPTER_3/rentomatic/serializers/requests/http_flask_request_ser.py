from rentomatic.serializers.requests.room_input_request_ser import RoomListInputRequestSeria

class HttpFlaskRequestSer(RoomListInputRequestSeria):
    
    
    
    def filters(self, flask_request: list):
        if not isinstance(flask_request, list): return None
        query_filter =  {
            'filters': {}
        }
        
        for arg, value in flask_request.args.items():
            if(arg).statswith('filter_'):
                query_filter['filters'][arg.replace('filter_', '')] = value
        
        return query_filter
                
    
