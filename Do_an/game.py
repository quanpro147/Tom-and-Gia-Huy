import pygame
from visual import *
import constants
from player import player

WIDTH, HEIGHT = constants.SIZE
FPS = constants.FPS

def draw_window(screen, player, maze):
    rect = player.get_rect(maze)
    screen.fill(pygame.Color(constants.WHITE))
    screen.blit(player.img, (rect.x, rect.y))
    pygame.display.update()

def game(Maze):

    pygame.init()
    pygame.display.set_caption('Tam and Gia Huy')
    Screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    Player = player(Maze)
    
    run = True
    while run:
        clock.tick(FPS)
        draw_window(Screen, Player, Maze)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Player.x += 1
        draw_maze(Maze, Screen)
        pygame.display.update()
        pygame.display.flip() 
        
        

