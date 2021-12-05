
ENV = 'real'


def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    res = []
    for coord in lines:
        res.append([list(map(int, x.split(","))) for x in coord.split(" -> ")])
    return res

class Scanner():
    def __init__(self, array):
        self.findings = {}
        self.array = array

    def scanner(self):
        for coords in self.array:
            line = self.draw_line(coords)
            for x in line:
                self.findings[x] = self.findings.get(x, 0) + 1

    def draw_line(self, coords):
        step_x = 1 if coords[0][0] < coords[1][0] else -1
        step_y = 1 if coords[0][1] < coords[1][1] else -1
        range_x = range(coords[0][0], coords[1][0] + step_x, step_x)
        range_y = range(coords[0][1], coords[1][1] + step_y, step_y)

        if (coords[0][0] == coords[1][0]) or (coords[0][1] == coords[1][1]):
            func = self.draw_straight
        else:
            func = self.draw_diagonal
        for x in func(range_x, range_y):
            yield x


    def draw_diagonal(self, range_x, range_y):

        for i,x in enumerate(range_x):
            y = range_y[i]
            yield f"{x},{y}"

    def draw_straight(self, range_x, range_y):
        for x in range_x:
            for y in range_y:
                yield f"{x},{y}"

    def hot_spots(self):
        self.scanner()
        count = 0
        for x in self.findings.values():
            if x >= 2:
                count += 1
        return count

a = Scanner(input_file())
print(a.hot_spots())