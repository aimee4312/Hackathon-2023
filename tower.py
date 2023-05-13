import pygame
from pygame.sprite import Sprite

# Tower class
class Tower(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings
        self.image = pygame.image.load("Sprites/tower.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        width = self.image.get_rect().width
        height = self.image.get_rect().height
        self.image = pygame.transform.scale(self.image, (int(width * 0.8), int(height * 0.8)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x = 5
        self.rect.y = 180
        
        # Figure out where the tower should be
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Ship(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings
        self.image = pygame.image.load("Sprites/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        width = self.image.get_rect().width
        height = self.image.get_rect().height
        self.image = pygame.transform.scale(self.image, (int(width * 1.5), int(height * 1.5)))
        self.rect.x = 570
        self.rect.y = 120
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Laser(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings
        self.left_laser = pygame.image.load("Sprites/laser eyes.png")
        self.right_laser = pygame.image.load("Sprites/laser eyes.png")
        self.rect = self.left_laser.get_rect()
        self.screen_rect = screen.get_rect()
        width = self.left_laser.get_rect().width
        height = self.left_laser.get_rect().height
        self.left_laser = pygame.transform.scale(self.left_laser, (int(width * 0.5), int(height * 0.5)))
        self.right_laser = pygame.transform.scale(self.right_laser, (int(width * 0.5), int(height * 0.5)))
        self.right_laser = pygame.transform.flip(self.right_laser, True, False)
        self.rect.x = -45
        self.rect.y = 200

    def blitme(self):
        self.screen.blit(self.left_laser, self.rect)
        self.screen.blit(self.right_laser, self.rect)