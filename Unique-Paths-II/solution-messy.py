from sample import *

def uniquePathsWithObstacles(matrix: list) -> int:
    r, c = len(matrix), len(matrix[0])

    sol_grid = [[0] * c for _ in range(r)]

    hit_obstacle = False
    for cn in range(c):
        if not hit_obstacle:
            if matrix[0][cn] == 1:
                hit_obstacle = True
            sol_grid[0][cn] = 1 if not hit_obstacle else 0
        else:
            sol_grid[0][cn] = 0
    
    hit_obstacle = False
    for rn in range(r):
        if not hit_obstacle:
            if matrix[rn][0] == 1:
                hit_obstacle = True
            sol_grid[rn][0] = 1 if not hit_obstacle else 0
        else:
            sol_grid[rn][0] = 0
    
    for rn in range(1, r):
        for cn in range(1, c):
            if matrix[rn][cn] == 1: #hit obstacle
                sol_grid[rn][cn] = 0
            else:
                sol_grid[rn][cn] = sol_grid[rn-1][cn] + sol_grid[rn][cn-1]
    
    return sol_grid[-1][-1]

uniquePathsWithObstacles(grid2)