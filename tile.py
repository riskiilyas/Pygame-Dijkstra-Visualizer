import pygame


class Tile:
    def __init__(self, i, j, w, h, cols, rows):
        self.x, self.y = i, j
        self.neighbors = []
        self.prev = None
        self.state = None
        self.wall = False
        self.visited = False
        self.cols = cols
        self.rows = rows
        self.w = w
        self.h = h

    def show(self, win, col, shape=1):
        if self.wall == True:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x * self.w, self.y * self.h, self.w - 1, self.h - 1))
        else:
            pygame.draw.circle(win, col, (self.x * self.w + self.w // 2, self.y * self.h + self.h // 2), self.w // 3)

    def add_neighbors(self, grid):
        if self.x < self.cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < self.rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
