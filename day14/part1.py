import numpy as np
with open('input') as f:
    coords = [l.split(' -> ') for l in f.read().splitlines()]

def sign(a):
    if a < 0: return -1
    if a > 0: return 1
    return 0

def getMap(map, x, y):
    key = f'{x},{y}'
    if key in map:
        return map[key]
    else:
        return None

map = {'500,0':3}
MAX_Y = 0
for coord in coords:
    starting_pos = None
    for c in coord:
        x, y = c.split(',')
        x, y = int(x), int(y)
        if y > MAX_Y: MAX_Y = y
        if starting_pos is None:
            starting_pos = [x, y]
            map[f'{starting_pos[0]},{starting_pos[1]}'] = 2

        while starting_pos[0] != x or starting_pos[1] != y:
            starting_pos[0] -= sign(starting_pos[0]-x)
            starting_pos[1] -= sign(starting_pos[1]-y)
            map[f'{starting_pos[0]},{starting_pos[1]}'] = 2

falled = 0
while True:
    moving_sand = [500, 0]
    falled += 1
    while True:
        if moving_sand[1] > MAX_Y:
            print(falled-1)
            exit(0)
        if getMap(map, moving_sand[0], moving_sand[1]+1) is None:
            moving_sand[1] += 1
            continue
        elif getMap(map, moving_sand[0]-1, moving_sand[1]+1) is None:
            moving_sand[0] -= 1
            moving_sand[1] += 1
            continue
        elif getMap(map, moving_sand[0]+1, moving_sand[1]+1) is None:
            moving_sand[0] += 1
            moving_sand[1] += 1
            continue
        map[f'{moving_sand[0]},{moving_sand[1]}'] = 1
        break
