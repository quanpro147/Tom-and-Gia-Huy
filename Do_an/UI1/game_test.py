
# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the line
while True:
    for event in pygame.event.get():
                        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.line(window, 'black',(100, 200),(50,50),1)
    pygame.display.update()

# Draws the surface object to the screen.
