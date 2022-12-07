class AoCsh:
    def __init__(self):
        self.root = TreeFS(None, '/', 'dir')
        self.current = self.root

    def flatten(self, dir, p2):
        p2.append(dir)
        for c in dir.children:
            self.flatten(c, p2)

    def walk(self, dir, depth=0):
        for c in dir.children:
            if c.ftype == 'dir':
                print(f"{' '*depth}{c.ftype} - {c.name}")
                self.walk(c, depth+1)
            else:
                print(f"{' '*depth}{c.ftype} - {c.name}")

    def mk(self, name, ftype):
        self.current.add_file(self.current, name, ftype)

    def cd(self, dirname):
        if dirname == '/':
            self.current = self.root
        elif dirname == '..':
            self.current = self.current.parent
        else:
            for d in self.current.children:
                if d.name != dirname: continue
                self.parent = self.current
                self.current = d
                break

class TreeFS:
    def __init__(self, parent, name, ftype):
        self.name: str = name
        self.children: list = []
        self.ftype = ftype
        self.parent: TreeFS = parent
        self.size: int = -1

    def get_size(self,) -> int:
        if self.size == -1:
            self.compute_size()
        return self.size

    def compute_size(self,) -> None:
        if type(self.ftype) == int:
            self.size = self.ftype
        else:
            self.size = sum([c.get_size() for c in self.children])

    def add_file(self, parent, name, ftype) -> None:
        if ftype != 'dir':
            ftype = int(ftype)
        self.children.append(TreeFS(parent, name, ftype))

#######################

with open('input') as f:
    lines = f.readlines()

sh = AoCsh()

while len(lines) > 0:
    l = lines.pop(0).strip()
    cmd = l.split(' ')
    if cmd[1] == 'cd':
        sh.cd(cmd[2])
    elif cmd[1] == 'ls':
        while lines and lines[0][0] != '$':
            l = lines.pop(0).rstrip().split(' ')
            ftype, name = l
            sh.mk(name, ftype)

sh.root.compute_size()

# part 1
p1 = []
sh.flatten(sh.root, p1)
print(sum([c.get_size() for c in p1 if c.get_size() <= 100000 and c.ftype == 'dir']))

# part 2
required_space = 30000000 - (70000000 - sh.root.get_size())
p2 = []
sh.flatten(sh.root, p2)
p2 = min([c.get_size() for c in p2 if c.get_size() >= required_space and c.ftype == 'dir'])
print(p2)
