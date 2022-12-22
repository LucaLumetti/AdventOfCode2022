import numpy as np
import re

conv = { '.': 0, '#': 1, ' ': 2, }
iconv = {'0': '.','1': '#', '2': ' ', '3': '\033[91m>\033[0m', '4': '\033[91mv\033[0m', '5': '\033[91m<\033[0m', '6': '\033[91m^\033[0m'}

def jump(pos):
    x, y, d = pos
    if x == 50 and y in range(0, 50) and d == 2:
        return (0, 149-y, 0)
    if x == 50 and y in range(50, 100) and d == 2:
        return (y-50+0, 100, 1)
    if x == 0 and y in range(100, 150) and d == 2:
        return (50, 49-(y-100), 0)
    if x == 0 and y in range(150, 200) and d == 2:
        return (y-150+50, 0, 1)
    if x == 149 and y in range(0, 50) and d == 0:
        return (99, 149-y, 2)
    if x == 99 and y in range(50, 100) and d == 0:
        return (y-50+100, 49, 3)
    if x == 99 and y in range(100, 150) and d == 0:
        return (149, 49-(y-100), 2)
    if x == 49 and y in range(150, 200) and d == 0:
        return (49+(y-150), 149, 3)
    if y == 100 and x in range(0, 50) and d == 3:
        return (50, x-0+50, 0)
    if y == 0 and x in range(50, 100) and d == 3:
        return (0, x-50+150, 0)
    if y == 0 and x in range(100, 150) and d == 3:
        return (x-100+0, 199, 3)
    if y == 199 and x in range(0, 50) and d == 1:
        return (x+100, 49, 1)
    if y == 149 and x in range(50, 100) and d == 1:
        return (49, x-50+149, 2)
    if y == 49 and x in range(100, 150) and d == 1:
        return (99, x-100+50, 2)
    assert False, f'ERROR {pos}'

def print_map(arr, poses):
    arr = arr.copy()
    for pos in poses:
        arr[pos[1], pos[0]] = 3+pos[-1]
    s = ''
    for l in arr:
        for c in l:
            s += iconv[str(c)]
        s += '\n'
    print(s)


def move(pos):
    d = pos[-1]
    if d == 0:
        return (pos[0]+1, pos[1], pos[2])
    elif d == 2:
        return (pos[0]-1, pos[1], pos[2])
    elif d == 1:
        return (pos[0], pos[1]+1, pos[2])
    return (pos[0], pos[1]-1, pos[2])

with open('input') as f:
    map, dirs = f.read().split('\n\n')
    map = [[conv[c] for c in l] for l in map.splitlines()]

for i in range(len(map)):
    while len(map[i]) < 150:
        map[i].append(2)

map =  np.array(map)
pos = (np.argwhere(map[0]==0).min(), 0, 0) # x, y, d
dirs = re.findall(r'(\d+[A-Z])', dirs)
dirs = [(int(d[:-1]), d[-1]) for d in dirs]

poses = []
for d in dirs:
    steps = d[0]
    turn = d[1]
    for _ in range(steps):
        # print_map(map, poses)
        poses.append(pos)
        next_pos = move(pos)
        if next_pos[1] >= map.shape[0]\
            or next_pos[0] >= map.shape[1]\
            or next_pos[1] < 0\
            or next_pos[0] < 0\
            or map[next_pos[1], next_pos[0]] == 2:
            next_pos = jump(pos)
        if map[next_pos[1], next_pos[0]] == 1:
            continue
        elif map[next_pos[1], next_pos[0]] == 0:
            pos = next_pos
    if turn == 'R':
        pos = (pos[0], pos[1], (pos[2]+1)%4)
    if turn == 'L':
        pos = (pos[0], pos[1], (pos[2]-1)%4)
print((pos[0]+1)*4+(pos[1]+1)*1000+((pos[2]-1)%4))
