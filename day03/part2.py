with open('input') as f:
    x = [ l.strip() for l in f.readlines()]

total = 0
for i in range(len(x)//3):
    common = (set(x[3*i+0]) & set(x[3*i+1]) & set(x[3*i+2])).pop()
    total += 27 if common.isupper() else 1
    total += ord(common.lower()) - ord('a')
print(total)

