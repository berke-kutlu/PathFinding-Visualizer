# Class that stores information for each square
class Square(object):
    def __init__(self):
        self.g = float("inf")
        self.open = None

    def __lt__(self, other):
        return self.g < other.g

    # Activate the square
    def activate(self, g, parent):
        self.open = True
        self.g = g
        self.parent = parent