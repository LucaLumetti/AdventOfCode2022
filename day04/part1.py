import re

with open('input') as f:
    x = f.readlines()

n = 0
regex = r"(\d+)\-(\d+),(\d+)-(\d+)"
for line in x:
    m = re.findall(regex, line, re.MULTILINE)
    m = [int(a) for a in m[0]]
    n += (m[0] <= m[2] and m[1] >= m[3]) or (m[0] >= m[2] and m[1] <= m[3])
print(n)
