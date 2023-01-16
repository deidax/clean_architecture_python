from rentomatic.response_object.success_response import SuccessResponse

class RoomListUseCase():
    
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        rooms = self.repo.list()
        return SuccessResponse(rooms)