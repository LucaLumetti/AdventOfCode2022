import re

with open('input') as f:
    x = [l.split(': ') for l in f.read().splitlines()]

def replace_all(mop, who, what):
    for k in mop.keys():
        if type(mop[k]) != str: continue
        mop[k] = mop[k].replace(who, f'({what})')
    return mop

mop = dict()
for monkey, op in x:
    mop[monkey] = op

for k in mop.keys():
    try:
        mop[k] = int(mop[k])
    except:
        continue

while type(mop['root']) == str:
    k_to_del = []
    for k in mop.keys():
        if type(mop[k]) == str: continue
        if k == 'root': continue
        mop = replace_all(mop, k, mop[k])
        k_to_del.append(k)
    for k in k_to_del: del mop[k]
    for k in mop.keys():
        if re.search(r'[a-z]{4}', mop[k]): continue
        mop[k] = int(eval(mop[k]))

print(mop['root'])
