with open('input') as f:
    x = [[eval(b) for b in a.strip().split('\n')] for a in f.read().split('\n\n')]

def compare(a, b):
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

def compare2(a, b):
    r = compare(b, a)
    return r

def qsort(input_list, compare_function):
    if len(input_list) < 2:
        return input_list
    else:
        pivot = input_list[0]
        less = [i for i in input_list[1:] if compare_function(i, pivot) < 0]
        greater = [i for i in input_list[1:] if compare_function(i, pivot) > -1]
        return qsort(less, compare_function) + [pivot] + qsort(greater, compare_function)

flat = [[[2]],[[6]]]
for l in x:
    flat.append(l[0])
    flat.append(l[1])
flat = qsort(flat, compare2)

key = 1
for i,ff in enumerate(flat):
    if ff == [[2]]:
        key*=(i+1)
    if ff == [[6]]:
        key*=(i+1)
print(key)
