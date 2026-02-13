from collections import deque
from sample import *

def pacificAtlantic(grid: list[list[int]]) -> list[list[int]]:
    ROWS, COLS = len(grid), len(grid[0])
    inbound = lambda x, y: 0 <= x < ROWS and 0 <= y < COLS

    pac, atl = set(), set() #these sets will contain cells which can reach pacific and atlantic respectively
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = deque()
    for i in range(COLS): #every element of first row can reach pacific
        q.append((0, i))
    for i in range(1, ROWS): #every element of first column can reach pacific
        q.append((i, 0))
    
    while q:
        cord_x, cord_y = q.popleft()
        if (cord_x, cord_y) in pac: continue
        pac.add((cord_x, cord_y))
        for dx, dy in dirs:
            new_x, new_y = cord_x + dx, cord_y + dy
            if inbound(new_x, new_y) and grid[new_x][new_y] >= grid[cord_x][cord_y]:
                q.append((new_x, new_y))

    #python based negative indexing won't work as it failed bound checks so cells neighbors cells aren't visited and also visit set contains coordinate in python -ve indexing format which is not valid for solution set
    #wrong code has been commented
    q = deque()
    for i in range(COLS): #last row
        # q.append((-1, i))
        q.append((ROWS - 1, i))
    for i in range(ROWS - 1): #last column, -1 is to make sure that last cell is not added twice.
        # q.append((i, -1))
        q.append((i, COLS - 1))

    while q:
        cord_x, cord_y = q.popleft()
        if (cord_x, cord_y) in atl: continue
        atl.add((cord_x, cord_y))
        for dx, dy in dirs:
            new_x, new_y = cord_x + dx, cord_y + dy
            if inbound(new_x, new_y) and grid[new_x][new_y] >= grid[cord_x][cord_y]:
                q.append((new_x, new_y))
    
    # print(pac)
    # print(atl)
    # print(pac.intersection(atl))
    return pac.intersection(atl)

res = pacificAtlantic(heights1)
print(res)
res = pacificAtlantic(heights2)
print(res)