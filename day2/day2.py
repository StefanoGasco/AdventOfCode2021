
class SubmarineDriver():
    def __init__(self):
        self.h_pos = 0
        self.depth = 0
        self.aim = 0

    def forward(self, dist):
        self.h_pos += dist
        self.depth += self.aim * dist

    def down(self, dist):
        self.aim += dist

    def up(self, dist):
        self.aim -= dist

    def position(self):
        return self.h_pos*self.depth

def example_file():
    with open('example_file.txt') as f:
        lines = [x.split(' ') for x in f.readlines()]
    res = [(c,int(d.strip())) for c,d in lines]
    return res

def input_file():
    with open('input_file.txt') as f:
        lines = [x.split(' ') for x in f.readlines()]
    res = [(c,int(d.strip())) for c,d in lines]
    return res

submarine = SubmarineDriver()
for direction, distance in input_file():
    if direction == 'forward':
        submarine.forward(distance)
    elif direction == 'up':
        submarine.up(distance)
    elif direction == 'down':
        submarine.down(distance)
    else:
        pass

print(submarine.position())