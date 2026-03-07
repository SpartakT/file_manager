import unittest
import os
import tempfile
import shutil
from unittest.mock import patch
from filemanager.fs_manager import copy_file, delete_path, count_files, search_files, add_creation_date, analyze_sizes , human_readable_size

class TestFSManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.txt")
        with open(self.test_file, "w") as f:
            f.write("test")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy_file(self):
        dest = os.path.join(self.test_dir, "copy.txt")
        copy_file(self.test_file, dest)
        self.assertTrue(os.path.exists(dest))


if __name__ == "__main__":
    unittest.main()