
class SuccessResponse:
    
    
    def __init__(self) -> None:
        self._res_type = None
        self._res_value = None
        self._res_message = ''
    
    @property
    def response_value(self):
        return self._res_value
    
    @response_value.setter
    def response_value(self, value):
        self._res_value = value
    
    @property
    def response_type(self):
        return self._res_type['label']
    
    @response_type.setter
    def response_type(self, value):
        self._res_type = value
    
    @property
    def response_message(self):
        return self._res_message
    
    @response_message.setter
    def response_message(self, value):
        self._res_message = self._format_message(value)
    
    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg
    
    def __bool__(self):
        return self._res_type['value']