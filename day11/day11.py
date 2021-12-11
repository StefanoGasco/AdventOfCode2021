

ENV = 'real'
class Dumbo():
    def __init__(self, energy_level, w, h):
        self.energy_level = int(energy_level)
        self.w = w
        self.h = h
        self.max_w = 10
        self.max_h = 10
        self.neighbours = []
        self.flashes = 0

    def add_neighbours(self):
        for h in [self.h - 1, self.h, self.h + 1]:
            for w in [self.w-1, self.w, self.w+1]:
                if (w, h) != (self.w, self.h):
                    self.add_neighbour(w, h)

    def add_neighbour(self, w, h):
        if 0 <= w < self.max_w and 0 <= h < self.max_h:
            dumbo = matrix[h][w]
            self.neighbours.append(dumbo)

    def step(self):
        self.increase_energy()

    def increase_energy(self):
        self.energy_level += 1
        if self.energy_level == 10:
            self.flashes += 1
            self.flash_neighbours()

    def flash_neighbours(self):
        for dumbo in self.neighbours:
            dumbo.step()

    def check_energy_level(self):
        if self.energy_level > 9:
            self.energy_level = 0

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
        res = [list(x) for x in lines]
    return [[Dumbo(e, w, h) for w,e in enumerate(l)] for h,l in enumerate(res)]


matrix = input_file()

for row in matrix:
    for d in row:
        d.add_neighbours()

aligned = False
c = 0
while not aligned:
    c+= 1
    for row in matrix:
        for d in row:
            d.step()
    for row in matrix:
        for d in row:
            d.check_energy_level()
    first = [x.energy_level for x in matrix[0]]
    aligned = all([first == [x.energy_level for x in y] for y in matrix])


print(c)