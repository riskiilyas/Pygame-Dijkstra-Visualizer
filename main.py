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

WIDTH, HEIGHT = 640, 480


def main():
    pygame.init()
    root = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            #for closing with x button top right
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

if __name__ == "__main__":
    main()
