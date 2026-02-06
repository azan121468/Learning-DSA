from samples import *

#DFS from each cell in grid in all directions to find word
def exist(board: list[list[str]], word: str) -> bool:
    r, c = len(board), len(board[0])

    inbound = lambda x, y: 0 <= x < r and 0 <= y < c

    # visited = set()
    def dfs(i, j, idx):
        if idx == len(word): return True

        # if not inbound(i, j) or (i, j) in visited or board[i][j] != word[idx]:
        if not inbound(i, j) or board[i][j] == '#' or board[i][j] != word[idx]:
            return False

        # visited.add((i, j))
        tmp = board[i][j]
        board[i][j] = '#'

        res = dfs(i+1, j, idx + 1) \
            or dfs(i-1, j, idx + 1) \
            or dfs(i, j+1, idx + 1) \
            or dfs(i, j-1, idx + 1)

        # visited.remove((i, j))
        board[i][j] = tmp
        

        return res
    
    for i in range(r):
        for j in range(c):
            if dfs(i, j, 0):
                return True
    
    return False

print(exist(*sample1))
print(exist(*sample2))
print(exist(*sample3))