with open('input') as f:
    x = f.read().strip()

for i in range(14,len(x)):
    if len(set(x[i-14:i])) == 14:
        print(i)
        break

