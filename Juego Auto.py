import pygame, random
from pygame.examples.video import backgrounds

pygame.init()

WIDTH = 800
HEIGHT = 600
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill (BLACK)





running  =  True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False                 # si ponemos TRUE  se cierra



