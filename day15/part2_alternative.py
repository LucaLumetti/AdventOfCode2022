import re

def intersect(l1, l2):
    x = (l2[1]-l1[1])/(l1[0]-l2[0])
    y = l1[0]*x+l1[1]
    return (x, y)

def get_line(x1, y1, x2, y2):
        m = (y2-y1)/(x2-x1)
        c = y1 - m*x1
        return m, c

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def overlap(a, b):
    return not (a[1] < b[0] or a[0] > b[1])

def combine_ranges(ranges):
    new_ranges = []
    r0 = ranges.pop(0)
    while len(ranges) > 1:
        r1 = ranges.pop(0)
        was_consumed = False
        while overlap(r0, r1):
            r0 = min(r0[0], r1[0]), max(r0[1], r1[1])
            if ranges:
                r1 = ranges.pop(0)
            else:
                break
            was_consumed = True
        new_ranges.append(r0)
        if was_consumed:
            if ranges:
                r0 = ranges.pop(0)
        else:
            r0 = r1
    return new_ranges


lines = set()
sensors_beacon = {}

with open('test') as f:
    for line in f:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        sensor = (sx, sy)
        beacon = (bx, by)
        sensors_beacon[sensor] = beacon
        r = dist(sensor, beacon)+1
        lines.add(get_line(sx+r, sy, sx, sy+r))
        lines.add(get_line(sx-r, sy, sx, sy-r))
        lines.add(get_line(sx-r, sy, sx, sy+r))
        lines.add(get_line(sx+r, sy, sx, sy-r))

lines = list(lines)
poslines = [line for line in lines if line[0] > 0]
neglines = [line for line in lines if line[0] < 0]

intersections = []
for p in poslines:
    for n in neglines:
        intersections.append(intersect(p, n))
print((14, 11) in intersections)
for inter in intersections:
    closer_sensor = {'d': None, 's': None}
    for s in sensors_beacon.keys():
        d = dist(s,inter)
        if closer_sensor['d'] is None or closer_sensor['d'] > d:
            closer_sensor['d'] = d
            closer_sensor['s'] = s
    b = sensors_beacon[closer_sensor['s']]
    print(dist(b, closer_sensor['s']), dist(closer_sensor['s'], inter))
    if dist(b, closer_sensor['s']) < dist(closer_sensor['s'], inter):
        print(inter)
