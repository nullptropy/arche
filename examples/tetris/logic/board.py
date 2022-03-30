# coding: utf-8

from .shape import Shape

class Board:
    BOARD_W = 10
    BOARD_H = 24

    def __init__(self):
        self.score = 0
        self.board = [None] * self.BOARD_W * self.BOARD_H
        self.is_game_finished = False

        self.new_shape()

    def get_shape(self, x, y):
        return self.board[x + y * self.BOARD_W]

    def set_shape(self, x, y, shape):
        self.board[x + y * self.BOARD_W] = shape

    def one_line_down(self):
        if not self.move(self.shape, self.shape.x, self.shape.y + 1):
            self.shape_dropped()

    def hard_drop(self):
        while self.move(self.shape, self.shape.x, self.shape.y + 1):
            continue

        self.shape_dropped()

    def remove_full_lines(self):
        for index in range(0, len(self.board), self.BOARD_W):
            if None not in self.board[index:index + self.BOARD_W]:
                del self.board[index:index + self.BOARD_W]
                self.board = [None] * self.BOARD_W + self.board
                self.score += 1

    def shape_dropped(self):
        for (x, y) in self.shape.coords:
            self.set_shape(
                x + self.shape.x,
                y + self.shape.y,
                self.shape.shape)

        self.remove_full_lines()
        self.new_shape()

    def new_shape(self):
        self.shape = Shape.random_shape()
        self.shape.x, self.shape.y = (
            self.BOARD_W // 2 - 1,
            0 if self.shape.shape in [2, 5] else 1)

        if not self.move(self.shape, self.shape.x, self.shape.y):
            self.is_game_finished = True

    def move(self, shape, nx, ny):
        for (x, y) in shape.coords:
            x, y = (x + nx, y + ny)
            if \
                    not (0 <= x < self.BOARD_W) or \
                    not (0 <= y < self.BOARD_H) or \
                    self.get_shape(x, y) is not None:
                return False

        self.shape = shape
        self.shape.x, self.shape.y = (nx, ny)

        return True