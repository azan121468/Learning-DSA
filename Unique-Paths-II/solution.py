from sample import *

# Unique Paths II

#1. We have to set first row and column to 1s
#   but if encounter a obstacle, we will set that all subsequent cell to zero.
#2. Loop through remaining cells.
#   i. if obstacle, hit set that spot to 0
#   ii. otherwise, set that cell to sum of left and above cells values.
#3. After loop finishes, return last cell value as answer.

def uniquePathsWithObstacles(matrix: list) -> int:
    r, c = len(matrix), len(matrix[0])

    sol_grid = [[0] * c for _ in range(r)]

    for cn in range(c):
        if matrix[0][cn] == 0:
            sol_grid[0][cn] = 1
        else:
            break
    
    for rn in range(r):
        if matrix[rn][0] == 0:
            sol_grid[rn][0] = 1
        else:
            break
    
    for rn in range(1, r):
        for cn in range(1, c):
            if matrix[rn][cn] == 1: #hit obstacle
                sol_grid[rn][cn] = 0
            else:
                sol_grid[rn][cn] = sol_grid[rn-1][cn] + sol_grid[rn][cn-1]
    
    return sol_grid[-1][-1]

uniquePathsWithObstacles(grid2)