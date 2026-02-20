import unittest
from unittest.mock import patch
import sys
from cli import main

class TestCLI(unittest.TestCase):
    @patch("sys.argv", ["cli.py", "copy", "test.txt"])
    @patch("fs_manager.copy_file")
    def test_copy_command(self, mock_copy):
        with self.assertRaises(SystemExit):
            main()
        mock_copy.assert_called()


if __name__ == "__main__":
    unittest.main()