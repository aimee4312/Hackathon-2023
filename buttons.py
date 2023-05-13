import pygame.font

class Button:
    def __init__(self, sw_settings, screen, msg):
        """Init button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimensions and properties of button