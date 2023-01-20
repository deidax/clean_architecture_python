from rentomatic.serializers.requests.room_input_request_ser import RoomListInputRequestSeria

class HttpFlaskRequestSer(RoomListInputRequestSeria):
    
    
    
    def filters(self, filters: list):
        if not isinstance(filters, list): return None
        return {'price__gt': '2', 'price__lt': '6'}
    
