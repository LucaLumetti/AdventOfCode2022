with open('input') as f:
    x = f.readlines()

total = 0
for line in x:
    length = len(line)
    common = (set(line[:length//2]) & set(line[length//2:])).pop()
    total += 27 if common.isupper()  else 1
    total += ord(common.lower()) - ord('a')
print(total)

