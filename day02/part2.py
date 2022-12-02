p = 0
for line in open('input').readlines():
    p1, p2 = ord(line[0]) - ord('A'), ord(line[2]) - ord('X')
    if p2 == 2: p += (p1+1)%3+7
    elif p2 == 1: p += p1+4
    elif p2 == 0: p += (p1+2)%3+1
print(p)

