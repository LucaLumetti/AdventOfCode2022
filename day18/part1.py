with open('input') as f:
    x = [[int(c) for c in l.split(',')] for l in f.read().splitlines()]

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
    n_neigh = sum([1 for n in get_neigh(coords) if n in x])
    count_of_neighs.append(n_neigh)

count_of_neighs = sum([6-x for x in count_of_neighs])
print(count_of_neighs)

