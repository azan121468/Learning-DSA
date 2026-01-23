from collections import defaultdict
from samples import *

def validTree(n: int, edges: list[list[int]]) -> bool:
    if n == 0:      #empty input is also considered valid tree
        return True

    #make adjacency list
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    visited = set()
    def dfs(cur, parent):
        if cur in visited:  #cycle is detected
            return False
        
        visited.add(cur)

        for child in adj[cur]:
            #in an undirected graph, visiting parent from child will lead to False cycle detection.
            if child == parent:
                continue

            #if dfs return False due to cycle, immediately return False
            if not dfs(child, cur):
                return False
        
        return True

    return dfs(0, -1) and len(visited) == n  #second condition is to make sure that we have visited all nodes and there are no orphan nodes.

ans = validTree(*input1)
print(ans)
ans = validTree(*input2)
print(ans)