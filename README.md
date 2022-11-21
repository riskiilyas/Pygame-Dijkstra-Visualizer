# Djikstra's Shortest Path Visualizer

## About

This repository contains the code of the shortest path
algorithm visualizer written in Python for the Quiz 2 of
Design & Analysis of Algorithm IUP Class of 2022

**Group Members**

- Mikhael Aryasatya Nugraha (5025211062)
- Muhammad Ghifari Taqiuddin (5025211063)
- Riski Ilyas (5025211189)

## Installation

In order to install this, you would first require python (≥ 3.10).
After python has been installed, run the following commands

```
$ git clone https://github.com/riskiilyas/DAA-Dijkstra-Visualizer
$ cd DAA-Dijkstra-Visualizer
$ pip3 install -r requirements.txt
$ python3 main.py
```

If everything done successfully, the program window will open

## Usage

- There are 3 modes when inserting a new tile: starting, finish, and wall tile.
  There can only be one starting and finish tile in the map.
    - Press `1` to insert the starting tile
    - Press `2` to insert the finish tile
    - Press `3` to insert wall

  After pressing the key, you can click anywhere in the map to insert the corresponding tile

- To start the pathfinding process, press `Enter` key
- To stop the process, press `q`
- To restart pathfinding, press `r`
