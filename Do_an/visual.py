import pygame

WIDTH, HEIGHT = 1202, 1002
RES = 1002
CELL_SIZE = RES//(10)
  
def draw_cell(_cell, surface):
    """ This function use to draw cell with 4 walls """

    x, y = _cell.row * CELL_SIZE, _cell.y * CELL_SIZE

    if _cell.walls['top']:
        pygame.draw.line(surface, pygame.Color('darkorange'), (x, y), (x + CELL_SIZE, y), _cell.thickness)
    if _cell.walls['right']:
        pygame.draw.line(surface, pygame.Color('darkorange'), (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), _cell.thickness)
    if _cell.walls['bot']:
        pygame.draw.line(surface, pygame.Color('darkorange'), (x + CELL_SIZE, y + CELL_SIZE), (x , y + CELL_SIZE), _cell.thickness)
    if _cell.walls['left']:
        pygame.draw.line(surface, pygame.Color('darkorange'), (x, y + CELL_SIZE), (x, y), _cell.thickness)

def get_rects(_cell):

    rects = []
    x, y = _cell.row * CELL_SIZE, _cell.col * CELL_SIZE
    if _cell.walls['top']:
        rects.append(pygame.Rect( (x, y), (CELL_SIZE, _cell.thickness) ))
    if _cell.walls['right']:
        rects.append(pygame.Rect( (x + CELL_SIZE, y), (_cell.thickness, CELL_SIZE) ))
    if _cell.walls['bot']:
        rects.append(pygame.Rect( (x, y + CELL_SIZE), (CELL_SIZE , _cell.thickness) ))
    if _cell.walls['left']:
        rects.append(pygame.Rect( (x, y), (_cell.thickness, CELL_SIZE) ))
    return rects

def draw_Maze(maze):
    for i in range(maze.num_rows):
        for j in range(maze.num_cols):
            draw_cell(maze.grid[i][j])


