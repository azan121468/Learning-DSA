'''
Given
[1, 2, 3]  0,0  0,1  0,2
[4, 5, 6]  1,0  1,1  1,2
[7, 8, 9]  2,0  2,1  2,2 
Required
[3, 6, 9]  0,2  1,2  2,2
[2, 5, 8]  0,1  1,1  2,1
[1, 4, 7]  0,0  1,0  2,0
'''

def rotate_90(matrix):
    if not matrix:
        return []
    
    r, c = len(matrix), len(matrix[0])
    rotated = []

    for ci in range(c - 1, -1, -1):
        col = [matrix[i][ci] for i in range(r)]
        rotated.append(col)
    
    return rotated

def spiral_matrix(matrix):
    out = []

    while matrix:
        out.extend(matrix[0])
        matrix = matrix[1:]
        matrix = rotate_90(matrix)
    
    return out
        

mat = \
   [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print(spiral_matrix(mat))
