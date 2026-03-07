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

    @patch("sys.argv", ["cli.py", "delete", "some_path"])
    @patch("filemanager.cli.delete_path")
    def test_delete(self, mock_delete):
        main()
        mock_delete.assert_called_once_with("some_path")

    @patch("sys.argv", ["cli.py", "count"])
    @patch("filemanager.cli.count_files")
    def test_count_default(self, mock_count):
        main()
        mock_count.assert_called_once_with(".")

    @patch("sys.argv", ["cli.py", "count", "some_dir"])
    @patch("filemanager.cli.count_files")
    def test_count_with_path(self, mock_count):
        main()
        mock_count.assert_called_once_with("some_dir")

    @patch("sys.argv", ["cli.py", "search", "pattern"])
    @patch("filemanager.cli.search_files")
    def test_search_default_path(self, mock_search):
        main()
        mock_search.assert_called_once_with(".", "pattern")

    @patch("sys.argv", ["cli.py", "search", "some_dir", "pattern"])
    @patch("filemanager.cli.search_files")
    def test_search_with_path(self, mock_search):
        main()
        mock_search.assert_called_once_with("some_dir", "pattern")


if __name__ == "__main__":
    unittest.main()