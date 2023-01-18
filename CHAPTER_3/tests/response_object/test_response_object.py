import pytest
from rentomatic.response_object.response_types_enums import ResponseTypesEnums
from rentomatic.response_object.success_response_builder import SuccessResponseBuilder
from rentomatic.response_object.failed_response_builder import FailureResponseBuilder
from rentomatic.request_exceptions.invalid_room_list_request_exception import InvalidRoomListRequestException

@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}
@pytest.fixture
def response_type():
    return 'ResponseError'
@pytest.fixture
def response_message():
    return 'This is a response error'

def test_response_success_is_true_with_all_builder_methods():
    room_success_resp = SuccessResponseBuilder()\
                        .default_type()\
                        .set_response_message('')\
                        .build_response()
    
    #Assert that the final response is True (Success response)
    assert bool(room_success_resp) == True

def test_response_success_is_true_with_default_builder():
    room_success_resp = SuccessResponseBuilder()\
                        .set_response_message_and_build('')
    
    assert bool(room_success_resp) == True

def test_response_success_has_type_and_value(response_value):
    room_success_resp = SuccessResponseBuilder()\
                        .set_value(response_value)\
                        .set_response_message_and_build('')
    
    assert room_success_resp.response_type == ResponseTypesEnums.SUCCESS['label']
    assert room_success_resp.response_value == response_value

def test_response_failure_is_false(response_type, response_message):
    room_failed_resp = FailureResponseBuilder()\
                        .set_response_message_and_build(response_message)
    
    assert bool(room_failed_resp) is False

def test_response_failure_has_type_and_message(response_type, response_message):
    room_failed_resp = FailureResponseBuilder()\
                        .set_response_message_and_build(response_message)
    
    assert room_failed_resp.response_type == response_type
    assert room_failed_resp.response_message == response_message

def test_response_failure_contains_value(response_type, response_message):
    room_failed_resp = FailureResponseBuilder()\
                        .set_response_message_and_build(response_message)
    
    assert room_failed_resp.response_value == {'type': response_type, 'message': response_message}

def test_response_failure_initialisation_with_exception(response_type):
    room_failed_resp = FailureResponseBuilder()\
                        .set_response_message_and_build(Exception('Just an error message'))
                        
    assert bool(room_failed_resp) is False
    assert room_failed_resp.response_type == response_type
    assert room_failed_resp.response_message == "Exception: Just an error message"
    

def test_response_failure_from_empty_invalid_request_object():
    room_failed_resp = FailureResponseBuilder()\
                        .build_invalid_request_exception_object(InvalidRoomListRequestException())
    
    assert bool(room_failed_resp) is False
    # Assert that the response is a Failure
    assert room_failed_resp.response_type_to_dict == ResponseTypesEnums.FAILURE
    # Assert the cause of the Failure for more details
    assert room_failed_resp.cause_of_failure_to_dict == ResponseTypesEnums.PARAMETERS_ERROR
    
def test_response_failure_from_invalid_request_object_with_errors():
    exc = InvalidRoomListRequestException()
    
    exc.add_error(parameter='path', message='Is mandatory')
    exc.add_error(parameter='path', message='cannot be empty')
    room_failed_resp = FailureResponseBuilder()\
                        .build_invalid_request_exception_object(exc)
    
    assert bool(room_failed_resp) is False
    # Assert that the response is a Failure
    assert room_failed_resp.response_type_to_dict == ResponseTypesEnums.FAILURE
    # Assert the cause of the Failure for more details
    assert room_failed_resp.cause_of_failure_to_dict == ResponseTypesEnums.PARAMETERS_ERROR
    assert room_failed_resp.response_message == "path: Is mandatory\npath: cannot be empty"
    