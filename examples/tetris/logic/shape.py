# coding: utf-8

from random import randint

last_pick = -1
coord_matrix = [
    [[ 0, -1], [0,  0], [-1, 0], [-1, 1]], # ZShape
    [[ 0, -1], [0,  0], [ 1, 0], [ 1, 1]], # SShape
    [[-1,  0], [0,  0], [ 1, 0], [ 0, 1]], # TShape
    [[-1, -1], [0, -1], [ 0, 0], [ 0, 1]], # LShape
    [[ 0, -1], [0,  0], [ 0, 1], [ 0, 2]], # LineShape
    [[ 0,  0], [1,  0], [ 0, 1], [ 1, 1]], # SquareShape
    [[ 1, -1], [0, -1], [ 0, 0], [ 0, 1]], # MirroredLShape
]

class Shape:
    def __init__(self, shape, coords, x=0, y=0):
        self.x = x
        self.y = y
        self.shape = shape
        self.coords = coords

    def __repr__(self):
        return f'Shape({self.shape}, x={self.x}, y={self.y})'

    def rotate(self, rot):
        if self.shape != 5: # exclude SquareShape
            return self.__class__(
                self.shape, x=self.x, y=self.y,
                coords=[(-1*rot*y, rot*x) for x, y in self.coords])

        return self

    @classmethod
    def random_shape(cls):
        global last_pick

        if (shape := randint(0, 7)) in [7, last_pick]:
            shape = randint(0, 6)

        last_pick = shape
        return cls(shape, coord_matrix[shape])