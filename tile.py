import pygame

from enum import Enum
from utils import hex_to_rgb

class TileState(Enum):
    START = ("#FC6589", "#B92347")
    FINISH = ("#2BCCFF", "#1099C5")
    EMPTY = ("#F8F8F8", "#E2E2E2")
    BLOCK = ("#7A7A7A", "#666666")
    VISITED = ("#8ECC5D", "#57A519")
    VISITING = ("#C0EF9B", "#8ECC5D")
    PATH = ("#FFC368", "#CD8E30")

    def __init__(self, fill, border):
        self.fill = fill
        self.border = border


class Tile:
    def __init__(self, i, j, w, h, cols, rows):
        self.x, self.y = i, j
        self.neighbors = []
        self.prev = None
        self.state = TileState.EMPTY
        self.visited = False
        self.cols = cols
        self.rows = rows
        self.w = w
        self.h = h

    def show(self, window, state=None):
        if state is not None:
            self.state = state
        pygame.draw.rect(window, hex_to_rgb(self.state.fill), (self.x * self.w, self.y * self.h, self.w, self.h))
        pygame.draw.rect(window, hex_to_rgb(self.state.border), (self.x * self.w, self.y * self.h, self.w, self.h), 1)

    def add_neighbors(self, grid):
        if self.x < self.cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < self.rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.x < self.cols - 1 and self.y < self.rows - 1:
            self.neighbors.append(grid[self.x + 1][self.y + 1])
        if self.x < self.cols - 1 and self.y > 0:
            self.neighbors.append(grid[self.x + 1][self.y - 1])
        if self.x > 0 and self.y < self.rows - 1:
            self.neighbors.append(grid[self.x - 1][self.y + 1])
        if self.x > 0 and self.y > 0:
            self.neighbors.append(grid[self.x - 1][self.y - 1])
