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

import sys
import pygame

from enum import Enum
from collections import deque
from tile import Tile, TileState
from utils import hex_to_rgb

class ModeState(Enum):
    MODE_BLOCK = 1
    MODE_START = 2
    MODE_FINISH = 3


SIZE = (WIDTH, HEIGHT) = 640, 480
COLS, ROWS = 64, 48
TILE_WIDTH = WIDTH // COLS
TILE_HEIGHT = HEIGHT // ROWS

window = pygame.display.set_mode((WIDTH, HEIGHT + 40))
pygame.display.set_caption("Dijkstra's Path Finding")

pygame.init()
font = pygame.font.Font("Pixeltype.ttf", 40)

grid = []
queue, visited = deque(), []
path = []
start = None
end = None
mode = "WALL"
status = "READY"

def init_scenario():
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

    start = grid[COLS // 4][ROWS // 2]
    end = grid[COLS - COLS // 4][ROWS // 2]
    start.visited = False
    end.visited = False
    queue.append(start)


def click_wall(pos, non_erase_mode, click_mode):
    i = pos[0] // TILE_WIDTH
    j = pos[1] // TILE_HEIGHT
    global start, end
    if not non_erase_mode:
        if i >= 0 and j >= 0 and i < COLS and j < ROWS:
            grid[i][j].show(window, TileState.EMPTY)
            if i + 1 < COLS:
                grid[i + 1][j].show(window, TileState.EMPTY)
            if j + 1 < ROWS:
                grid[i][j + 1].show(window, TileState.EMPTY)
            if i + 1 < COLS and j + 1 < ROWS:
                grid[i + 1][j + 1].show(window, TileState.EMPTY)
    elif click_mode == ModeState.MODE_BLOCK:
        if i >= 0 and j >= 0 and i < COLS and j < ROWS:
            grid[i][j].show(window, TileState.BLOCK)
            if i + 1 < COLS:
                grid[i + 1][j].show(window, TileState.BLOCK)
            if j + 1 < ROWS:
                grid[i][j + 1].show(window, TileState.BLOCK)
            if i + 1 < COLS and j + 1 < ROWS:
                grid[i + 1][j + 1].show(window, TileState.BLOCK)
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
    flag = False
    noflag = True
    startflag = False
    finished = False
    click_mode = ModeState.MODE_BLOCK
    global mode, status

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
                        status = "READY"
                        finished = False
                        startflag = False
                        flag = False
                        noflag = True
                        init_scenario()
                    else:
                        startflag = True
                elif event.key == pygame.K_1:
                    click_mode = ModeState.MODE_START
                    mode = "START"
                elif event.key == pygame.K_2:
                    click_mode = ModeState.MODE_FINISH
                    mode = "FINISH"
                elif event.key == pygame.K_3:
                    click_mode = ModeState.MODE_BLOCK
                    mode = "WALL"

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
                        status = "FOUND " + str(len(path)) + " STEPS"
                    finished = True

                if not flag:
                    status = "WALKING..."
                    for i in current.neighbors:
                        if not i.visited and not i.state == TileState.BLOCK:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    noflag = False
                    status = "NO PATH FOUND :("
                finished = True

        window.fill(hex_to_rgb("#ffffff"))

        if finished:
            mode_label = font.render("Press Enter to Restart", False, hex_to_rgb("#000000"))
        else:
            mode_label = font.render("MODE: " + mode, False, hex_to_rgb("#000000"))
        status_label = font.render(status, False, hex_to_rgb("#000000"))

        window.blit(mode_label, (10, 490))
        window.blit(status_label, (400, 490))
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
