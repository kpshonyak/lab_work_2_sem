import unittest
from task import find_kth_largest

class TestAlgorithm(unittest.TestCase):
    def test_kth_largest(self):
        self.assertEqual(find_kth_largest([15, 7, 22, 9, 36, 2, 42, 18], 3), (22, 2))
        self.assertEqual(find_kth_largest([10, 20, 30, 40, 50], 1), (50, 3))
        self.assertEqual(find_kth_largest([4, 6, 2, 9, 1], 2), (6, 1))
    
    def test_invalid_k(self):
        self.assertRaises(ValueError,find_kth_largest,[1, 2],3)
        
