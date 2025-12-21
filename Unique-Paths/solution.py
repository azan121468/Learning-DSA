def uniquePaths(m: int, n: int) -> int:
    r, c = m, n       #renaming for simiplicity

    #1. make the grid
    dp = [[0] * c for _ in range(r)]

    #2. Set first row can column to 1s as there is no only one way to reach each cell
    #2.1  Set row to 1
    dp[0] = [1] * c

    #2.2 Set column to 1
    for row in dp:
        row[0] = 1
    
    #3. For remaining, number of path to reach each cell is just sum its above and left cell.
    for rn in range(1, r):
        for cn in range(1, c):
            dp[rn][cn] = dp[rn-1][cn] + dp[rn][cn-1]

    #4. Return value at last cell
    # return grid[rn][cn]  #this is also same as last call bcz rn and cn at end of loop will contain last value of rn and cn which corresponds to last cell
    return dp[r-1][c-1]  #better way is just to just access last cell by length of row and columns than depending on rn and cn from the loop

print(uniquePaths(3, 7))