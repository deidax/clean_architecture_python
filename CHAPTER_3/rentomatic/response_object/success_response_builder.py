from rentomatic.response_object.response_builder import ResponseBuilder
from rentomatic.response_object.success_response import SuccessResponse
from rentomatic.response_object.response_types_enums import ResponseTypesEnums

class SuccessResponseBuilder(ResponseBuilder):

    def __init__(self) -> None:
        """
        A builder instance should contain a blank response object
        which is used in further assembly
        """
        self._success_response = SuccessResponse()
    
    def set_value(self, value):
        self._success_response.response_value = value
        return self
    
    def set_type(self):
        self._success_response.response_type = ResponseTypesEnums.SUCCESS
        return self

    def set_response_message(self, message_value):
        self._success_response.response_message = message_value
        return self

    def build_response(self):
        return self._success_response
    
    def set_response_message_and_build(self, message_value):
        success_builder = self.set_type().set_response_message(message_value)
        return success_builder.build_response()