from samples import *

#Traverse through nodes using BST property that left.val < node.val < right.val.
# Move down the tree like a BST search:
# - If both p and q are greater than current, go right
# - If both are smaller, go left
# - otherwise current node is LCA

def LCA_iterative(root, p, q):
    if not root: return None
    if p == q: return p

    if p.val > q.val:
        p, q = q, p
    
    cur = root
    while cur:
        if p.val > cur.val:
            cur = cur.right
        elif q.val < cur.val:
            cur = cur.left
        else:
            return cur

def LCA_recursive(root, p, q):
    if not root: return None
    if p == q: return p

    if p.val > root.val:
        return LCA_recursive(root.right, p, q)
    if q.val < root.val:
        return LCA_recursive(root.left, p, q)

    return root

node = LCA_iterative(root1, n2, n8)
print(node.val)

node = LCA_iterative(root2, m2, m4)
print(node.val)

assert LCA_iterative(root1, n2, n8) == LCA_recursive(root1, n2, n8)
assert LCA_iterative(root2, m2, m4) == LCA_recursive(root2, m2, m4)