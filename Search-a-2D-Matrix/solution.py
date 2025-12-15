# we assume of matrix as a 1-D array
# given 1-D cordinate, we will convert into 2-D for comparison.
# binary search is super easy in 1-D
def searchMatrix(matrix, target):
    r, c = len(matrix), len(matrix[0])
    l, r = 0, r*c-1

    while l <= r:
        mid = (l + r) // 2
        x, y = mid // c, mid % c

        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            r = mid - 1
        elif matrix[x][y] < target:
            l = mid + 1

    return False

# for 2-D coordinate binary it code is attached as well. it is from while ago.
def searchMatrix2(matrix, target) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    # 1. Find correct row
    l, r = 0, rows - 1
    while l <= r:
        mid = (l + r) // 2
        value = matrix[mid][0]
        if value == target:
            return True
        elif value > target:
            r = mid - 1
        else:
            l = mid + 1
            
    row = r

    # 2. Do Binary Search in correct row against columns
    l, r = 0, cols - 1
    while l <= r:
        mid = (l + r) // 2
        value = matrix[row][mid]
        if value == target:
            return True
        elif value > target:
            r = mid - 1
        else:
            l = mid + 1

    return False


mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
ans = searchMatrix(mat, 13)
print(ans)