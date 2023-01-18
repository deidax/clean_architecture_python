
from rentomatic.response_object.response_builder import ResponseBuilder
from rentomatic.response_object.failure_response import FailureResponse
from rentomatic.response_object.response_types_enums import ResponseTypesEnums
from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException

class FailureResponseBuilder(ResponseBuilder):

    def __init__(self) -> None:
        """
        A builder instance should contain a blank response object
        which is used in further assembly
        """
        self._failure_response = FailureResponse()
    
    def set_value(self, value):
        self._failure_response.response_value = value
        return self
    
    def default_type(self):
        self._failure_response.response_type = ResponseTypesEnums.FAILURE
        return self
    
    def set_response_message(self, message_value):
        self._failure_response.response_message = message_value
        return self

    def build_response(self):
        self._failure_response.response_value = {'type': self._failure_response.response_type, 'message': self._failure_response.response_message}
        return self._failure_response
    
    def set_response_message_and_build(self, message_value=''):
        failure_builder = self.default_type().set_response_message(message_value)
        return failure_builder.build_response()
    
    def _set_cause_of_failure(self, value=ResponseTypesEnums.PARAMETERS_ERROR):
        self._failure_response.cause_of_failure = value
        return self
        
    def build_invalid_request_exception_object(self, exc: InvalidRoomListRequestException):
        #default value 'PARAMETERS_ERROR'
        failure_builder = self._set_cause_of_failure()\
                              .set_response_message_and_build(exc.get_errors_messages())
                             
        return failure_builder