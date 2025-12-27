from samples import *

def numIslands(grid: list) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    inbound = lambda x,y : 0 <= x < ROWS and 0 <= y < COLS

    def dfs(i, j):
        #we stop dfs on either
        #1. Water, 2. Out-of-bound 3. Cell already has been visited
        #tho i think visited check is redundant as we already do it before function
        if not inbound(i, j) or grid[i][j] == "0" or (i, j) in visited:
            return

        visited.add((i, j))

        #We will not visited above and left, bcz they are already covered, 
        #since we are coming from above or left, we only expand right and down
        #for loop order is from above and left, so we don't  move back to those dirs
        
        #assumption above is wrong, see sample 4 for understanding
        dfs(i+1, j)
        dfs(i, j+1)

    island_count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in visited or grid[r][c] == "0":
                continue
            island_count += 1
            dfs(r, c)
    
    return island_count

n = numIslands(grid1)
print(n)
n = numIslands(grid2)
print(n)
n = numIslands(grid3)
print(n)
n = numIslands(grid4)
print(n)