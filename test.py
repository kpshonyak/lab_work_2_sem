import unittest
from lab2 import max_hamsters 

class TestHamsters(unittest.TestCase):
    def test_cases1(self):
        self.assertEqual(max_hamsters(7, 3, [[1,2], [2, 2], [3, 1]]), 2)
    def test_cases2(self):
        self.assertEqual(max_hamsters(20, 4, [[5, 0], [2, 2], [1, 4], [5, 1]]), 3)
    def test_cases3(self):
        self.assertEqual(max_hamsters(2, 2, [[1, 50000], [1, 60000]]), 1)
    def test_cases4(self):
        self.assertEqual(max_hamsters(5, 1, [[3, 2]]), 1)