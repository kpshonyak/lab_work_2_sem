import unittest
from src.task  import find_min_depth

class TestMinDepth(unittest.TestCase):

    def test_simple_tree(self):
        root = 1
        graph = {
            1: [2, 3],
            2: [4],
            3: [6],
            4: [5]
        }
        self.assertEqual(find_min_depth(root, graph), 3)

    def test_single_node(self):
        root = 1
        graph = {}
        self.assertEqual(find_min_depth(root, graph), 1)

    def test_deep_chain(self):
        root = 1
        graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [5]
        }
        self.assertEqual(find_min_depth(root, graph), 5)

    def test_wide_tree(self):
        root = 10
        graph = {
            10: [11, 12, 13],
            11: [],
            12: [14],
            13: [15]
        }
        self.assertEqual(find_min_depth(root, graph), 2)

    def test_unbalanced_tree(self):
        root = 1
        graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [],
            1: [5],
            5: []
        }
        # хоч є довга гілка через 2-3-4, але коротка — 1 → 5
        self.assertEqual(find_min_depth(root, graph), 2)
