#0: no orange
#1: fresh orange
#2: rotten orange

#Perform multi-source BFS from all rotten oranges at same time.

from sample import *
from collections import deque

def orangesRotting(grid: list) -> int:
    FRESH, ROTTEN = 1, 2

    rn, cn = len(grid), len(grid[0])

    inbound = lambda x, y: 0 <= x < rn and 0 <= y < cn

    rotten, fresh = 0, 0
    q = deque()

    for r in range(rn):
        for c in range(cn):
            if grid[r][c] == FRESH:
                fresh += 1
            elif grid[r][c] == ROTTEN:
                q.append((r, c))
                rotten += 1
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    time = 0
    while q:
        rotted = False  # this will check if we rot any orange in current layer
        for _ in range(len(q)):
            x, y = q.popleft()
            for dir in directions:
                new_x, new_y = x + dir[0], y + dir[1]
                if inbound(new_x, new_y) and grid[new_x][new_y] == FRESH:
                    grid[new_x][new_y] = ROTTEN
                    rotted = True
                    rotten += 1
                    fresh -= 1
                    q.append((new_x, new_y))
                
        time += 1 if rotted else 0 # we only increment time if we infect any orange in current layer.


    return time if fresh == 0 else -1  # if all orange are rotten, return time, otherwise -1 as there are still fresh oranges in the grid which cannot be rotten by infection as they are isolated from infected oranges from all directions.



orangesRotting(grid1)