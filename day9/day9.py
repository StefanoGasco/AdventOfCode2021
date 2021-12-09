

ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        lines = [list(x.strip()) for x in f.readlines()]
    return lines

class Board():
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.count = 0

    def parser(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.checker(w, h):
                    print(int(self.board[h][w]))
                    self.count += (int(self.board[h][w]) + 1)
    def checker(self, w, h):
        directions = [self.up, self.down, self.left, self.right]
        return all([int(self.board[h][w]) < int(func(w,h)) for func in directions])

    def up(self, w, h):
        if 0 <= w < self.width and 0 <= h - 1 < self.height:
            return self.board[h-1][w]
        else:
            return 10

    def down(self, w, h):
        if 0 <= w < self.width and 0 <= h + 1 < self.height:
            return self.board[h+1][w]
        else:
            return 10

    def left(self, w, h):
        if 0 <= w - 1 < self.width and 0 <= h < self.height:
            return self.board[h][w-1]
        else:
            return 10

    def right(self, w, h):
        if 0 <= w + 1 < self.width and 0 <= h < self.height:
            return self.board[h][w+1]
        else:
            return 10


board = input_file()
board_w = len(board[0])
board_h = len(board)
print(board_h, board_w)

a = Board(board)
a.parser()
print(a.count)
