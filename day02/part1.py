p = 0
for line in open('input').readlines():
    p1, p2 = ord(line[0]) - ord('A'), ord(line[2]) - ord('X')
    if (p1-p2)%3 == 2: p+=p2+7
    elif (p1-p2)%3 == 1: p+=p2+1
    elif (p1-p2) == 0: p+=p2+4
print(p)

