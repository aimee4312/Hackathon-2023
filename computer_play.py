import pygame
import random

class enemy_ai():
    def __init__(self, clock):
        self.clock = clock
        self.wave = 1
        self.interval = 7
    
    #ez_q      
    #def spawn_random(self):
        