
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip().split(" | ") for x in f.readlines()]
    return [[x[0].split(" "), x[1].split(" ")] for x in lines]

class ScreenDigits():
    def __init__(self):
        self.matches = [None for _ in range(10)]
        self.others = []

    def deduct(self):
        for x in self.others:
            c = len(x)
            if c == 5:
                if len(set(self.matches[1]).intersection(set(x))) == 2:
                    self.matches[3] = x
                elif len(set(self.matches[4]).intersection(set(x))) == 2:
                    self.matches[2] = x
                else:
                    self.matches[5] = x
            if c == 6:
                if len(set(self.matches[1]).intersection(set(x))) == 1:
                    self.matches[6] = x
                elif len(set(self.matches[4]).intersection(set(x))) == 4:
                    self.matches[9] = x
                else:
                    self.matches[0] = x


    def add(self, string):
        if len(string) == 2:
            self.matches[1] = string
        elif len(string) == 4:
            self.matches[4] = string
        elif len(string) == 3:
            self.matches[7] = string
        elif len(string) == 7:
            self.matches[8] = string
        else:
            self.others.append(string)

    def result(self, arr):
        self.deduct()
        res = ""
        for a in arr:
            for b in self.matches:
                if self.same(a, b):
                    res += str(self.matches.index(b))
                    break
        return int(res)

    def same(self, a, b):
        if len(a) == len(b) and all([x in b for x in a]):
            return True
        return False

findings = input_file()

tot = 0

for l in findings:
    screen = ScreenDigits()
    for x in l[0]:
        screen.add(x)
    screen.deduct()
    res = screen.result(l[1])
    print(res)
    tot += res

print(tot)
