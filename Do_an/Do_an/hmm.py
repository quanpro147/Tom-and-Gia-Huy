import pygame 
import os 
import random
import pygame
from os import listdir 
from os.path import isfile, join
from maze import *

mazes = maze(100, 100)
mazes.generate_maze()
for i in range(100):
    for j in range(100):
        print(mazes.grid[i][j].walls[0])