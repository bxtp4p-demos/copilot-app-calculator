import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from history_entry import HistoryEntry

class TestHistoryEntry(unittest.TestCase):
    def test_initialization(self):
        """Test that a HistoryEntry is correctly initialized with a message and a timestamp."""
        message = "Test message"
        entry = HistoryEntry(message)
        self.assertEqual(entry.message, message)
        self.assertTrue(isinstance(entry.timestamp, datetime))

        # Test that the timestamp is within 1 second of the current time
        self.assertTrue(abs(entry.timestamp - datetime.now()) <= timedelta(seconds=1))

    @patch('history_entry.datetime')
    def test_repr(self, mock_datetime):
        """Test the string representation of a HistoryEntry."""
        # Setup a fixed datetime for testing
        test_time = datetime(2020, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = test_time

        message = "Test message"
        entry = HistoryEntry(message)
        expected_repr = f"{test_time}: {message}"
        self.assertEqual(repr(entry), expected_repr)

if __name__ == '__main__':
    unittest.main()