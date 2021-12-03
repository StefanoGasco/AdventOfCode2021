
ENV = 'real'


class BinaryDiagnostic():
    def __init__(self, in_file):
        self.in_file = in_file
        self.size = len(in_file)
        self.counter = [0 for _ in in_file[0]]
        self.parse_file()

    def add_counters(self, num):
        for i,x in enumerate(num):
            self.counter[i] += int(x)

    def parse_file(self):
        for x in self.in_file:
            self.add_counters(x)

    def generate_rates(self):
        gamma_rate = ""
        epsilon_rate = ""
        for x in self.counter:
            if x > self.size/2:
                gamma_rate += "1"
                epsilon_rate += "0"
            else:
                gamma_rate += "0"
                epsilon_rate += "1"
        return int(gamma_rate, 2), int(epsilon_rate, 2)

    def consumption(self):
        gamma_rate, epsilon_rate = self.generate_rates()
        return gamma_rate*epsilon_rate





def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

bin_diag = BinaryDiagnostic(input_file())
print(bin_diag.consumption())