import unittest
import filecmp
import os

from lab6.main import main


class TestIjones(unittest.TestCase):

    def setUp(self):
        self.ijones_results_file1_path = "ijones_results1.txt"
        self.ijones_results_file2_path = "ijones_results2.txt"
        self.ijones_results_file3_path = "ijones_results3.txt"

    def test_ijones(self):
        main("ijones_data1.txt")
        self.assertTrue(filecmp.cmp("ijones_out.txt", self.ijones_results_file1_path, shallow=False))
        main("ijones_data2.txt")
        self.assertTrue(filecmp.cmp("ijones_out.txt", self.ijones_results_file2_path, shallow=False))
        main("ijones_data3.txt")
        self.assertTrue(filecmp.cmp("ijones_out.txt", self.ijones_results_file3_path, shallow=False))
        os.remove("ijones_out.txt")


if __name__ == "__main__":
    unittest.main()
