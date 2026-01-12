class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.val})"

root1 = TreeNode(
    3,
    TreeNode(1, None, TreeNode(2)),  # left child with a right child
    TreeNode(4)                       # right child
)
k1 = 1

root2 = TreeNode(
    5,
    TreeNode(
        3,
        TreeNode(
            2,
            TreeNode(1)   # left child of 2
        ),
        TreeNode(4)       # right child of 3
    ),
    TreeNode(6)           # right child of 5
)
k2 = 3