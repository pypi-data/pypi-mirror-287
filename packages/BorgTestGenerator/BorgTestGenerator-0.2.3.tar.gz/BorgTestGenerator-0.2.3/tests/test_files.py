import unittest
from BorgTestGenerator.utils.files import read_text_file

class TestFiles(unittest.TestCase):
    def test_read_text_file(self):
        # Test case 1: Existing file
        file_path = "/path/to/existing/file.txt"
        expected_output = "This is the content of the file."
        self.assertEqual(read_text_file(file_path), expected_output)

        # Test case 2: Non-existing file
        file_path = "/path/to/non_existing/file.txt"
        self.assertIsNone(read_text_file(file_path))

if __name__ == "__main__":
    unittest.main()