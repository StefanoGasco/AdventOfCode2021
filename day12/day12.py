
ENV = 'real'


def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip().split("-") for x in f.readlines()]
    return lines

visited = []

class Node():
    def __init__(self, value):
        self.value = value
        self.connections = []

    def __repr__(self):
        return f"Connected to {[x.value for x in self.connections]}"

    def connect(self, node):
        if node.value != "start" and self.value != "end":
            self.connections.append(node)
        if self.value != "start" and node.value != "end":
            node.connections.append(self)

    def two_way(self, node):
        return self.value.isupper() and node.value not in ["start", "end"]

    def visit(self):
        res = 0
        if self.value.islower() and self.value not in ["start", "end"]:
            visited.append(self)
        if self.connections != []:
            for node in self.connections:
                if node not in visited:
                    res += node.visit()
        else:
            if self.value == "end":
                return 1
            else:
                return 0
        if self.value.islower() and self.value not in ["start", "end"]:
            visited.remove(self)
        return res

connections = input_file()
nodes = {}
for couple in connections:
    first, second = couple
    nodes[first] = nodes.get(first, Node(first))
    nodes[second] = nodes.get(second, Node(second))
    nodes[first].connect(nodes[second])

print(nodes)

root = nodes["start"]
print(root.visit())