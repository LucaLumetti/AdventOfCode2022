import numpy as np
with open('input') as f:
    m = [ [int(a) for a in list(l)] for l in f.read().splitlines()]


def is_visible(m, x, y):
    total = 1
    visible = 0
    for i in list(range(0, x))[::-1]:
        visible += 1
        if m[x][y] > m[i][y]:
            continue
        break
    total *= visible

    visible = 0

    for i in range(x+1, len(m)):
        visible += 1
        if m[x][y] > m[i][y]:
            continue
        break
    total *= visible

    visible = 0

    for j in list(range(0, y))[::-1]:
        visible += 1
        if m[x][y] > m[x][j]:
            continue
        break
    total *= visible
    visible = 0

    for j in range(y+1, len(m[0])):
        visible += 1
        if m[x][y] > m[x][j]:
            continue
        break

    return total * visible

v = np.zeros_like(np.array(m))
for x in range(len(m)):
    for y in range(len(m[0])):
        v[x,y] = is_visible(m, x, y);

print(v.max())

