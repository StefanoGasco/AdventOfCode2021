

class School():
    def __init__(self, school):
        self.school = school
        self.count = len(self.school)
        self.deliveries = {}
        for x in range(9):
            self.deliveries[x] = self.school.count(x)

    def day_pass(self):
        restart = self.deliveries[0]
        for x in range(1, 9):
            self.deliveries[x-1] = self.deliveries[x]
        self.deliveries[6] += restart
        self.deliveries[8] = restart
        self.count += restart




ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    return [int(x) for x in lines[0].split(",")]

a = School(input_file())
for _ in range(256):
    a.day_pass()
print(a.count)
