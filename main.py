"""

Dijkstra Visualizer

Quiz 2
Design & Analysis of Algorithm (IUP)
Lecturer: Misbakhul Munir Irfan Subakti, S.Kom., M.Sc.

Group Member
- Mikhael Aryasatya Nugraha (5025211062)
- Muhammad Ghifari Taqiuddin (5025211063)
- Riski Ilyas (5025211189)

"""

import sys
import pygame

from enum import Enum
from collections import deque
from tile import Tile, TileState
from utils import hex_to_rgb


class ModeState(Enum):
    MODE_WALL = 1
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
start_tile = None
finish_tile = None
tile_insert_mode = "WALL"
status = "READY"


def reset_visited_path():
    global grid, start_tile, queue, visited, path
    queue = deque()
    visited = []
    path = []

    queue.append(start_tile)

    for i in range(COLS):
        for j in range(ROWS):
            tile = grid[i][j]
            tile.visited = False
            if tile.state in (TileState.VISITED, TileState.VISITING, TileState.PATH):
                tile.state = TileState.EMPTY


def init_scenario():
    global grid, queue, visited, path, start_tile, finish_tile
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

    start_tile = grid[COLS // 4][ROWS // 2]
    finish_tile = grid[COLS - COLS // 4][ROWS // 2]
    start_tile.visited = False
    finish_tile.visited = False
    queue.append(start_tile)


def click_wall(pos, non_erase_mode, click_mode):
    i = pos[0] // TILE_WIDTH
    j = pos[1] // TILE_HEIGHT
    global start_tile, finish_tile
    if not non_erase_mode:
        if i >= 0 and j >= 0 and i < COLS and j < ROWS:
            grid[i][j].show(window, TileState.EMPTY)
    elif click_mode == ModeState.MODE_WALL:
        if i >= 0 and j >= 0 and i < COLS and j < ROWS:
            grid[i][j].show(window, TileState.BLOCK)
    elif click_mode == ModeState.MODE_START:
        if i >= 0 and j >= 0 and i < COLS and j < ROWS:
            start_tile.show(window, TileState.EMPTY)
            start_tile = grid[i][j]
            queue.clear()
            queue.append(start_tile)
            start_tile.show(window, TileState.START)
    elif click_mode == ModeState.MODE_FINISH:
        if i >= 0 and j >= 0 and i < COLS and j < ROWS:
            finish_tile.show(window, TileState.EMPTY)
            finish_tile = grid[i][j]
            finish_tile.show(window, TileState.FINISH)


def main():
    flag = False
    noflag = True
    startflag = False
    finished = False
    end_path = deque()
    click_mode = ModeState.MODE_WALL
    global tile_insert_mode, status, start_tile, finish_tile

    init_scenario()
    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and startflag is False:
                if event.button in (1, 3):
                    click_wall(mouse, event.button == 1, click_mode)
            elif event.type == pygame.MOUSEMOTION and startflag is False:
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
                        end_path = deque()
                        reset_visited_path()
                    else:
                        if not startflag:
                            status = "EXPLORING MAPS..."
                            startflag = True
                        else:
                            status = "READY"
                            startflag = False
                            reset_visited_path()
                elif event.key == pygame.K_r:
                    if not startflag:
                        init_scenario()
                elif event.key == pygame.K_1:
                    click_mode = ModeState.MODE_START
                    tile_insert_mode = "START"
                elif event.key == pygame.K_2:
                    click_mode = ModeState.MODE_FINISH
                    tile_insert_mode = "FINISH"
                elif event.key == pygame.K_3:
                    click_mode = ModeState.MODE_WALL
                    tile_insert_mode = "WALL"

                if click_mode == ModeState.MODE_START and startflag is False:
                    if event.key == pygame.K_UP:
                        global start_tile
                        start_tile.show(window, TileState.EMPTY)
                        start_tile = grid[start_tile.x][start_tile.y - 1]
                        queue.clear()
                        queue.append(start_tile)
                        start_tile.show(window, TileState.START)

                    elif event.key == pygame.K_DOWN:
                        start_tile.show(window, TileState.EMPTY)
                        if start_tile.y < ROWS - 1:
                            start_tile = grid[start_tile.x][start_tile.y + 1]
                        else:
                            start_tile = grid[start_tile.x][0]
                        queue.clear()
                        queue.append(start_tile)
                        start_tile.show(window, TileState.START)

                    elif event.key == pygame.K_LEFT:
                        start_tile.show(window, TileState.EMPTY)
                        start_tile = grid[start_tile.x - 1][start_tile.y]
                        queue.clear()
                        queue.append(start_tile)
                        start_tile.show(window, TileState.START)

                    elif event.key == pygame.K_RIGHT:
                        start_tile.show(window, TileState.EMPTY)
                        if start_tile.x < COLS - 1:
                            start_tile = grid[start_tile.x + 1][start_tile.y]
                        else:
                            start_tile = grid[0][start_tile.y]
                        queue.clear()
                        queue.append(start_tile)
                        start_tile.show(window, TileState.START)

                elif click_mode == ModeState.MODE_FINISH and startflag is False:
                    if event.key == pygame.K_UP:
                        global finish_tile
                        finish_tile.show(window, TileState.EMPTY)
                        finish_tile = grid[finish_tile.x][finish_tile.y - 1]
                        finish_tile.show(window, TileState.FINISH)

                    elif event.key == pygame.K_DOWN:
                        finish_tile.show(window, TileState.EMPTY)
                        if finish_tile.y < ROWS - 1:
                            finish_tile = grid[finish_tile.x][finish_tile.y + 1]
                        else:
                            finish_tile = grid[finish_tile.x][0]
                        finish_tile.show(window, TileState.FINISH)

                    elif event.key == pygame.K_LEFT:
                        finish_tile.show(window, TileState.EMPTY)
                        finish_tile = grid[finish_tile.x - 1][finish_tile.y]
                        finish_tile.show(window, TileState.FINISH)

                    elif event.key == pygame.K_RIGHT:
                        finish_tile.show(window, TileState.EMPTY)
                        if finish_tile.x < COLS - 1:
                            finish_tile = grid[finish_tile.x + 1][finish_tile.y]
                        else:
                            finish_tile = grid[0][finish_tile.y]
                        finish_tile.show(window, TileState.FINISH)

        if startflag:
            start_tile.visited = True
            if len(queue) > 0:
                current = queue.popleft()
                if current == finish_tile:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev
                    if not flag:
                        flag = True
                        steps = len(path)
                        status = "FOUND IN " + str(steps) + " STEPS"
                    finished = True

                if not flag:
                    for i in current.neighbors:
                        if not (i.visited or i.state == TileState.BLOCK):
                            if i.x == current.x+1 and i.y == current.y-1:
                                if not (grid[current.x+1][current.y].state == TileState.BLOCK and grid[current.x][current.y-1].state == TileState.BLOCK):
                                    i.visited = True
                                    i.prev = current
                                    queue.append(i)
                            elif i.x == current.x-1 and i.y == current.y-1:
                                if not (grid[i.x][current.y].state == TileState.BLOCK and grid[current.x][i.y].state == TileState.BLOCK):
                                    i.visited = True
                                    i.prev = current
                                    queue.append(i)
                            elif i.x == current.x-1 and i.y == current.y+1:
                                if not (grid[current.x-1][current.y].state == TileState.BLOCK and grid[current.x][current.y+1].state == TileState.BLOCK):
                                    i.visited = True
                                    i.prev = current
                                    queue.append(i)
                            elif i.x == current.x+1 and i.y == current.y+1:
                                if not (grid[current.x+1][current.y].state == TileState.BLOCK and grid[current.x][current.y+1].state == TileState.BLOCK):
                                    i.visited = True
                                    i.prev = current
                                    queue.append(i)
                            else:
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
            mode_label = font.render("PRESS ENTER TO RESTART", False, hex_to_rgb("#000000"))
        else:
            mode_label = font.render("MODE: " + tile_insert_mode, False, hex_to_rgb("#000000"))
        status_label = font.render(status, False, hex_to_rgb("#000000"))

        window.blit(mode_label, (10, 490))
        window.blit(status_label, (380, 490))
        for i in range(COLS):
            for j in range(ROWS):
                spot = grid[i][j]
                spot.show(window)
                if spot.visited:
                    spot.show(window, TileState.VISITED)
                if spot in queue and not flag:
                    spot.show(window, TileState.VISITING)
                if spot == start_tile:
                    spot.show(window, TileState.START)
                if spot == finish_tile:
                    spot.show(window, TileState.FINISH)

        if finished:
            if len(path) > 0:
                end_path.append(path.pop())

            for i in end_path:
                if i.state != TileState.START:
                    i.show(window, TileState.PATH)

        pygame.display.flip()


if __name__ == "__main__":
    main()
