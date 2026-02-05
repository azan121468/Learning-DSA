from samples import *

def setZeroes_marker(matrix: list[list[int]]) -> None:
    #Time Complexity: O(R*C), Space Complexity: O(R+C)
    r, c = len(matrix), len(matrix[0])
    rowMarker, colMarker = [False] * r, [False] * c

    #1. Set markers on if row and column has to be zeroed
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowMarker[i], colMarker[j] = True, True
    
    #2. Set current cell zero if either row or column marker is zero
    for i in range(r):
        for j in range(c):
            if rowMarker[i] or colMarker[j]:
                matrix[i][j] = 0

def setZeros_inplace(matrix: list[list[int]]) -> None:
    #Time Complexity: O(R*C), Space Complexity: O(1)
    r, c = len(matrix), len(matrix[0])

    #1. Check if first row has to be zero and store in flag
    row_zero = False
    for j in range(c):
        if matrix[0][j] == 0:
            row_zero = True
            break
    
    #2. Check if first column has to be zero out
    col_zero = False
    for i in range(r):
        if matrix[i][0] == 0:
            col_zero = True

    #3. Zero out whole matrix except first row and column.
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    #4. Zero out column if first cell is zero
    if col_zero:
        for i in range(r):
            matrix[i][0] = 0

    #5. Zero out row if row_zero flag is set
    if row_zero:
        for j in range(c):
            matrix[0][j] = 0

    

# setZeroes_marker(mat1)
# print(mat1)
# setZeroes_marker(mat2)
# print(mat2)
setZeros_inplace(mat1)
print(mat1)
setZeros_inplace(mat2)
print(mat2)