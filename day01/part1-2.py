with open('input', 'r') as f:
    x = f.read().split('\n\n')
x = sorted([sum([int(a) for a in elf.strip().split('\n')]) for elf in x])
print(x[-1])
print(sum(x[-3:]))

