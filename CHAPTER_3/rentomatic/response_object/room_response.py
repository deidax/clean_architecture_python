from abc import ABC, abstractmethod
import json

class RoomResponse(ABC):
    
    
    def __init__(self) -> None:
        self._res_type = None
        self._res_value = None
        self._res_message = ''
        self._status_code = None
    
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
    
    @property
    def status_code(self):
        return self._status_code
    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    
    
    def __bool__(self):
        return self._res_type['value']
    
    def get_response(self):
        return {
            'type': self.response_type,
            'status_code': self.status_code,
            'message': self.response_message,
            'response': self.response_value
        }
    
    
    @abstractmethod
    def json_ser(self, encoder: json.JSONEncoder) -> json:
        pass