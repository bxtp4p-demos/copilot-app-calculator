import unittest
from file_manager import FileManager
import os

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_history.txt"
        self.history = ["add 1 + 1 = 2", "subtract 5 - 3 = 2"]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_initialization(self):
        fm = FileManager()
        self.assertIsNone(fm.filename)
        fm_with_filename = FileManager(self.test_file)
        self.assertEqual(fm_with_filename.filename, self.test_file)

    def test_set_filename(self):
        fm = FileManager()
        fm.set_filename(self.test_file)
        self.assertEqual(fm.filename, self.test_file)

    def test_save_to_file_no_filename(self):
        fm = FileManager()
        with self.assertRaises(ValueError):
            fm.save_to_file(self.history)

    def test_save_to_file_success(self):
        fm = FileManager(self.test_file)
        fm.save_to_file(self.history)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as file:
            content = file.readlines()
        self.assertIn("History of calculations:\n", content)
        for entry in self.history:
            self.assertIn(entry + "\n", content)

    def test_load_from_file_no_filename(self):
        fm = FileManager()
        with self.assertRaises(ValueError):
            fm.load_from_file()

    def test_load_from_file_success(self):
        fm = FileManager(self.test_file)
        fm.save_to_file(self.history)
        loaded_history = fm.load_from_file()
        self.assertEqual(len(loaded_history), len(self.history) + 1)  # Including the header
        for entry in self.history:
            self.assertIn(entry + "\n", loaded_history)

if __name__ == '__main__':
    unittest.main()