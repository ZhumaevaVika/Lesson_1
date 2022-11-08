import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((192, 192, 192))
'''
rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
'''
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 1)

circle(screen, (255, 0, 0), (160, 150), 23)
circle(screen, (255, 0, 0), (240, 150), 16)
circle(screen, (0, 0, 0), (160, 150), 16)
circle(screen, (0, 0, 0), (240, 150), 10)

#rect(screen, (0, 0, 0), (100, 100, 100, 12))
#rect(screen, (0, 0, 0), (200, 100, 100, 12))
rect(screen, (0, 0, 0), (150, 200, 100, 20))

line(screen, (0, 0, 0), (120, 100), (190, 150), 15)
line(screen, (0, 0, 0), (290, 100), (220, 150), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()