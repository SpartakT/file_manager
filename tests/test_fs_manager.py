import unittest
import os
import tempfile
import shutil
from unittest.mock import patch
from fs_manager import copy_file, delete_path, count_files, search_files, add_creation_date, analyze_sizes , human_readable_size

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

    def test_delete_path(self):
        delete_path(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))
        subdir = os.path.join(self.test_dir, "subdir")
        os.mkdir(subdir)
        delete_path(subdir)
        self.assertFalse(os.path.exists(subdir))

    def test_count_files(self):
        self.assertEqual(count_files(self.test_dir), 1)
        os.mkdir(os.path.join(self.test_dir, "subdir"))
        with open(os.path.join(self.test_dir, "subdir", "sub.txt"), "w") as f:
            f.write("sub")
        self.assertEqual(count_files(self.test_dir), 2)

    def test_search_files(self):
        results = search_files(self.test_dir, r"\.txt$")
        self.assertIn(self.test_file, results)

    def test_add_creation_date(self):
        add_creation_date(self.test_file)
        new_name = os.listdir(self.test_dir)[0]
        self.assertTrue(new_name.startswith("20"))

    def test_analyze_sizes(self):
        subdir = os.path.join(self.test_dir, "sub")
        os.mkdir(subdir)
        subfile = os.path.join(subdir, "sub.txt")
        with open(subfile, "w") as f:
            f.write("sub")
        expected_total = os.path.getsize(self.test_file) + os.path.getsize(subfile)
        expected_str = human_readable_size(expected_total)
        with patch('builtins.print') as mock_print:
            analyze_sizes(self.test_dir)
        printed = [str(call[0][0]) for call in mock_print.call_args_list if call[0]]
        self.assertTrue(any(expected_str in s for s in printed))


if __name__ == "__main__":
    unittest.main()