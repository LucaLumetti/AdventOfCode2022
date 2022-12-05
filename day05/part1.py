import re
regex = r"[a-z ]+(\d+)[a-z ]+(\d+)[a-z ]+(\d+)"

with open('input') as f:
    cargo, moves = [x.rstrip().split('\n') for x in f.read().split('\n\n')]

cargo = [ c[1::4] for c in cargo if c[1::4] != '']
cargo = [ ''.join([ c[n] for c in cargo[:-1] ])  for n in range(len(cargo[-1])) ]
cargo = [ list(c.strip()[::-1]) for c in cargo ]

for m in moves:
    n, f, t = re.findall(regex, m, re.MULTILINE)[0]
    n, f, t = int(n), int(f)-1, int(t)-1
    cargo[t] += cargo[f][-n:][::-1]
    del cargo[f][-n:]
print(''.join([ c[-1] for c in cargo]))
