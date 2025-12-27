from graph import *

def cloneGraph(root):
    if not root: return None

    stack = [root]
    old_to_new = {}

    while stack:
        node = stack.pop()

        if node in old_to_new:  #we don't want to visit this node as it is already processed
            continue
        
        old_to_new[node] = Node(node.val)
    
        for nei in node.neighbors:
            stack.append(nei)
    
    for node in old_to_new:
        for nei in node.neighbors:
            old_to_new[node].neighbors.append(old_to_new[nei])
        
    return old_to_new[root]

cg = cloneGraph(root)
print(verify_graph(cg, root))