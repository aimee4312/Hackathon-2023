import pygame.font
from pygame.sprite import Sprite
from assets import *

class Button:
    def __init__(self, screen, msg):
        """Init button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dimensions and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Button rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button only prepped once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered img and center text"""    
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class spawnButtons(Sprite):
    def __init__(self, screen, type):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        match type:
            case "weak":
                self.image = pygame.image.load(AW_BUTTON)
                self.cost_msg("Cost: 25")
            case "fast":
                self.image = pygame.image.load(AF_BUTTON)
                self.cost_msg("Cost: 50")
            case "ranged":
                self.image = pygame.image.load(AR_BUTTON)
                self.cost_msg("Cost: 75")
            case "tank":
                self.image = pygame.image.load(AT_BUTTON)
                self.cost_msg("Cost: 100")
    
    def cost_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        

