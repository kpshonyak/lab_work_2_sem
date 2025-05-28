import unittest
from task import BinaryTree, branchSums

class TestBranchSums(unittest.TestCase):
    #def test_example_case(self):
        #root = BinaryTree(3)
        #root.left = BinaryTree(9)
        #root.right = BinaryTree(20)
        #root.right.left = BinaryTree(15)
        #root.right.right = BinaryTree(7)
        #self.assertEqual(branchSums(root), 24)
    
    #def test_only_right_nodes(self):
        #root = BinaryTree(1)
        #root.right = BinaryTree(2)
        #root.right.right = BinaryTree(3)
        #self.assertEqual(branchSums(root), 0)
    
    #def test_only_left_nodes(self):
        #root = BinaryTree(1)
        #root.left = BinaryTree(2)
        #root.left.left = BinaryTree(3)
        #self.assertEqual(branchSums(root), 3)
    
    def test_mixed_tree(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right.right = BinaryTree(18)
        self.assertEqual(branchSums(root), 28)
    
    #def test_empty_tree(self):
        #self.assertEqual(branchSums(None), 0)