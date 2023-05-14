import pygame
import random

class enemy_ai():
    def __init__(self, clock):
        self.clock = clock
        self.currency = 0
        self.interval = 7
          
    def spawn_random(self):
        if self.currency >= 100:
            max = 4
        elif self.currency >= 75:
            pass