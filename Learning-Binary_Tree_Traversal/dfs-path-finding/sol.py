from test import *

paths = []

def dfs(node, path):
    if not node:
        return

    path.append(node.val)
    
    if not node.left and not node.right:
        paths.append(path.copy())
    
    dfs(node.left, path)
    dfs(node.right, path)

    path.pop()

dfs(root, [])
print(paths)