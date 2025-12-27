from test import root
from collections import deque

def dfs(node, word, i):

    if not node: return False
    if i >= len(word): return False

    if not node.left and not node.right and len(word) - 1 == i and node.val == word[i]:
        return True
    
    return node.val == word[i] and (dfs(node.left, word, i+1) or dfs(node.right, word, i+1))
    


def bfs(node):
    q = deque([node])
    levels = []

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        levels.append(level)
    
    return levels

hidden_word = 'azanshahid'
ans = dfs(root, hidden_word, 0)
print(ans)

# tree = bfs(root)
# for row in tree:
#     print(row)