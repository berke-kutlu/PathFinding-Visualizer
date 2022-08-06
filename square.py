# Class that stores information for each square
class Square(object):
    def __init__(self, r, c):
        self.loc = (r, c)
        self.g = float("inf")
        self.key = False
        self.open = None
        self.wall = False

    def __lt__(self, other):
        return self.g < other.g

    # Activate the square
    def activate(self, g, parent):
        self.open = True
        self.g = g
        self.parent = parent