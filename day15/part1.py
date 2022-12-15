import re

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


sensor_beacons = set()
beacons = set()
with open('input') as f:
    for line in f:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        sensor = (sx, sy)
        beacon = (bx, by)
        sensor_beacons.add((sensor, beacon))
        beacons.add(beacon)

# test
if (-2, 15) in beacons:
    row = 10
else:
    row = 2000000

ranges = []

for sensor, beacon in sensor_beacons:
    m_dist = dist(sensor, beacon)
    dist_to_row = abs(row - sensor[1])
    if m_dist >= dist_to_row:
        offset = abs(m_dist - dist_to_row)
        cov_along_row = (sensor[0] - offset, sensor[0] + offset)
        ranges.append(cov_along_row)
        ranges = sorted(ranges, key=lambda r: r[0])

ranges = combine_ranges(ranges)

count = 0
for r in ranges:
    count += r[1] + 1 - r[0]
count -= len([beacon for beacon in beacons if beacon[1] == row])
print(count)
