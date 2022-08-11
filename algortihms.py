import math
from tracemalloc import start

# Djikstra Algortihm
class Djikstra(object):
    def __init__(self, board, s_loc, t_loc):
        self.board = board
        self.start = s_loc
        self.target = t_loc

        self.interested_nodes = []
        self.board.board[self.start[0]][self.start[1]].activate(0, self.start)
        self.interested_nodes.append(self.board.board[self.start[0]][self.start[1]])

    def get_neighbors(self, row, col):
        # Get the list of open or none visited neighbors
        neighbors = []
        if row > 0 and not self.board.board[row - 1][col].wall: # TOP
            neighbors.append((row - 1, col))
        if row > 0 and col < self.board.size[1] - 1 and not self.board.board[row - 1][col + 1].wall: # TOP RIGHT
            neighbors.append((row - 1, col + 1))
        if col < self.board.size[1] - 1 and not self.board.board[row][col + 1].wall: # RIGHT
            neighbors.append((row, col + 1))
        if row < self.board.size[0] - 1 and col < self.board.size[1] - 1 and not self.board.board[row + 1][col + 1].wall: # BOTTOM RIGHT
            neighbors.append((row + 1, col + 1))
        if row < self.board.size[0] - 1 and not self.board.board[row + 1][col].wall: # BOTTOM
            neighbors.append((row + 1, col))
        if row < self.board.size[0] - 1 and col > 0 and not self.board.board[row + 1][col - 1].wall: # BOTTOM LEFT
            neighbors.append((row + 1, col - 1))
        if col > 0 and not self.board.board[row][col - 1].wall: # LEFT
            neighbors.append((row, col - 1))
        if row > 0 and col > 0 and not self.board.board[row - 1][col - 1].wall: # TOP LEFT
            neighbors.append((row - 1, col - 1))
        
        # Remove Closed Neighbors
        for (nr, nc) in neighbors:
            if self.board.board[nr][nc].open == False:
                neighbors.remove((nr, nc))
        
        return neighbors

    # Set the length and parent
    def set_neighbors(self, row, col, neighbors):
        for (nr, nc) in neighbors:
            start_distance = self.board.board[row][col].g + self.calculate_length(row, col, nr, nc)
            # If the length is defined for the first time or it is shorter change it's length and parent
            if start_distance < self.board.board[nr][nc].g:
                self.board.board[nr][nc].activate(start_distance, (row, col))
            # Place it in interested nodes if it isnt already in it
            if (not self.board.board[nr][nc] in self.interested_nodes) and self.board.board[nr][nc].open:
                self.interested_nodes.append(self.board.board[nr][nc])

    def close_square(self, row, col):
        # Close and remove the current interested node
        self.board.board[row][col].open = False
        self.interested_nodes.remove(self.board.board[row][col])
        
    # Sort interested nodes    
    def sort_interests(self):
        self.interested_nodes.sort()

    # Calculate the length between parent (pr, pc) and main (mr, mc) square
    def calculate_length(self, pr, pc, mr, mc):
        return int(round(math.sqrt(((pr - mr) ** 2 + (pc - mc) ** 2)), 1) * 10)

    def solve(self):
        # Solve The Algorithm
        neighbors = self.get_neighbors(self.interested_nodes[0].loc[0], self.interested_nodes[0].loc[1])
        self.set_neighbors(self.interested_nodes[0].loc[0], self.interested_nodes[0].loc[1], neighbors)
        self.close_square(self.interested_nodes[0].loc[0], self.interested_nodes[0].loc[1])
        self.sort_interests()

        if self.board.board[self.target[0]][self.target[1]] in self.interested_nodes:
            cparent = self.board.board[self.target[0]][self.target[1]].parent
            while True:
                self.board.board[cparent[0]][cparent[1]].key = True
                cparent = self.board.board[cparent[0]][cparent[1]].parent
                if cparent == self.start:
                    break
            return True