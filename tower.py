import pygame
from pygame.sprite import Sprite

# Tower class
class Tower(Sprite):
    def __init__(self, level):
        self.hp = 100
        self.level = level