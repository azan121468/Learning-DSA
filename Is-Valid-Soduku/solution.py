
def get_box(board):
    boxes = []
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            box = []
            for i in range(3):
                box.extend(
                    board[row_start+i][col_start:col_start+3]
                )
            boxes.append(box)
    return boxes

def isValidSudoku(board):
    # Get all 3x3 boxes
    boxes = get_box(board)

    # 1. all values in 3x3 box should be unique
    for box in boxes:
        seen = set()
        # Check if box has value repeated, return False
        for val in box:
            if val in seen and val != '.':
                return False
            seen.add(val)
    
    #2. all rows are unique
    #for r in range(board)
    for r in range(9):
        seen = set()
        for val in board[r]:
            if val in seen and val != '.':
                return False
            seen.add(val)
    
    # #3. all columns are unique
    for c in range(9):
        col = []
        for r in range(9):
            col.append(board[r][c]) # i know that here it can be optimized by not making col but directly adding in seen and checking but just for better understanding
        
        seen = set()

        for val in col:
            if val in seen and val != '.':
                return False
            seen.add(val)
        

    return True

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]



print(isValidSudoku(board))
