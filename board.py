import square as s

class Board(object):
    def __init__(self, rows, cols):
        self.size = (rows, cols)
        self.board = self.create_board()

    def create_board(self):
        board = []
        for r in range(self.size[0]):
            row = []
            for c in range(self.size[1]):
                row.append(s.Square())
            board.append(row)
        return board

board = Board(5, 5, 4, 4, 3, 3)
print(board.board)