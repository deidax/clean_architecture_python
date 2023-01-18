
class RoomListUseCase():
    
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        rooms = self.repo.list()
        return rooms
        #return SuccessResponse(rooms)