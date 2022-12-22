# 146092
import numpy as np
import re

conv = { '.': 0, '#': 1, ' ': 2, }

iconv = { '0': '.', '1': '#', '2': ' ', '3': '>', '4': 'v', '5': '<', '6': '^', }

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
    n_pos = None
    if d == 0:
        n_pos = (pos[0]+1, pos[1], pos[2])
    if d == 2:
        n_pos = (pos[0]-1, pos[1], pos[2])
    if d == 1:
        n_pos = (pos[0], pos[1]+1, pos[2])
    if d == 3:
        n_pos = (pos[0], pos[1]-1, pos[2])
    return (n_pos[0], n_pos[1], d)

with open('input') as f:
    map, dirs = f.read().split('\n\n')
    map = [[conv[c] for c in l] for l in map.splitlines()]
for i in range(len(map)):
    while len(map[i]) < 150:
        map[i].append(2)

map =  np.array(map)
pos = (np.argwhere(map[0]==0).min(), 0, 0) # x, y, d
dirs = re.findall('(\d+[A-Z])', dirs)
dirs = [(int(d[:-1]), d[-1]) for d in dirs]

poses = []
for d in dirs:
    steps = d[0]
    turn = d[1]
    for _ in range(steps):
        poses.append(pos)
        next_pos = move(pos)
        # print_map(map, poses)
        if next_pos[1] >= map.shape[0] or next_pos[0] >= map.shape[1] or next_pos[1] < 0 or next_pos[0] < 0 or map[next_pos[1], next_pos[0]] == 2:
            curr_dir = pos[-1]
            if curr_dir == 0:
                next_pos = (np.argwhere(map[pos[1]]!=2).min(), pos[1], next_pos[2])
                if map[next_pos[1], next_pos[0]] == 1: continue
                pos = next_pos
                continue
            if curr_dir == 2:
                next_pos = (np.argwhere(map[pos[1]]!=2).max(), pos[1], next_pos[2])
                if map[next_pos[1], next_pos[0]] == 1: continue
                pos = next_pos
                continue
            if curr_dir == 1:
                next_pos = (pos[0], np.argwhere(map[:,pos[0]]!=2).min(), next_pos[2])
                if map[next_pos[1], next_pos[0]] == 1: continue
                pos = next_pos
                continue
            if curr_dir == 3:
                next_pos = (pos[0], np.argwhere(map[:,pos[0]]!=2).max(), next_pos[2])
                if map[next_pos[1], next_pos[0]] == 1: continue
                pos = next_pos
                continue
        if map[next_pos[1], next_pos[0]] == 1:
            continue
        if map[next_pos[1], next_pos[0]] == 0:
            pos = next_pos
            continue
    if turn == 'R':
        pos = (pos[0], pos[1], (pos[2]+1)%4)
    if turn == 'L':
        pos = (pos[0], pos[1], (pos[2]-1)%4)
print((pos[0]+1)*4+(pos[1]+1)*1000+((pos[2]-1)%4))
