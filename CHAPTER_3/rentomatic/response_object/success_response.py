
class SuccessResponse:
    
    def __init__(self, value=None) -> None:
        self.value = value
    
    def __bool__(self):
        return True
    