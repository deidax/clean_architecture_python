from rentomatic.request_object.room_list_request_object import RoomListRequestObject
from rentomatic.repository.repo import Repo
from rentomatic.response_object.room_response import RoomResponse
from rentomatic.use_case.room_list_use_case import RoomListUseCase

class RoomListService:
    
    def __init__(self, repository: Repo) -> None:
        self._repository = repository
    
    
    def list_with_filters(self, filters={}) -> RoomResponse:
        
        req = RoomListRequestObject.from_dict(filters)
        uc = RoomListUseCase(self._repository)
        
        return uc.execute(req)
    
    