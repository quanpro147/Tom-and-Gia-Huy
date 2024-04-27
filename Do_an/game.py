import pygame
from visual import draw_Maze
from maze import maze



def game():
    FPS = 60
    Maze = maze(10, 10)
    Maze = Maze.generate_maze()
    pygame.init()
    surface = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()
    run = True
    while run:
        surface.fill(pygame.Color('darkslategrey'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_Maze(Maze, surface)
        pygame.display.flip() 
        clock.tick(FPS)
        

