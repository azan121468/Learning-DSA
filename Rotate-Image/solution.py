from samples import *

def rotate(matrix: list) -> None:
    r, c = len(matrix), len(matrix[0]) 
    diag_idx = 0

    #main loop is to move along diagonal
    while diag_idx < r:
        #1. Swap element of row and column in current diagonal cell.
        rr, cc = diag_idx, diag_idx  #rr: row-wise movment, cc: column-wise movement
        while cc < c:
            matrix[rr][diag_idx], matrix[diag_idx][cc] = matrix[diag_idx][cc], matrix[rr][diag_idx]
            cc += 1
            rr += 1

        diag_idx += 1
    
    #2. now, we just have to reverse each row
    for rn in range(r):
        i, j = 0, c - 1
        while i < j:
            matrix[rn][i], matrix[rn][j] = matrix[rn][j], matrix[rn][i]
            i += 1
            j -= 1


rotate(input1)
print(input1)
rotate(input2)
print(input2)
rotate(input3)
print(input3)