import unittest
from unittest.mock import patch
from filemanager.cli import main

class TestCLI(unittest.TestCase):

    @patch("sys.argv", ["cli.py", "copy", "source.txt"])
    @patch("filemanager.cli.copy_file")
    def test_copy_without_destination(self, mock_copy):
        main()
        mock_copy.assert_called_once_with("source.txt", "source.txt_copy")

    @patch("sys.argv", ["cli.py", "copy", "source.txt", "dest.txt"])
    @patch("filemanager.cli.copy_file")
    def test_copy_with_destination(self, mock_copy):
        main()
        mock_copy.assert_called_once_with("source.txt", "dest.txt")


if __name__ == "__main__":
    unittest.main()