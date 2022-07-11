import square as s

class Board(object):
    def __init__(self, rows, cols, s_row, s_col, t_row, t_col):
        self.size = (rows, cols)
        self.start = (s_row, s_col)
        self.target = (t_row, t_col)
        self.board = self.create_board()

    def create_board(self):
        board = []
        for r in range(self.size[0]):
            row = []
            for c in range(self.size[1]):
                row.append(s.Square(r, c))
            board.append(row)
        return board

    def getNeighbors(self, row, col):
        neighbors = []

        if row > 0: # TOP
            neighbors.append((row - 1, col))
        if row < self.rows - 1: # BOTTOM
            neighbors.append((row + 1, col))
        if col > 0: # LEFT
            neighbors.append((row, col - 1))
        if col < self.cols - 1: # RIGHT
            neighbors.append((row, col + 1))

        if row > 0 and col > 0: # TOP LEFT
            neighbors.append((row - 1, col - 1))
        if row > 0 and col < self.cols - 1: # TOP RIGHT
            neighbors.append((row - 1, col + 1))
        if row < self.rows - 1 and col > 0: # BOTTOM LEFT
            neighbors.append((row + 1, col - 1))
        if row < self.rows - 1 and col < self.cols - 1: # BOTTOM RIGHT
            neighbors.append((row + 1, col + 1))

        return neighbors

board = Board(5, 5, 4, 4, 3, 3)
print(board.board)