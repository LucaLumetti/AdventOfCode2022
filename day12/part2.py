with open('input') as f:
    x = [[ord(c)-ord('a') for c in list(l)] for l in f.read().splitlines()]

def find_shortest_path(matrix, S, E):
    H = len(matrix)
    W = len(matrix[0])
    visited = [[False for _ in range(W)] for _ in range(H)]
    path = [[0 for _ in range(W)] for _ in range(H)]
    q = []
    q.append(S)
    visited[S[0]][S[1]] = True
    while q:
        i, j = q.pop(0)
        if (i, j) == E:
            return path[i][j]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if visited[ni][nj]:
                continue
            if matrix[ni][nj] -matrix[i][j] > 1:
                continue
            path[ni][nj] = path[i][j] + 1
            visited[ni][nj] = True
            q.append((ni, nj))
    return -1

S = []
E = None
for i,l in enumerate(x):
    for j,c in enumerate(l):
        if c == ord('S')-ord('a'):
            x[i][j] = 0
            S.append((i, j))
        elif c == 0:
            S.append((i, j))
        elif c == ord('E')-ord('a'):
            x[i][j] = ord('z')-ord('a')
            E = (i, j)

min_p = float('+inf')
for s in S:
    p = find_shortest_path(x, s, E)
    if p == -1: continue
    if p < min_p:
        min_p = p
print(min_p)
