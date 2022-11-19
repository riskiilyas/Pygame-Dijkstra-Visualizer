import pygame
from enum import Enum


class TileState(Enum):
    START = (0, 255, 200)
    END = (0, 120, 255)
    EMPTY = (44, 62, 80)
    BLOCK = (0, 0, 0)
    VISITED = (39, 174, 96)
    VISITING = (39, 174, 96)
    PATH = (192, 57, 43)

    def __init__(self, color):
        self.color = color


class Tile:
    def __init__(self, i, j, w, h, cols, rows):
        self.x, self.y = i, j
        self.neighbors = []
        self.prev = None
        self.state = TileState.EMPTY
        # self.wall = False
        # self.visited = False
        self.cols = cols
        self.rows = rows
        self.w = w
        self.h = h

    def show(self, win, state):
        self.state = state
        pygame.draw.rect(win, self.state.color, (self.x * self.w, self.y * self.h, self.w - 1, self.h - 1))

    def add_neighbors(self, grid):
        if self.x < self.cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < self.rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
