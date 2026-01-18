from sample import *

#Pacific Atlantic Water Flow
#1. Idea is to start DFS from all border cells and try to reach all inner cells.
#   We will perform DFS in reverse order. Instead of trying to reach oceans from each cell, we will be trying to reach each cell from oceans.
#   For Pacific, we start DFS from first row and first column.
#   For Atlantic, we start DFS from last row and last column.
#We keep track of each cell of ocean separately in two hashsets.
#2. Once all DFS are completed, we have two hashsets containing coordinates which can reach pacific and altlantic respectively.
#We can return intersection of these two sets, as it means these cells can reach both pacific and atlantic. 

def pacificAtlantic(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])

    inbound = lambda x, y: 0 <= x < rows and 0 <= y < cols

    def dfs(i, j, visited, prevHeight):
        if not inbound(i, j) or (i, j) in visited or grid[i][j] < prevHeight:
            return
        
        visited.add((i, j))

        dfs(i+1, j, visited, grid[i][j])
        dfs(i-1, j, visited, grid[i][j])
        dfs(i, j+1, visited, grid[i][j])
        dfs(i, j-1, visited, grid[i][j])
    
    pac, atl = set(), set()

    #DFS from Pacific Ocean
    for i in range(rows): # First column
        dfs(i, 0, pac, grid[i][0])
    for i in range(cols): # First row
        dfs(0, i, pac, grid[0][i])
    
    #DFS from Atlantic Ocean
    for i in range(rows): #Last column
        dfs(i, cols-1, atl, grid[i][cols-1])
    for i in range(cols): #Last row
        dfs(rows-1, i, atl, grid[rows-1][i])
    
    #now, get intersection of cells to find out which cells can reach both pacific and atlantic
    ans = pac.intersection(atl)
    ans = [list(i) for i in ans]
    return ans

ans = pacificAtlantic(heights1)
print(ans)