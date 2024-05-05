from maze import maze
from algrithms import dfs, A_star, bfs
from game import game

class CreateMaze:
    def __init__(self, x):
        self.x = x
        Maze = maze(self.x, self.x)
        Maze.generate_maze()
        print(bfs(Maze))
        print(dfs(Maze))
        #print(A_star(Maze))
        game(Maze)
    
#CreateMaze(10)