import pygame
from time import sleep
from pygame.sprite import Sprite
from pygame import mixer
from assets import *

# Tower class
class Tower(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings
        self.image = pygame.image.load(TOWER)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting the size and location
        width = self.image.get_rect().width
        height = self.image.get_rect().height
        self.image = pygame.transform.scale(self.image, (int(width * 0.8), int(height * 0.8)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x = 5
        self.rect.y = 180
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

# Ship class
class Ship(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings
        self.image = pygame.image.load(SHIP)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting the size and location
        width = self.image.get_rect().width
        height = self.image.get_rect().height
        self.image = pygame.transform.scale(self.image, (int(width * 1.5), int(height * 1.5)))
        self.rect.x = 570
        self.rect.y = 120
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


# Laser class
class Laser(Sprite):
    def __init__(self, sw_settings, screen):
        self.screen = screen
        self.sw_settings = sw_settings
        self.left_laser = pygame.image.load(LZR_EYES)
        self.right_laser = pygame.image.load(LZR_EYES)
        self.laser_shot = pygame.image.load(LZR_SHOT)
        self.rect = self.left_laser.get_rect()
        self.screen_rect = screen.get_rect()
        self.laser_list = []

        # Setting the size and location
        width = self.left_laser.get_rect().width
        height = self.left_laser.get_rect().height
        self.laser_shot = pygame.transform.rotate(self.laser_shot, 60)
        self.left_laser = pygame.transform.scale(self.left_laser, (int(width * 0.5), int(height * 0.5)))
        self.right_laser = pygame.transform.scale(self.right_laser, (int(width * 0.5), int(height * 0.5)))
        self.right_laser = pygame.transform.flip(self.right_laser, True, False)
        self.rect.x = -45
        self.rect.y = 200

    def blitme(self):
        self.screen.blit(self.left_laser, self.rect)
        self.screen.blit(self.right_laser, self.rect)
        self.screen.blit(self.laser_shot, (-45, 50))
    
    def laser_sound(self):
        mixer.music.load(TOWER_LASER)
        mixer.music.set_volume(1)
        mixer.music.play()
    
    def laser_explosion(self):
        mixer.music.load(LZR_EXP)
        mixer.music.set_volume(1)
        mixer.music.play()
    
    def __del__(self):
        print()
    
