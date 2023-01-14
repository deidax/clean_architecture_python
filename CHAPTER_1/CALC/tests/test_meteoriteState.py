import pytest
from unittest import mock
from unittest.mock import patch
from meteoriteStats.MeteoriteStats import MeteoriteStats
from .meteoriteStatsMockData import mock_data

@patch('urllib.request')
def test_average_mass(mock_urlopen):
    url = 'http://mock_url_api.test'
    
    def urlopen_test(url):
        return url

    m = MeteoriteStats()
    m.get_data = mock.Mock()
    mock_urlopen.urlopen.side_effect = urlopen_test
    mock_urlopen.urlopen(url)
    mock_urlopen.urlopen.assert_called_with(url)
    m.get_data.return_value = mock_data
    avg = m.average_mass(m.get_data())
    assert avg == 370.5
