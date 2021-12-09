
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [list(x.strip()) for x in f.readlines()]
    return lines

class Node():
    def __init__(self, n, w, h):
        self.n = n
        self.w = w
        self.h = h
        self.connections = []

    def __repr__(self):
        return f"{self.n=} - {self.w=} - {self.h=}"


    def connect(self, other_node):
        if not other_node in self.connections:
            self.connections.append(other_node)

class Board():
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.visited = []
        self.roots = []
        self.generate_nodes()
        self.generate_trees()

    def generate_nodes(self):
        for h in range(self.height):
            for w in range(self.width):
                self.board[h][w] = Node(self.board[h][w], w, h)

    def generate_trees(self):
        for h in range(self.height):
            for w in range(self.width):
                node = self.board[h][w]
                if node not in self.visited and node.n != '9':
                    self.visited.append(node)
                    self.roots.append(node)
                    self.draw_connections(node)

    def draw_connections(self, node):
        self.up(node)
        self.down(node)
        self.left(node)
        self.right(node)
        for next_node in node.connections:
            self.draw_connections(next_node)

    def up(self, node):
        if 0 <= node.w < self.width and 0 <= node.h - 1 < self.height:
            up_node = self.board[node.h-1][node.w]
            if up_node not in self.visited and up_node.n != '9':
                self.visited.append(up_node)
                node.connect(up_node)

    def down(self, node):
        if 0 <= node.w < self.width and 0 <= node.h + 1 < self.height:
            down_node = self.board[node.h + 1][node.w]
            if down_node not in self.visited and down_node.n != '9':
                self.visited.append(down_node)
                node.connect(down_node)

    def left(self, node):
        if 0 <= node.w-1 < self.width and 0 <= node.h < self.height:
            left_node = self.board[node.h][node.w-1]
            if left_node not in self.visited and left_node.n != '9':
                self.visited.append(left_node)
                node.connect(left_node)

    def right(self, node):
        if 0 <= node.w+1 < self.width and 0 <= node.h < self.height:
            right_node = self.board[node.h][node.w+1]
            if right_node not in self.visited and right_node.n != '9':
                self.visited.append(right_node)
                node.connect(right_node)

def tree_length(root):
    if root.connections == []:
        return 1
    else:
        count = 1
        for branch in root.connections:
            count += tree_length(branch)
        return count

b = Board(input_file())

import math

print(math.prod(sorted([tree_length(root) for root in b.roots])[-3:]))