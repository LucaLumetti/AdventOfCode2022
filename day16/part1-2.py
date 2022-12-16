from collections import defaultdict
import functools
import re

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

valves = set()
flows = dict()
D = defaultdict(lambda: float('inf'))

for valve, flow, conns in re.findall(r, open('input').read()):
    flow = int(flow)
    valves.add(valve)
    if flow != 0: flows[valve] = flow
    for u in conns.split(', '):
        D[u,valve] = 1

for i in valves:
    for j in valves:
        for k in valves:
            D[j,k] = min(D[j,k], D[j,i] + D[i,k])

@functools.cache
def search(time_left, actual_valve='AA', vf=frozenset(flows), e=False):
    solutions = [0]
    for v in vf:
        if D[actual_valve, v] > time_left: continue
        remaining_time = time_left - D[actual_valve, v] - 1
        partial_sol = flows[v] * remaining_time
        partial_sol += search(remaining_time, v, vf-{v}, e)
        solutions.append(partial_sol)
    if e:
        solutions += [search(26, vf=vf)]
    return max(solutions)

print(search(30))
print(search(26, e=True))
