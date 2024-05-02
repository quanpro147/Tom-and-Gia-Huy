import pygame
from constants import *

class cell():

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col
        self.y = row
        self.walls = {'top': True, 'bot': True, 'right': True, 'left': True}
        self.is_visited = False
        self.is_entry_exit = None
        self.thickness = 4

    def draw(self, screen):
        """ This function use to draw wall if it appear """
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE

        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y), (x + CELL_SIZE, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), self.thickness)
        if self.walls['bot']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + CELL_SIZE, y + CELL_SIZE), (x , y + CELL_SIZE), self.thickness)
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y + CELL_SIZE), (x, y), self.thickness)

    def get_rects(self):
        """ This function use to mask the wall to process collision """
        rects = []
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls['top']:
            rects.append(pygame.Rect( (x, y), (CELL_SIZE, self.thickness) ))
        if self.walls['right']:
            rects.append(pygame.Rect( (x + CELL_SIZE, y), (self.thickness, CELL_SIZE) ))
        if self.walls['bot']:
            rects.append(pygame.Rect( (x, y + CELL_SIZE), (CELL_SIZE , self.thickness) ))
        if self.walls['left']:
            rects.append(pygame.Rect( (x, y), (self.thickness, CELL_SIZE) ))
        return rects
    
    def remove_walls(self, neighbour_row, neighbour_col):
        """
        Function that removes walls between neighbour cell given by indices in grid.

            Args:
                neighbour_row (int):
                neighbour_col (int):

            Return:
                True: If the operation was a success
                False: If the operation failed
                
        """

        if self.row - neighbour_row == 1:
            self.walls["top"] = False
            return True
        elif self.row - neighbour_row == -1:
            self.walls["bot"] = False
            return True
        elif self.col - neighbour_col == 1:
            self.walls["left"] = False
            return True
        elif self.col - neighbour_col == -1:
            self.walls["right"] = False
            return True
        
        return False
    
    def set_entry_exit(self, entry_exit, row_limit, col_limit):
        """
        Function that sets the cell as an entry/exit cell by disabling the outer boundary wall.
        First, we check if the entrance/exit is on the top row. Next, we check if it should
        be on the bottom row. Finally, we check if it is on the left wall or the bottom row.

        Args:
            entry_exit: True to set this cell as an exit/entry. False to remove it as one
            row_limit:
            col_limit:

        """
        if self.row == 0:
            self.walls["top"] = False
        elif self.row == row_limit:
            self.walls["bot"] = False
        elif self.col == 0:
            self.walls["left"] = False
        elif self.col == col_limit:
            self.walls["right"] = False

        self.is_entry_exit = entry_exit
    
    