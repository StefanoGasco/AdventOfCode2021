
ENV = 'real'

class GasNode():
    def __init__(self, value):
        self.value = value
        self.counter = 1
        self.leaves = []

    def __repr__(self):
        return f"Value: {self.value}, counter: {self.counter}, leaves: {self.leaves[0].value, self.leaves[0].counter,self.leaves[1].value, self.leaves[1].counter}"

    def add_leaf(self, n):
        for x in self.leaves:
            if x.value == n:
                x.counter += 1
                return x
        new_leaf = GasNode(n)
        self.leaves.append(new_leaf)
        return new_leaf

    def find_gas(self, gas):
        if not self.leaves:
            return self.value
        if len(self.leaves) == 1:
            return self.value + self.leaves[0].find_gas(gas)
        if self.leaves[0].counter > self.leaves[1].counter:
            to_return = self.leaves[0] if gas == 'oxygen' else self.leaves[1]
            return self.value + to_return.find_gas(gas)
        elif self.leaves[1].counter > self.leaves[0].counter:
            to_return = self.leaves[1] if gas == 'oxygen' else self.leaves[0]
            return self.value + to_return.find_gas(gas)
        else:
            base = "1" if gas == 'oxygen' else "0"
            return self.value + [branch.find_gas(gas) for branch in self.leaves if branch.value == base][0]



def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def calculate_ratings():

    root = GasNode("")

    for x in input_file():
        branch = root
        for c in x:
            branch = branch.add_leaf(c)

    return int(root.find_gas('oxygen'), 2)*int(root.find_gas('co2'), 2)

print(calculate_ratings())