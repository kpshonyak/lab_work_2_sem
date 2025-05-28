class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    def dfs(node,is_right):
        if not node:
            return 0
        
        if not node.left and not node.right and is_right:
            return node.value
        
        return dfs(node.left, False) + dfs(node.right, True)
    
    return dfs(root, False)
root = BinaryTree(1)
root.right = BinaryTree(2)
root.right.right = BinaryTree(3)
print(branchSums(root))