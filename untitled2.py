import pygame
from pygame.draw import *
import numpy as np
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 150 )
circle(screen, (255, 0, 0), (140, 150), 20)
circle(screen,(0, 0, 0), (143, 150), 10)
circle(screen, (255, 0, 0), (260, 150), 30)
circle(screen,(0, 0, 0), (256, 150), 10)

x = np.linspace(140, 260, 250)
print(x)
for i in x:
    circle(screen,(0, 0, 0),(int(i), int(280-150/(i-265))),2)
line(screen,(0, 0, 0), (100, 100),(180, 150), 15)
line(screen,(0, 0, 0), (300, 100), (200, 150), 10)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()