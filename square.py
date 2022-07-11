# Class That Stores Information For Each Square
class Square(object):
    def __init__(self, row, col):
        self.loc = (row, col)
        self.g = float("inf")

    # Activate The Square
    def open(self, g, parent):
        self.open = True # Temporary
        self.g = g
        self.parent = parent