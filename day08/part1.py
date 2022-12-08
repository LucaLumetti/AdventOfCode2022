import numpy as np
with open('input') as f:
    m = [ [int(a) for a in list(l)] for l in f.read().splitlines()]

def is_visible(m, x, y):
    visible = True
    for i in range(0, x):
        if m[x][y] > m[i][y]: continue
        visible = False
        break

    if visible: return True
    visible = True

    for i in range(x+1, len(m)):
        if m[x][y] > m[i][y]: continue
        visible = False
        break

    if visible: return True
    visible = True

    for j in range(0, y):
        if m[x][y] > m[x][j]: continue
        visible = False
        break

    if visible: return True
    visible = True

    for j in range(y+1, len(m[0])):
        if m[x][y] > m[x][j]: continue
        visible = False
        break

    if visible: return True
    return False

for x in range(len(m)):
    for y in range(len(m[0])):
        if is_visible(m, x, y) == False:
            m[x][y] = -1

m = np.array(m)
print(m.size - (m==-1).sum())

