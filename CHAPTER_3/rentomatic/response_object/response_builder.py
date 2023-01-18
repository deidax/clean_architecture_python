from abc import ABC, abstractmethod

class ResponseBuilder(ABC):
    """
    This is a builder interface to specifie methods for creating
    the different parts of the Response object
    """
    
    @staticmethod
    @abstractmethod
    def set_value(value=None):
        pass
    
    @staticmethod
    @abstractmethod
    def default_type():
        pass
    
    @staticmethod
    @abstractmethod
    def set_response_message(message_value=''):
        pass
    
    @staticmethod
    @abstractmethod
    def build_response():
        pass
    
    @staticmethod
    @abstractmethod
    def set_response_message_and_build(message_value=''):
        pass