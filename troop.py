import pygame
from pygame.sprite import Sprite

# Alien class
class Troop(Sprite):
    def __init__(self, sw_settings, screen):
        # Initialize the troop, and set its starting position.
        super(Troop, self).__init__()
        self.screen = screen
        self.sw_settings = sw_settings

        # Load the troop image, and get its rect.
        self.image = pygame.image.load("Sprites/basic_alien.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new troop at the ???bottom center??? of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the troop's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving = True

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Update the troop's position, based on movement flags
        # Update the ship's center value, not the rect.
        if self.moving:
            self.rect.centerx += 5

    def blitme(self):
        # Draw the troop at its current location.
        self.screen.blit(self.image, self.rect)