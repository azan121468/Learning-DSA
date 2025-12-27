def uniquePaths(m: int, n: int) -> int:
    r, c = m, n  #just to ease of understanding

    #This time we will only use 1 row as we only need previous state of row and col which can be done in single row
    #1. Set whole row to 1 as there is only 1 way to reach first column and row
    dp = [1] * c

    #2. In each cell, we will put its current value(representing above cell) and cell at its left
    #we run this loop r times we get last row
    for _ in range(1, r):
        for i in range(1, c):
            dp[i] = dp[i-1] + dp[i]
        
    #return final cell
    return dp[c-1]


print(uniquePaths(3, 7))