import pygame
from pygame.sprite import Sprite

# Tower class
class Tower(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings

        self.image = pygame.image.load("Sprites/tower_l1.jpeg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Figure out where the tower should be
    def blitme(self):
        self.screen.blit(self.image, self.rect)