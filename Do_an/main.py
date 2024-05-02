from maze import maze
from algrithms import dfs, A_star
from game import game

if __name__ == '__main__':
    Maze = maze(10, 10)
    Maze.generate_maze()
    print(A_star(Maze))
    game(Maze)
    