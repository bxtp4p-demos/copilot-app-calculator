import unittest
from history_manager import HistoryManager

class TestHistoryManager(unittest.TestCase):
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_initialization(self):
        self.assertEqual(len(self.history_manager.get_history()), 0, "History should be empty upon initialization")

    def test_add_entry(self):
        self.history_manager.add_entry("add", 1, 2, result=3)
        self.assertEqual(self.history_manager.get_history(), ["add(1, 2) = 3"], "Failed to add a single entry correctly")

        self.history_manager.add_entry("multiply", 3, 4, result=12)
        self.assertEqual(self.history_manager.get_history(), ["add(1, 2) = 3", "multiply(3, 4) = 12"], "Failed to add multiple entries correctly")

        self.history_manager.add_entry("concat", "Hello, ", "world!", result="Hello, world!")
        self.assertEqual(self.history_manager.get_history(), ["add(1, 2) = 3", "multiply(3, 4) = 12", "concat(Hello, , world!) = Hello, world!"], "Failed to handle string operands correctly")

    def test_clear_history(self):
        self.history_manager.add_entry("add", 1, 2, result=3)
        self.history_manager.clear_history()
        self.assertEqual(len(self.history_manager.get_history()), 0, "Failed to clear history correctly")

    def test_get_history(self):
        self.history_manager.add_entry("add", 1, 2, result=3)
        self.assertEqual(self.history_manager.get_history(), ["add(1, 2) = 3"], "get_history did not return the correct entries")

        self.history_manager.clear_history()
        self.assertEqual(len(self.history_manager.get_history()), 0, "get_history did not return an empty list after clearing history")

if __name__ == '__main__':
    unittest.main()