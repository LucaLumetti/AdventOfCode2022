import re
from z3 import z3, Int, Abs

sensors = []
with open('input') as f:
    for line in f:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        sensors.append((sx,sy,bx,by))

s = z3.Solver()
x, y = Int('x'), Int('y')
s.add(x >= 0, x <= 4000000)
s.add(y >= 0, y <= 4000000)
for sx, sy, bx, by in sensors:
    d = abs(sx-bx) + abs(sy-by)
    s.add(Abs(sx-x) + Abs(sy-y) > d)
s.check()
m = s.model()
print(m[x].as_long()*4000000 + m[y].as_long())
