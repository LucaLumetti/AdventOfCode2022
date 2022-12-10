with open('input') as f:
    x = f.read().splitlines()

class CPU:
    def __init__(self,):
        self.X = 1
        self.IP = 0
        self.ops = []
        self.total = 0
        self.CRT = ""

    def addx(self, V):
        self.ops.append(self._noop)
        self.ops.append(lambda: self._addx(V))

    def _addx(self, V):
        self.X += V

    def noop(self,):
        self.ops.append(self._noop)

    def _noop(self,):
        pass

    def step(self,):
        self.IP += 1
        if (self.IP-20)%40==0:
            self.total += self.X*self.IP
        if (self.IP-1)%40 in range(self.X-1, self.X+2):
            self.CRT += '#'
        else:
            self.CRT += '.'
        self.ops.pop(0)()

cpu = CPU()

for i,l in enumerate(x):
    op = l[:4]
    if op == 'addx':
        op, args = l.split(' ')
        args = int(args)
        cpu.addx(args)
    else:
        cpu.noop()
    cpu.step()

while len(cpu.ops) > 0:
    cpu.step()

print(cpu.total)
for i in range(0, len(cpu.CRT), 40):
    print(cpu.CRT[i:i+40])
