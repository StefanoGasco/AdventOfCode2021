

class LanternFish():
    def __init__(self, days):
        self.days = days

    def __repr__(self):
        return str(self.days)

    def day_pass(self):
        self.days -= 1
        if self.days < 0:
            self.days = 6
            return True
        return False

ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    return [int(x) for x in lines[0].split(",")]

school = [LanternFish(x) for x in input_file()]

for _ in range(80):
    for i in range(len(school)):
        if school[i].day_pass():
            school.append(LanternFish(8))

print(len(school))
