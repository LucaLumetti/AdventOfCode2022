with open('input') as f:
    x = [[eval(b) for b in a.strip().split('\n')] for a in f.read().split('\n\n')]

def compare(a, b):
    # print(f'Compare {a} vs {b}')
    for aa, bb in zip(a, b):
        if type(aa) == int and type(bb) == int:
            if aa == bb: continue
            return bb - aa
        elif type(aa) == list and type(bb) == int:
            bb = [bb]
            c = compare(aa, bb)
            if c == 0: continue
            else: return c
        elif type(bb) == list and type(aa) == int:
            aa = [aa]
            c = compare(aa, bb)
            if c == 0: continue
            else: return c
        elif type(bb) == list and type(aa) == list:
            c = compare(aa, bb)
            if c == 0: continue
            else: return c
    if len(a) < len(b):
        return 1
    elif len(b) < len(a):
        return -1
    return 0
    

total_right = 0
for i,l in enumerate(x):
    right = compare(l[0], l[1])
    if right > 0: total_right += i+1
print(total_right)
