
ENV = 'real'


def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    res = []
    for coord in lines:
        res.append([list(map(int, x.split(","))) for x in coord.split(" -> ")])
    return res


def filter(array):
    filtered = []
    for coords in array:
        if (coords[0][0] == coords[1][0]) or (coords[0][1] == coords[1][1]):
            filtered.append(coords)
    return filtered

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
        lower_x = min(coords[0][0], coords[1][0])
        higher_x = max(coords[0][0], coords[1][0])+1
        for x in range(lower_x, higher_x):
            lower_y = min(coords[0][1], coords[1][1])
            higher_y = max(coords[0][1], coords[1][1]) + 1
            for y in range(lower_y, higher_y):
                yield f"{x},{y}"

    def hot_spots(self):
        self.scanner()
        count = 0
        for x in self.findings.values():
            if x >= 2:
                count += 1
        return count

filtered_array = filter(input_file())
print(filtered_array)
a = Scanner(filtered_array)
print(a.hot_spots())
print(list(a.findings.values()).count(4))