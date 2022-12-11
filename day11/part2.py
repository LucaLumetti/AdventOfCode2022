ops = [
    lambda x: x*11,
    lambda x: x+4,
    lambda x: x**2,
    lambda x: x+2,
    lambda x: x+3,
    lambda x: x+1,
    lambda x: x+5,
    lambda x: x*19,
]
starting_items = [
    [63, 84, 80, 83, 84, 53, 88, 72],
    [67, 56, 92, 88, 84],
    [52],
    [59, 53, 60, 92, 69, 72],
    [61, 52, 55, 61],
    [79, 53],
    [59, 86, 67, 95, 92, 77, 91],
    [58, 83, 89],
]
tests = [
        lambda x: 7 if x%13 else 4,
        lambda x: 3 if x%11 else 5,
        lambda x: 1 if x%2 else 3,
        lambda x: 6 if x%5 else 5,
        lambda x: 2 if x%7 else 7,
        lambda x: 6 if x%3 else 0,
        lambda x: 0 if x%19 else 4,
        lambda x: 1 if x%17 else 2,
        ]
LCM = 13*11*2*5*7*3*19*17

class Monkey:
    def __init__(self, starting_items, operation, test):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspected_items = 0

    def act(self,):
        throws = []
        for item in self.items:
            self.inspected_items += 1
            val = self.operation(item)%LCM
            throws.append((val, self.test(val)))
        self.items = []
        return throws

monkeys = [Monkey(s_item, op, test) for s_item, op, test in zip(starting_items, ops, tests)]
for _ in range(10_000):
    for monkey in monkeys:
        for worry, m in monkey.act(): monkeys[m].items.append(worry)
monkeys = [m.inspected_items for m in monkeys]
monkeys.sort()
print(monkeys[-2]*monkeys[-1])
