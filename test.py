import unittest
import HeapSort
from BinarySearchTree import *


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.asc_sorted_array = [1, 2, 4, 6, 7, 8, 100, 120]
        self.desc_sorted_array = [120, 100, 8, 7, 6, 4, 2, 1]
        self.unsorted_array = [2, 1, 4, 8, 7, 6, 120, 100]

    def test_sorting(self):
        HeapSort.args.sorting_array = self.unsorted_array
        testing_array = HeapSort.main()
        is_sorted = all(testing_array[i] >= testing_array[i + 1] for i in range(len(testing_array) - 1))
        self.assertTrue(is_sorted)

    def test_asc_by_asc_sorted_array(self):
        HeapSort.args.sorting_array = self.asc_sorted_array
        HeapSort.args.order = "asc"
        self.assertEqual(HeapSort.main(), self.asc_sorted_array)

    def test_asc_by_desc_sorted_array(self):
        HeapSort.args.sorting_array = self.desc_sorted_array
        HeapSort.args.order = "asc"
        self.assertEqual(HeapSort.main(), self.asc_sorted_array)

    def test_desc_by_asc_sorted_array(self):
        HeapSort.args.sorting_array = self.asc_sorted_array
        HeapSort.args.order = "desc"
        self.assertEqual(HeapSort.main(), self.desc_sorted_array)

    def test_desc_by_desc_sorted_array(self):
        HeapSort.args.sorting_array = self.desc_sorted_array
        HeapSort.args.order = "desc"
        self.assertEqual(HeapSort.main(), self.desc_sorted_array)

    def test_binary_tree_inserting(self):
        binary_search_tree = BinarySearchTree(Node(2))
        binary_search_tree.insert(binary_search_tree.root, 1)
        binary_search_tree.insert(binary_search_tree.root, 6)
        self.assertEqual(binary_search_tree.root.right.data, 6)
        self.assertEqual(binary_search_tree.root.left.data, 1)

    def test_binary_tree_deleting(self):
        binary_search_tree = BinarySearchTree(Node(2))
        binary_search_tree.insert(binary_search_tree.root, 1)
        binary_search_tree.insert(binary_search_tree.root, 6)
        binary_search_tree.insert(binary_search_tree.root, 7)
        binary_search_tree.delete_node(binary_search_tree.root, 6)
        self.assertEqual(binary_search_tree.root.right.data, 7)


if __name__ == "__main__":
    unittest.main()
