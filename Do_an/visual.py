import pygame
import constants

def draw_cell(_cell, surface):
        """ This function use to draw cell with 4 walls """

        x, y = _cell.x * constants.CELL_SIZE, _cell.y * constants.CELL_SIZE

        if _cell.walls['top']:
            pygame.draw.line(surface, pygame.Color('darkorange'), (x, y), (x + constants.CELL_SIZE, y), 4)
        if _cell.walls['right']:
            pygame.draw.line(surface, pygame.Color('darkorange'), (x + constants.CELL_SIZE, y), (x + constants.CELL_SIZE, y + constants.CELL_SIZE), 4)
        if _cell.walls['bot']:
            pygame.draw.line(surface, pygame.Color('darkorange'), (x + constants.CELL_SIZE, y + constants.CELL_SIZE), (x , y + constants.CELL_SIZE), 4)
        if _cell.walls['left']:
            pygame.draw.line(surface, pygame.Color('darkorange'), (x, y + constants.CELL_SIZE), (x, y), 4)

def draw_maze(maze, surface):
        """ This function use to draw maze on a surface """
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):    
                draw_cell(maze.grid[i][j], surface)
    



