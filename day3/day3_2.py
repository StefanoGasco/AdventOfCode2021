
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


def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def find_oxygen(root):
    result = ""
    branch = root
    while True:
        if not branch.leaves:
            return result
        if len(branch.leaves) == 1:
            branch = branch.leaves[0]
            continue
        if branch.leaves[0].counter > branch.leaves[1].counter:
            branch = branch.leaves[0]
        elif branch.leaves[1].counter > branch.leaves[0].counter:
            branch = branch.leaves[1]
        else:
            if branch.leaves[0].value == "1":
                branch = branch.leaves[0]
            else:
                branch = branch.leaves[1]
        result += branch.value
    return result

def find_co2(root):
    result = ""
    branch = root
    while True:
        if not branch.leaves:
            return result
        if len(branch.leaves) == 1:
            branch = branch.leaves[0]
        elif branch.leaves[0].counter < branch.leaves[1].counter:
            branch = branch.leaves[0]
        elif branch.leaves[1].counter < branch.leaves[0].counter:
            branch = branch.leaves[1]
        else:
            if branch.leaves[0].value == "0":
                branch = branch.leaves[0]
            else:
                branch = branch.leaves[1]
        result += branch.value
    return result

def calculate_ratings():

    root = GasNode(None)

    for x in input_file():
        branch = root
        for c in x:
            branch = branch.add_leaf(c)

    return int(find_co2(root), 2)*int(find_oxygen(root), 2)

print(calculate_ratings())