"""

Dijkstra Visualizer

Quiz 2
Design & Analysis of Algorithm (IUP)
Lecturer: Misbakhul Munir Irfan Subakti, S.Kom., M.Sc.

Group Member
- Muhammad Ghifari Taqiuddin (5025211063)
- Mikhael Aryasatya Nugraha (5025211062)
- Riski Ilyas (5025211189)

"""

import pygame
import sys
import random
import math
from enum import Enum

from collections import deque
from tkinter import messagebox, Tk

from tile import Tile, TileState


class ModeState(Enum):
    MODE_BLOCK = 1
    MODE_START = 2
    MODE_FINISH = 3


SIZE = (WIDTH, HEIGHT) = 640, 480
COLS, ROWS = 64, 48
TILE_WIDTH = WIDTH // COLS
TILE_HEIGHT = HEIGHT // ROWS

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Dijkstra's Path Finding")

grid = []
queue, visited = deque(), []
path = []

for i in range(COLS):
    arr = []
    for j in range(ROWS):
        arr.append(Tile(i, j, TILE_WIDTH, TILE_HEIGHT, COLS, ROWS))
    grid.append(arr)

for i in range(COLS):
    for j in range(ROWS):
        grid[i][j].add_neighbors(grid)

start = grid[0][0]
end = grid[COLS - COLS // 2][ROWS - COLS // 4]
start.wall = False
end.wall = False

queue.append(start)
start.visited = True


def clickWall(pos, non_erase_mode, click_mode):
    i = pos[0] // TILE_WIDTH
    j = pos[1] // TILE_HEIGHT
    print(non_erase_mode)
    print(click_mode)
    if not non_erase_mode:
        grid[i][j].show(window, TileState.EMPTY)
    elif click_mode == ModeState.MODE_BLOCK:
        print('yess')
        grid[i][j].show(window, TileState.BLOCK)
    elif click_mode == ModeState.MODE_START:
        grid[i][j].show(window, TileState.START)
    elif click_mode == ModeState.MODE_FINISH:
        grid[i][j].show(window, TileState.END)


def main():
    pygame.init()
    root = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    flag = False
    noflag = True
    startflag = False
    click_mode = ModeState.MODE_BLOCK

    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    clickWall(mouse, event.button == 1, click_mode)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    clickWall(mouse, event.buttons[0], click_mode)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag = True
                elif event.key == pygame.K_1:
                    click_mode = ModeState.MODE_START
                elif event.key == pygame.K_2:
                    click_mode = ModeState.MODE_FINISH
                elif event.key == pygame.K_3:
                    click_mode = ModeState.MODE_BLOCK

        if startflag:
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev
                    if not flag:
                        flag = True
                        print("Done")
                    elif flag:
                        continue
                if not flag:
                    for i in current.neighbors:
                        if not i.visited and not i.state == TileState.BLOCK:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution")
                    noflag = False
                else:
                    continue

        window.fill((0, 20, 20))
        for i in range(COLS):
            for j in range(ROWS):
                spot = grid[i][j]
                spot.show(window)
                if spot in path:
                    spot.show(window, TileState.PATH)
                    # spot.show(window, (46, 204, 113))
                    # spot.show(window, (192, 57, 43), 0)
                elif spot.visited:
                    spot.show(window, TileState.VISITED)
                    # spot.show(window, (39, 174, 96))
                if spot in queue and not flag:
                    spot.show(window, TileState.VISITING)
                    # spot.show(window, (44, 62, 80))
                    # spot.show(window, (39, 174, 96), 0)
                if spot == start:
                    spot.show(window, TileState.START)
                    # spot.show(window, (0, 255, 200))
                if spot == end:
                    spot.show(window, TileState.END)
                    # spot.show(window, (0, 120, 255))

        pygame.display.flip()


if __name__ == "__main__":
    main()
