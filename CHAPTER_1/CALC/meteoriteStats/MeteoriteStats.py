import urllib.request
import json
from calc.calc import Calc

class MeteoriteStats():
    
    _URL = ("https://data.nasa.gov/resource/y77d-th95.json")

    def get_data(self):
        with urllib.request.urlopen(self._URL) as url:
            return json.loads(url.read().decode())
    def average_mass(self, data):
        c = Calc()
        masses = [float(d['mass']) for d in data if 'mass' in d]
        return c.avg(masses)