# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:35:20 2020

@author: dege-
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 200
screen = pygame.display.set_mode((1200, 600)) 

class Manager():
    def __init__(self):
        self.gun = Gun()
        self.score_t = Table()
    def draw(self, screen):
        screen.fill(BLACK)
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        return done
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True 
        return done
                
class gun():
    pass 

class Table():
    pass

mgr = Manager()

done = False

while not done :
    mgr.process(pygame.event.get(), screen)

    pygame.display.flip()

pygame.quit()