import unittest

import HeapSort
from BinarySearchTree import *
from DijkstraAlgorithm import *


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        self.asc_sorted_array = [1, 2, 4, 6, 7, 8, 100, 120]
        self.desc_sorted_array = [120, 100, 8, 7, 6, 4, 2, 1]
        self.unsorted_array = [2, 1, 4, 8, 7, 6, 120, 100]

        self.vertex_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                              [4, 0, 8, 0, 0, 0, 0, 11, 0],
                              [0, 8, 0, 7, 0, 4, 0, 0, 2],
                              [0, 0, 7, 0, 9, 14, 0, 0, 0],
                              [0, 0, 0, 9, 0, 10, 0, 0, 0],
                              [0, 0, 4, 14, 10, 0, 2, 0, 0],
                              [0, 0, 0, 0, 0, 2, 0, 1, 6],
                              [8, 11, 0, 0, 0, 0, 1, 0, 7],
                              [0, 0, 2, 0, 0, 0, 6, 7, 0]]
        self.starting_vertex = 0

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

    def test_dijkstra_algorithm_test(self):
        graph = Graph(len(self.vertex_matrix))
        graph.vertices_matrix = self.vertex_matrix
        distances_list = graph.dijkstra_search(self.starting_vertex)
        benchmark_distances_array = [0, 4, 12, 19, 21, 11, 9, 8, 14]
        self.assertEqual(distances_list, benchmark_distances_array)


if __name__ == "__main__":
    unittest.main()
