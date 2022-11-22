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
start = None
end = None


def init_scenario():
    print('ahlloo')
    global grid, queue, visited, path, start, end
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
    start.visited = False
    end.visited = False
    queue.append(start)


def click_wall(pos, non_erase_mode, click_mode):
    i = pos[0] // TILE_WIDTH
    j = pos[1] // TILE_HEIGHT
    global start
    global end
    if not non_erase_mode:
        grid[i][j].show(window, TileState.EMPTY)
    elif click_mode == ModeState.MODE_BLOCK:
        grid[i][j].show(window, TileState.BLOCK)
    elif click_mode == ModeState.MODE_START:
        start.show(window, TileState.EMPTY)
        start = grid[i][j]
        queue.clear()
        queue.append(start)
        start.show(window, TileState.START)
    elif click_mode == ModeState.MODE_FINISH:
        end.show(window, TileState.EMPTY)
        end = grid[i][j]
        end.show(window, TileState.END)


def main():
    pygame.init()
    root = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    flag = False
    noflag = True
    startflag = False
    finished = False
    click_mode = ModeState.MODE_BLOCK

    init_scenario()
    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    click_wall(mouse, event.button == 1, click_mode)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    click_wall(mouse, event.buttons[0], click_mode)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if finished:
                        finished = False
                        startflag = False
                        flag = False
                        noflag = True
                        init_scenario()
                    else:
                        startflag = True
                elif event.key == pygame.K_1:
                    click_mode = ModeState.MODE_START
                elif event.key == pygame.K_2:
                    click_mode = ModeState.MODE_FINISH
                elif event.key == pygame.K_3:
                    click_mode = ModeState.MODE_BLOCK

        if startflag:
            start.visited = True
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
                    finished = True

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
                finished = True

        window.fill((255, 255, 255))
        for i in range(COLS):
            for j in range(ROWS):
                spot = grid[i][j]
                spot.show(window)
                if spot in path:
                    spot.show(window, TileState.PATH)
                elif spot.visited:
                    spot.show(window, TileState.VISITED)
                if spot in queue and not flag:
                    spot.show(window, TileState.VISITING)
                if spot == start:
                    spot.show(window, TileState.START)
                if spot == end:
                    spot.show(window, TileState.END)

        pygame.display.flip()


if __name__ == "__main__":
    main()
