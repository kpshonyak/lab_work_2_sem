import unittest
from src.task import DisjointSet, merge_sort, merge, minimum_cable_length

class TestMinimumCableLength(unittest.TestCase):

    def test_disjoint_set(self):
        ds = DisjointSet(4)
        ds.union(0, 1)
        ds.union(2, 3)
        self.assertEqual(ds.find(0), ds.find(1))
        self.assertEqual(ds.find(2), ds.find(3))
        self.assertNotEqual(ds.find(0), ds.find(2))

    def test_merge_sort(self):
        edges = [(5, 0, 1), (1, 1, 2), (3, 2, 3)]
        sorted_edges = merge_sort(edges)
        self.assertEqual(sorted_edges, [(1, 1, 2), (3, 2, 3), (5, 0, 1)])

    def test_merge(self):
        left = [(3, 0, 1), (6, 1, 2)]
        right = [(2, 2, 3), (5, 3, 0)]
        result = merge(left, right)
        self.assertEqual(result, [(2, 2, 3), (3, 0, 1), (5, 3, 0), (6, 1, 2)])

    def test_minimum_cable_length(self):
        matrix = [
            [0, 2, 0, 6],
            [2, 0, 3, 8],
            [0, 3, 0, 0],
            [6, 8, 0, 0]
        ]
        result = minimum_cable_length(matrix)
        self.assertEqual(result, 11)  # MST: 2 + 3 + 6 = 11


