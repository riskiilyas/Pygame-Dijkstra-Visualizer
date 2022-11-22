import pygame
from enum import Enum


class TileState(Enum):
    START = ((252, 101, 137), (185, 35, 71))
    END = ((43, 204, 255), (16, 153, 197))
    EMPTY = ((248, 248, 248), (226, 226, 226))
    BLOCK = ((122, 122, 122), (102, 102, 102))
    VISITED = ((142, 204, 93), (87, 165, 25))
    VISITING = ((192, 239, 155), (142, 204, 93))
    PATH = ((255, 195, 104), (205, 142, 48))

    def __init__(self, fill, border):
        self.fill = fill
        self.border = border


class Tile:
    def __init__(self, i, j, w, h, cols, rows):
        self.x, self.y = i, j
        self.neighbors = []
        self.prev = None
        self.state = TileState.EMPTY
        # self.wall = False
        self.visited = False
        self.cols = cols
        self.rows = rows
        self.w = w
        self.h = h

    def show(self, window, state=None):
        if state is not None:
            self.state = state
        """
        types(by probably if statements):
        WALL
        EMPTY
        VISITING
        """
        #inside if
        # draw inner rectangle
        print(self.state.fill)
        pygame.draw.rect(window, self.state.fill, (self.x * self.w, self.y * self.h, self.w - 1, self.h - 1))
        # draw border

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
