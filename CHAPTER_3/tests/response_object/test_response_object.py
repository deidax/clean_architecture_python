from rentomatic.response_object.success_response import SuccessResponse

def test_response_success_is_true():
    assert bool(SuccessResponse()) is True
