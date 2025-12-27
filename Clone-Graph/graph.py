class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# i tried but there were many edges so i ask chatgpt to write for me
# visited = set()
# def verify(original, copy):
#     if (original and not copy) or (not original and copy):
#         return False

#     if original in visited:
#         return True
    
#     visited.add(original)


    
#     return original != copy and original.val == copy.val and \
        
#         # all(verify(onei, cnei) for onei, cnei in zip(original.neighbors, copy.neighbors))

def verify_graph(original, copy):
    """
    Verifies that 'copy' is a deep clone of 'original'.
    Returns True if it is, False otherwise.
    """
    if not original and not copy:
        return True
    if not original or not copy:
        return False

    visited = {}  # maps original node -> cloned node

    def dfs(o, c):
        if o in visited:
            # Already visited: make sure it's mapped to the same clone
            return visited[o] is c

        if o == c or o.val != c.val:
            return False

        visited[o] = c

        if len(o.neighbors) != len(c.neighbors):
            return False

        for onei in o.neighbors:
            # Each neighbor must have a corresponding clone in c.neighbors
            # We find the cloned neighbor by using dfs on each possibility
            if not any(dfs(onei, cnei) for cnei in c.neighbors):
                return False

        return True

    return dfs(original, copy)


#make a simple connected graph
'''
       1      2
    
       3      4
'''

n1, n2, n3, n4 = [Node(i) for i in range(1, 4+1)]
n1.neighbors.extend([n2, n3])
n2.neighbors.extend([n1, n4])
n3.neighbors.extend([n1, n4])
n1.neighbors.extend([n2, n3])

root = n1