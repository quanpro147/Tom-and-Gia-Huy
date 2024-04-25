import numpy as np
from numpy.random import shuffle
from random import randrange
#import matplotlib.pyplot as plt

class BacktrackingGenerator():
    """
    1. Randomly choose a starting cell.
    2. Randomly choose a wall at the current cell and open a passage through to any random adjacent
        cell, that has not been visited yet. This is now the current cell.
    3. If all adjacent cells have been visited, back up to the previous and repeat step 2.
    4. Stop when the algorithm has backed all the way up to the starting cell.
    """

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1

    def generate(self):
        """highest-level method that implements the maze-generating algorithm

        Returns:
            np.array: returned matrix
        """
        # create empty grid, with walls
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(1)

        crow = randrange(1, self.H, 2)
        ccol = randrange(1, self.W, 2)
        track = [(crow, ccol)]
        grid[crow][ccol] = 0

        while track:
            (crow, ccol) = track[-1]
            neighbors = self._find_neighbors(crow, ccol, grid, True)

            if len(neighbors) == 0:
                track = track[:-1]
            else:
                nrow, ncol = neighbors[0]
                grid[nrow][ncol] = 0
                grid[(nrow + crow) // 2][(ncol + ccol) // 2] = 0

                track += [(nrow, ncol)]

        return grid
    def _find_neighbors(self, r, c, grid, is_wall=False):
        """Find all the grid neighbors of the current position; visited, or not.
        Args:
            r (int): row of cell of interest
            c (int): column of cell of interest
            grid (np.array): 2D maze grid
            is_wall (bool): Are we looking for neighbors that are walls, or open cells?
        Returns:
            list: all neighboring cells that match our request
        """
        ns = []

        if r > 1 and grid[r - 2][c] == is_wall:
            ns.append((r - 2, c))
        if r < self.H - 2 and grid[r + 2][c] == is_wall:
            ns.append((r + 2, c))
        if c > 1 and grid[r][c - 2] == is_wall:
            ns.append((r, c - 2))
        if c < self.W - 2 and grid[r][c + 2] == is_wall:
            ns.append((r, c + 2))

        shuffle(ns)
        return ns
    
     
class maze():
    def __init__(self, h, w):
        '''
        h (int): height of maze, in number of hallways
        w (int): width of maze, in number of hallways
        H (int): height of maze, in number of hallways + walls
        W (int): width of maze, in number of hallways + walls

        '''
        self.h = h
        self.w = w
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1
        self.generator = None
        self.grid = None
        self.start = None
        self.end = None
        self.transmuters = []
        self.solver = None
        self.solutions = None

    
    def generate(self):
        self.generator = BacktrackingGenerator(self.h, self.w)
        self.grid = self.generator.generate()

    def generate_entrances(self, start_outer=True, end_outer=True):
        """Generate maze entrances. Entrances can be on the walls, or inside the maze.

        Args:
            start_outer (bool): Do you want the start of the maze to be on an outer wall?
            end_outer (bool): Do you want the end of the maze to be on an outer wall?
        Returns: None
        """
        if start_outer and end_outer:
            self._generate_outer_entrances()
        elif not start_outer and not end_outer:
            self._generate_inner_entrances()
        elif start_outer:
            self.start, self.end = self._generate_opposite_entrances()
        else:
            self.end, self.start = self._generate_opposite_entrances()

        # the start and end shouldn't be right next to each other
        if abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1]) < 2:
            self.generate_entrances(start_outer, end_outer)

    def _generate_outer_entrances(self):
        """Generate maze entrances, along the outer walls.

        Returns: None
        """
        H = self.grid.shape[0]
        W = self.grid.shape[1]

        start_side = randrange(4)

        # maze entrances will be on opposite sides of the maze.
        if start_side == 0:
            self.start = (0, randrange(1, W, 2))  # North
            self.end = (H - 1, randrange(1, W, 2))
        elif start_side == 1:
            self.start = (H - 1, randrange(1, W, 2))  # South
            self.end = (0, randrange(1, W, 2))
        elif start_side == 2:
            self.start = (randrange(1, H, 2), 0)  # West
            self.end = (randrange(1, H, 2), W - 1)
        else:
            self.start = (randrange(1, H, 2), W - 1)  # East
            self.end = (randrange(1, H, 2), 0)

    def _generate_inner_entrances(self):
        """Generate maze entrances, randomly within the maze.

        Returns: None
        """
        H, W = self.grid.shape

        self.start = (randrange(1, H, 2), randrange(1, W, 2))
        end = (randrange(1, H, 2), randrange(1, W, 2))

        # make certain the start and end points aren't the same
        while end == self.start:
            end = (randrange(1, H, 2), randrange(1, W, 2))

        self.end = end

    def _generate_opposite_entrances(self):
        """Generate one inner and one outer entrance.

        Returns:
            tuple: start cell, end cell
        """
        H, W = self.grid.shape

        start_side = randrange(4)

        # pick a side for the outer maze entrance
        if start_side == 0:
            first = (0, randrange(1, W, 2))  # North
        elif start_side == 1:
            first = (H - 1, randrange(1, W, 2))  # South
        elif start_side == 2:
            first = (randrange(1, H, 2), 0)  # West
        else:
            first = (randrange(1, H, 2), W - 1)  # East

        # create an inner maze entrance
        second = (randrange(1, H, 2), randrange(1, W, 2))

        return (first, second)

# def showPNG(grid):
#     """Generate a simple image of the maze."""
#     plt.figure(figsize=(10, 5))
#     plt.imshow(grid, cmap=plt.cm.binary, interpolation='nearest')
#     plt.xticks([]), plt.yticks([])
#     plt.show()
a = maze(5, 5)
a.generate()
a.generate_entrances()
print(a.grid)
