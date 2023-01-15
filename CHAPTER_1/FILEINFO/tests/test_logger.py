from fileinfo.logger import Logger
from unittest.mock import patch

@patch('datetime.datetime')
def test_log(mock_now_datetime):
    test_now_datetime = 123
    mock_now_datetime.now.return_value = test_now_datetime
    test_message_text = "This is a test log message"
    l = Logger()
    l.log(test_message_text)
    assert l.messages ==  [(test_now_datetime, test_message_text)]
