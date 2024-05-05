import pygame
import constants
from save_load import saveloadsystem

WIDTH, HEIGHT = constants.SIZE
FPS = constants.FPS

saveloadmangager = saveloadsystem('.save', 'Do_an/SaveLoad')

def draw_window(screen):
    screen.fill(pygame.Color(constants.WHITE))
    pygame.display.update()

def draw_maze(maze, screen):
        """ This function use to draw maze on a screen """
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):    
                maze.grid[i][j].draw(screen)

def game(Maze = saveloadmangager.load('maze')):

    pygame.init()
    pygame.display.set_caption('Tam and Gia Huy')
    Screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    draw_window(Screen)
    draw_maze(Maze, Screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveloadmangager.save('maze', Maze)
                pygame.quit()
                quit()

        pygame.display.flip() 
        clock.tick(FPS)
        
        

