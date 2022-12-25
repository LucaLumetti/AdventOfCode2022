fuels =     { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
decimals =  { -2: '=', -1: '-', 0: '0', 1: '1', 2: '2' }

def b5tob10(n):
    return sum([(5 ** i) * fuels[c] for i, c in enumerate(n[::-1])])

def b10tob5(n):
    result = []
    while n > 0:
        r = n % 5
        if r > 2:
            n += r
            digit = decimals[r-5]
        else:
            digit = str(r)
        result.insert(0, digit)
        n //= 5
    return ''.join(result)

print(b10tob5(sum([b5tob10(l) for l in open('input').read().splitlines()])))
