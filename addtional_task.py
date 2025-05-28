class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sumAllLeaves(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return root.value
    
    return sumAllLeaves(root.left) + sumAllLeaves(root.right)

root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(7)
root.right.right = BinaryTree(18)

print(sumAllLeaves(root))