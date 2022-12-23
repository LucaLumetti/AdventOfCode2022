import numpy as np

with open('input') as f:
    x = f.read().splitlines()

def indexall(ar, el):
    return [i for i, x in enumerate(ar) if x == el]

def print_forest(forest):
    s = ''
    for l in forest:
        for c in l:
            s += '#' if c == 1 else '.'
        s += '\n'
    print(s)

w, h = len(x[0]), len(x)

forest = np.zeros((h, w))

for i,l in enumerate(x):
    for j,c in enumerate(l):
        if c == '#':
            forest[i, j] = 1
def check_if_border(f):
    return f[0,:].sum() + f[-1,:].sum() + f[:,0].sum() + f[:,-1].sum()

forest = np.pad(forest, 1)

idk = 0
while True:
    elfs_proposal = []
    elfs_pos = np.vstack(np.where(forest==1)).T
    forest_update = np.zeros_like(forest)
    for p in elfs_pos:
        moved = False
        where_to_move = None
        if forest[p[0]-1:p[0]+2,p[1]-1:p[1]+2].sum() == 1:
            elfs_proposal.append(None)
            continue

        for i in range(idk, idk+4):
            if forest[p[0]-1, p[1]-1:p[1]+2].sum() == 0 and i%4==0:
                elfs_proposal.append([p[0]-1, p[1]])
                moved = True
                break
            elif forest[p[0]+1, p[1]-1:p[1]+2].sum() == 0 and i%4==1:
                elfs_proposal.append([p[0]+1, p[1]])
                moved = True
                break
            elif forest[p[0]-1:p[0]+2, p[1]-1].sum() == 0 and i%4==2:
                elfs_proposal.append([p[0], p[1]-1])
                moved = True
                break
            elif forest[p[0]-1:p[0]+2, p[1]+1].sum() == 0 and i%4==3:
                elfs_proposal.append([p[0], p[1]+1])
                moved = True
                break
        if not moved:
            elfs_proposal.append(None)

    moved = False
    for i in range(len(elfs_proposal)):
        if elfs_proposal[i] is None: continue
        moved = True
        idxs = indexall(elfs_proposal, elfs_proposal[i])
        if len(idxs) > 1:
            for idx in idxs: elfs_proposal[idx] = None
    if moved is False: break
    for i,pos in enumerate(elfs_proposal):
        if pos is None:
            pos = elfs_pos[i]
        forest_update[pos[0], pos[1]] = 1
    forest = forest_update

    idk = (idk+1)
    if check_if_border(forest):
        forest = np.pad(forest_update, 1)
print(idk+1)
