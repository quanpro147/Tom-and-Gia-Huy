from maze import *
from user_interface import ui
from visual import show
import time

if __name__ == '__main__':
    #ui()
    Maze = maze(10, 10)
    Maze.generate_maze()
    show(Maze, 1, 'testfile')
    