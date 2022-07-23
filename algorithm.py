import math

class Algorithm(object):
    def __init__(self, board, s_row, s_col, t_row, t_col):
        self.board = board
        self.start = (s_row, s_col)
        self.target = (t_row, t_col)
        self.interested_nodes = []
        self.board.board[self.start[0]][self.start[1]].activate(0, self.start)
        self.interested_nodes.append(self.board.board[self.start[0]][self.start[1]])

    def measure_neighbors(self, row, col):
        # Get the list of open or none visited neighbors
        neighbors = []
        if row > 0: # TOP
            neighbors.append((row - 1, col))
        if row > 0 and col < self.cols - 1: # TOP RIGHT
            neighbors.append((row - 1, col + 1))
        if col < self.cols - 1: # RIGHT
            neighbors.append((row, col + 1))
        if row < self.rows - 1 and col < self.cols - 1: # BOTTOM RIGHT
            neighbors.append((row + 1, col + 1))
        if row < self.rows - 1: # BOTTOM
            neighbors.append((row + 1, col))
        if row < self.rows - 1 and col > 0: # BOTTOM LEFT
            neighbors.append((row + 1, col - 1))
        if col > 0: # LEFT
            neighbors.append((row, col - 1))
        if row > 0 and col > 0: # TOP LEFT
            neighbors.append((row - 1, col - 1))
        
        for (nr, nc) in neighbors:
            if self.board.board[nr][nc].open == False:
                neighbors.remove((nr, nc))

        # Set the length and parent
        for (nr, nc) in neighbors:
            start_distance = self.board.board[row][col].g + self.calculate_length(row, col, nr, nc)
            # If the length is defined for the first time or it is shorter change it's length and parent
            if start_distance < self.board.board[nr][nc].g:
                self.board.board[nr][nc].activate(start_distance, (row, col))
            # Place it in interested nodes if it isnt already in it
            if not self.board.board[nr][nc] in self.interested_nodes:
                self.interested_nodes.append(self.board.board[nr][nc])

        self.board.board[row][col].open = False
        
    # Sort interested nodes    
    def sort_interests(self):
        self.interested_nodes.sort()

    # Calculate the length between parent (pr, pc) and main (mr, mc) square
    def calculate_length(self, pr, pc, mr, mc):
        return int(round(math.sqrt(((pr - mr) ** 2 + (pc - mc) ** 2)), 1) * 10)