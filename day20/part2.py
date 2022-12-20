from collections import deque

x = list(map(lambda x: int(x)*811589153, open('input').read().splitlines()))
l = len(x)
v_i = deque([(v, i) for i, v in enumerate(x)])

for _ in range(10):
    for i,n in enumerate(x):
        idx = v_i.index((n, i))
        v_i.remove((n, i))
        v_i.insert((idx+n)%(l-1), (n, i))

s = [vi[0] for vi in v_i]
zero = s.index(0)
print(s[(zero+1000) % l]+s[(zero+2000) % l]+s[(zero+3000) % l])
