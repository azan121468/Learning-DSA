from samples import *

def numIslands(grid: list) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    inbound = lambda x, y: 0 <= x < ROWS and 0 <= y < COLS

    visited = set()
    def dfs(i, j):
        if not inbound(i, j) or grid[i][j] == "0" or (i, j) in visited:
            return

        visited.add((i, j))

        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    num_of_islands = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "0" or (r, c) in visited:
                continue
            num_of_islands += 1
            dfs(r, c)
    
    return num_of_islands

n = numIslands(grid1)
print(n)
n = numIslands(grid2)
print(n)
n = numIslands(grid3)
print(n)
n = numIslands(grid4)
print(n)