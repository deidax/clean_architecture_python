from rentomatic.response_object.room_response import RoomResponse
from rentomatic.response_object.success_response_builder import SuccessResponseBuilder
from rentomatic.response_object.failed_response_builder import FailureResponseBuilder

class RoomListUseCase():
    
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request) -> RoomResponse:
        """
        Check if request is valid before calling repo list
        """
        if request.has_error():
            return FailureResponseBuilder()\
                    .build_parameters_error(request.show_clean_errors_message())

        """
        Inject valid filter request in repo
        and handle any generic errors
        """
        try:
            rooms = self.repo.list(filters=request.filters)
            """
            Build success response after validation
            and return data
            """
            return SuccessResponseBuilder()\
                    .set_value(rooms)\
                    .set_response_message_and_build('Rooms List Data')
                    #.get_response()Remove this later
        except Exception as exp:
            return FailureResponseBuilder()\
                    .build_system_error(exp)
                    #.get_response()Remove this later
