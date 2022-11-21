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

from collections import deque
from tkinter import messagebox, Tk

SIZE = (WIDTH, HEIGHT) = 640, 480
COLS, ROWS = 64, 48
TILE_WIDTH = WIDTH // COLS
TILE_HEIGHT = HEIGHT // ROWS

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Dijkstra's Path Finding")

grid = []
queue, visited = deque(), []
path = []


def main():
    pygame.init()
    root = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    
    flag = False
    noflag = True
    startflag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    pass  # clickWall(pygame.mouse.get_pos(), event.button==1)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    pass  # clickWall(pygame.mouse.get_pos(), event.buttons[0])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag = True


if __name__ == "__main__":
    main()
