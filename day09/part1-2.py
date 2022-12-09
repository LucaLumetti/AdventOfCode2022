from math import sqrt, atan2, cos, sin, pi

def move(R, d):
    if d == 'R':
        R[0] += 1
    if d == 'L':
        R[0] -= 1
    if d == 'U':
        R[1] += 1
    if d == 'D':
        R[1] -= 1
    return R

def step(H, T):
    dist = sqrt((H[0]-T[0])**2 + (H[1]-T[1])**2)
    if dist <= sqrt(2): return H, T

    dir = atan2(H[1]-T[1], H[0]-T[0])

    if abs(dir/pi) in [0., 0.5, 1., 1.5, 2.0]:
        T[0] += int((dist-1)*cos(dir))
        T[1] += int((dist-1)*sin(dir))
        return H, T
    T[0] += -1 if H[0]-T[0] < 0 else 1
    T[1] += -1 if H[1]-T[1] < 0 else 1
    return H, T

with open('input') as f:
    moves = [(d, int(n)) for d, n in (line.split(' ') for line in f.read().splitlines())]

R = [[0, 0] for _ in range(10)]
history = [{str(R[1])},{str(R[-1])}]

for m in moves:
    d, n = m

    for _ in range(n):
        R[0] = move(R[0], d)
        for t in range(1, 10):
            R[t-1], R[t] = step(R[t-1], R[t])
        history[0].add(f'{R[1]}')
        history[1].add(f'{R[-1]}')
print(len(history[0]))
print(len(history[1]))

