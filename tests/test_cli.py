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

    @patch("sys.argv", ["cli.py", "add_date", "some_path"])
    @patch("filemanager.cli.add_creation_date")
    def test_add_date_non_recursive(self, mock_add_date):
        main()
        mock_add_date.assert_called_once_with("some_path", False)

    @patch("sys.argv", ["cli.py", "add_date", "some_path", "--recursive"])
    @patch("filemanager.cli.add_creation_date")
    def test_add_date_recursive(self, mock_add_date):
        main()
        mock_add_date.assert_called_once_with("some_path", True)

    @patch("sys.argv", ["cli.py", "analyse"])
    @patch("filemanager.cli.analyze_sizes")
    def test_analyse_default(self, mock_analyse):
        main()
        mock_analyse.assert_called_once_with(".")

    @patch("sys.argv", ["cli.py", "analyse", "some_dir"])
    @patch("filemanager.cli.analyze_sizes")
    def test_analyse_with_path(self, mock_analyse):
        main()
        mock_analyse.assert_called_once_with("some_dir")

    @patch("sys.argv", ["cli.py"])
    def test_no_arguments(self):
        with self.assertRaises(SystemExit):
            main()

if __name__ == "__main__":
    unittest.main()