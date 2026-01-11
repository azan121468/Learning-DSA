from sample import *

def kthSmallest(root: TreeNode, k: int) -> int:
    def dfs(node):
        if not node: return None

        yield from dfs(node.left)
        yield node.val
        yield from dfs(node.right)
    
    g = dfs(root)

    for i, x in enumerate(g):
        if i == k - 1:
            return x

ans = kthSmallest(root1, k1)
print(ans)
ans = kthSmallest(root2, k2)
print(ans)