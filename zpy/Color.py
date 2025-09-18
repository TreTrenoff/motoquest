class Color():
    """Class for defining colors in RGB format."""
    def __init__(self, r, g, b):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.r = r
        self.g = g
        self.b = b

    def to_tuple(self):
        return (self.r, self.g, self.b)
