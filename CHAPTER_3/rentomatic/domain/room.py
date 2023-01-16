
class Room:
    
    def __init__(self, code, size, price, longitude, latitude) -> None:
        self.code=code
        self.size=size
        self.price=price
        self.longitude=longitude
        self.latitude=latitude
    
    
    """ 
    We might receive data to initialise
    this model from other layers and this data
    is likely to be a dictionary.
    """
    @classmethod
    def from_dict(cls, dict_data):
        r = cls(
            code = dict_data['code'],
            size = dict_data['size'],
            price = dict_data['price'],
            longitude = dict_data['longitude'],
            latitude = dict_data['latitude']
        )
        return r

    """
    Convert Room object to a dict
    """
    def to_dict(self):
        return {
            'code': self.code,
            'size': self.size,
            'price': self.price,
            'longitude': self.longitude,
            'latitude': self.latitude
        }
    
    """
    Configuration of comparison operator
    """
    def __eq__(self, __o: object) -> bool:
        return self.to_dict() == __o.to_dict()