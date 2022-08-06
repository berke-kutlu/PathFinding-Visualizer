import square as square

class Board(object):
    def __init__(self, rows, cols, s_loc, t_loc):
        self.size = (rows, cols)
        self.start = s_loc
        self.target = t_loc
        self.board = self.create_board()
        self.board[self.start[0]][self.start[1]].key = True
        self.board[self.target[0]][self.target[1]].key = True

    def create_board(self):
        board = []
        for r in range(self.size[0]):
            row = []
            for c in range(self.size[1]):
                row.append(square.Square(r, c))
            board.append(row)
        return board

    def click(self, row, col):
        self.board[row][col].wall = True