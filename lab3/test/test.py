import unittest
import filecmp
import os
from main import *


class TestHamsters(unittest.TestCase):

    def setUp(self):
        self.hamster_results_file1_path = "hamsters_results1.txt"
        self.hamster_results_file2_path = "hamsters_results2.txt"
        self.hamster_results_file3_path = "hamsters_results3.txt"

    def test_hamsters(self):
        main("hamsters_data1.txt")
        self.assertTrue(filecmp.cmp("hamsters_out.txt", self.hamster_results_file1_path, shallow=False))
        main("hamsters_data2.txt")
        self.assertTrue(filecmp.cmp("hamsters_out.txt", self.hamster_results_file2_path, shallow=False))
        main("hamsters_data3.txt")
        self.assertTrue(filecmp.cmp("hamsters_out.txt", self.hamster_results_file3_path, shallow=False))
        os.remove("hamsters_out.txt")


if __name__ == "__main__":
    unittest.main()
