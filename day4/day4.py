
ENV = 'real'

def get_boards(entry):
    board = []
    for x in range(len(entry)):
        board.append(entry[x].split())
        if (x+1)%5 == 0:
            yield board
            board = []

class Board():
    def __init__(self, board):
        self.board = [list(map(int, x)) for x in board]
        self.value = sum([sum(x) for x in self.board])
        self.founds = 0

    def cross(self, n):
        for ir, row in enumerate(self.board):
            for ic, cell in enumerate(row):
                if self.board[ir][ic] == n:
                    self.founds += n
                    self.board[ir][ic] = "x"
                if self.check_victory(ir, ic):
                    return True
        return False

    def row(self, i):
        return self.board[i]

    def col(self, i):
        return [row[i] for row in self.board]

    def check_row(self, i):
        return all(x == "x" for x in self.row(i))

    def check_col(self, i):
        return all(x == "x" for x in self.col(i))

    def check_victory(self, x, y):
        if self.check_row(x) or self.check_col(y):
            return True
        return False



def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    return [x for x in lines if x != ""]

def checker(numbers, boards):
    for x in numbers:
        for b in boards:
            if b.cross(x):
                return x, b

entry = input_file()

numbers = [int(x) for x in entry[0].split(",")]
boards = [Board(x) for x in get_boards(entry[1:])]

n, winner = checker(numbers, boards)
print((winner.value-winner.founds)*n)