from maze import maze
from user_interface import ui
from visual import *
from game import game

if __name__ == '__main__':
    #ui()
    Maze = maze(10, 10)
    Maze.generate_maze()
    game(Maze)

    
    
    
    