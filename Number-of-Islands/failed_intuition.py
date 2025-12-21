from samples import *

def numIslands(grid: list) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    # my initial idea was that we can detect start of island by checking if 
    # left and above element are water which is not correct.
    # see failed test case
    island_count = 0
    for r in range(ROWS):
        for c in range(COLS):
            up = grid[r-1][c] if r > 0 else "0"
            left   = grid[r][c-1] if c > 0 else "0"
            if grid[r][c] == "1" and up == left == "0":
                island_count += 1
    
    return island_count

c1 = numIslands(grid1)
c2 = numIslands(grid2)
c3 = numIslands(grid3)

print(c1)
print(c2)
print(c3)

'''
Failed Test Case
0 1
1 1

my code out two islands from cells (0, 1) and (1, 0) while only one of them should
have been count
'''