import pygame
import os
import constants

class player():
    def __init__(self, maze):
        img = pygame.image.load(os.path.join('Assets', 'Tom_image.webp'))
        self.img = pygame.transform.rotate(pygame.transform.scale(img, (40, 40)), 180)
        self.speed = 5
        self.size = constants.CELL_SIZE
        self.rect = self.get_rect(maze)
        self.x = self.rect.x
        self.y = self.rect.y

    @staticmethod
    def get_start_pos(maze):
        """ This funtion return the start position of the player """
        y_start, x_start = maze.start
        return x_start*constants.CELL_SIZE, y_start*constants.CELL_SIZE
    
    @staticmethod
    def get_rect(maze):
        return pygame.Rect(player.get_start_pos(maze)[0], player.get_start_pos(maze)[1], 
                         constants.CELL_SIZE, constants.CELL_SIZE)