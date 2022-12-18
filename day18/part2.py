import numpy as np
import fill_voids

with open('input') as f:
    x = [[int(c) for c in l.split(',')] for l in f.read().splitlines()]


coords = np.array(x)
max_x, max_y, max_z = coords[:,0].max(), coords[:,1].max(), coords[:,2].max()

grid = np.zeros((max_x+1, max_y+1, max_z+1))
for pos in coords:
    grid[pos[0],pos[1],pos[2]] = 1

filled_image = fill_voids.fill(grid, in_place=False)

x = np.vstack((np.where(filled_image==1))).T
x = [list(a) for a in x]

def get_neigh(pos):
    n = []
    n.append([pos[0]+1, pos[1], pos[2]])
    n.append([pos[0], pos[1]+1, pos[2]])
    n.append([pos[0], pos[1], pos[2]+1])
    n.append([pos[0]-1, pos[1], pos[2]])
    n.append([pos[0], pos[1]-1, pos[2]])
    n.append([pos[0], pos[1], pos[2]-1])
    n = [ a for a in n if not(a[0] < 0 or a[1] < 0 or a[2] < 0)]
    return n

count_of_neighs = []
for coords in x:
    neighs = get_neigh(coords)
    n_neigh = sum([1 for n in neighs if n in x])
    count_of_neighs.append(n_neigh)

count_of_neighs = sum([6-x for x in count_of_neighs])
print(count_of_neighs)

