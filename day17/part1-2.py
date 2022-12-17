from math import pi
import numpy as np
from matplotlib import pyplot as plt

DEBUG=0
def print_tower(tower):
    s = '_________\n'
    for line in tower:
        if line.sum() == 0:continue
        s += '|'
        for c in line:
            if c==1: s += '#'
            elif c==2: s += '@'
            elif c==0: s += '.'
        s += '|\n'
    s='\n'.join(s.split('\n')[::-1])
    s+='\n'
    print(s)

TILES = [
        np.array([[1,1,1,1]]),
        np.array([[0,1,0],
                  [1,1,1],
                  [0,1,0]]),
        np.array([[1,1,1],
                  [0,0,1],
                  [0,0,1]]),
        np.array([[1],
                  [1],
                  [1],
                  [1]]),
        np.array([[1,1],
                  [1,1]]),
        ]

with open('input') as f:
    winds = f.read().strip()

HEIGHTS = [0]
tower = np.zeros((7,7))
tile_index = 0
wind_index = 0
ITERATIONS = 4000
for i in range(ITERATIONS):
    height = np.argwhere(tower>0)
    if height.shape[0]==0:
        height = 0
    else:
        height = height[:,0].max()+1
    if DEBUG:
        print(f'HEIGHT: {height}')

    tile = TILES[i%len(TILES)].copy()
    tile_pos = [height+3, 2]
    while True:
        if DEBUG:
            tower[tile_pos[0]:tile_pos[0]+tile.shape[0], tile_pos[1]:tile_pos[1]+tile.shape[1]] += tile
            print_tower(tower)
            tower[tile_pos[0]:tile_pos[0]+tile.shape[0], tile_pos[1]:tile_pos[1]+tile.shape[1]] -= tile

        # h movement
        wind = winds[wind_index%len(winds)]
        wind_index += 1
        if DEBUG:
            print(f'{wind_index}:{len(winds)} - {wind}')
        sy = tile_pos[0]
        ey = tile_pos[0]+tile.shape[0]
        sx = tile_pos[1]
        ex = tile_pos[1]+tile.shape[1]
        if wind == '<' and tile_pos[1] > 0 and ((tower[sy:ey,sx-1:ex-1] + tile)>2).sum() == 0:
            tile_pos[1] -= 1
        elif wind == '>' and tile_pos[1]+tile.shape[1] < 7 and ((tower[sy:ey,sx+1:ex+1] + tile)>2).sum() == 0:
            tile_pos[1] += 1

        if DEBUG:
            tower[tile_pos[0]:tile_pos[0]+tile.shape[0], tile_pos[1]:tile_pos[1]+tile.shape[1]] += tile
            print_tower(tower)
            tower[tile_pos[0]:tile_pos[0]+tile.shape[0], tile_pos[1]:tile_pos[1]+tile.shape[1]] -= tile

        # v movement
        sy = tile_pos[0]
        ey = tile_pos[0]+tile.shape[0]
        sx = tile_pos[1]
        ex = tile_pos[1]+tile.shape[1]
        if sy == 0: break
        if ((tower[sy-1:ey-1,sx:ex] + tile)>2).sum() != 0: break
        tile_pos[0] -= 1
    tile[tile==1] = 2
    tower[tile_pos[0]:tile_pos[0]+tile.shape[0], tile_pos[1]:tile_pos[1]+tile.shape[1]] += tile
    tower = np.vstack((tower, np.zeros((3,7))))
    HEIGHTS.append(np.argwhere(tower>1)[:,0].max()+1)

    tile_index += 1

print(HEIGHTS[2022])

# Do it by hand
h = np.argwhere(tower>1)[:,0].max()+1
m = h/ITERATIONS
n = len(HEIGHTS)
a, b = np.polyfit(list(range(len(HEIGHTS))), HEIGHTS, 1)
plt.plot(list(range(len(HEIGHTS))), HEIGHTS)
plt.plot(list(range(len(HEIGHTS))), [a*i+b for i in range(len(HEIGHTS))])
plt.plot(list(range(len(HEIGHTS))), [a*i+b-h for i,h in enumerate(HEIGHTS)])
plt.show()
