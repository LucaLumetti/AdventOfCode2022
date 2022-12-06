with open('input') as f:
    x = f.read().strip()

for i in range(4,len(x)):
    if len(set(x[i-4:i])) == 4:
        print(i)
        break

