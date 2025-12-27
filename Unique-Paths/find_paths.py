def find_all_paths(m, n):
    all_paths = []
    path = []
    def dfs(r, c):
        if r == m or c == n: #out of bound, we don't add >= since increment is by 1 each time so we will not go beyond m and n
            return

        path.append((r, c))

        if r == m - 1 and c == n - 1: #reached end cell, store path
            all_paths.append(path[:])
            path.pop()
            return
        
        dfs(r+1, c)
        dfs(r, c+1)

        path.pop()

    dfs(0, 0)
    return all_paths

paths = find_all_paths(3, 3)
# print(f'{len(paths)} paths')
print(paths)