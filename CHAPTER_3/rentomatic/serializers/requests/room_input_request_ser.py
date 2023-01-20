from abc import ABC, abstractmethod

class RoomListInputRequestSeria(ABC):
    
    @staticmethod
    @abstractmethod
    def filters(filters) -> dict:
        pass
    