class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


root = TreeNode(12)
child1 = TreeNode(11)
child2 = TreeNode(13)

root.left = child1
root.right = child2

print(root.left.value)
print(root.right.value)