# Djikstra's Shortest Path Visualizer

![preview](./readme_assets/preview.png)

## About

_Quiz 2 project for Design & Analysis Algorithm IUP 2022 where
we made a shortest path finder in a maze using Djikstra's algorithm_

**Group Members**

- Mikhael Aryasatya Nugraha (5025211062)
- Muhammad Ghifari Taqiuddin (5025211063)
- Riski Ilyas (5025211189)

## Installation

Requirements:

- Python (≥ 3.10)
- pygame (≥ 2.1.2, can be installed via pip: `pip3 install pygame`)

After all requirements are satisfied, you can run the following commands

```
$ git clone https://github.com/riskiilyas/DAA-Dijkstra-Visualizer
$ cd DAA-Dijkstra-Visualizer
$ python3 main.py
```

If everything done successfully, the program window will open

## Usage

![demo](./readme_assets/demo.gif)

- There are 3 modes when inserting a new tile: starting, finish, and wall tile.
  The current mode is also displayed on the bottom of the screen, along with
  the pathfinding status.
    - Press `1` to insert the starting tile
    - Press `2` to insert the finish tile
    - Press `3` to insert wall

  After pressing the key, you can left-click anywhere in the map to insert a new tile
  and right-click to remove tile. You can also use the arrow keys to move
  the starting and finish tile around.

- To start the pathfinding process, press `Enter` key
- After the pathfinding process is done, press `Enter` again
  to restart. This will only erase the path and the visited tile, while
  keeping everything else in the same position
- Pressing `Enter` when the pathfinding process is still running will stop it
- To reset everything, press `r`. This will erase every tile and place starting
  and finish tile in their initial place
