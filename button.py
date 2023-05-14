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
    def __init__(self, screen, sw_settings ,type):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = (255, 255, 255)

       

        match type:
            case "weak":
                self.image = pygame.image.load(AW_BUTTON)
                self.rect = self.image.get_rect()
                width = self.image.get_rect().width
                height = self.image.get_rect().height
                self.image = pygame.transform.scale(self.image, (int(width * 0.5), int(height * 0.5)))
                self.rect.x = 0
                self.msgx = 10
                self.msgy = 10
                self.cost_msg("1. Cost: " + str(sw_settings.reg_cost))
            case "fast":
                self.image = pygame.image.load(AF_BUTTON)
                self.rect = self.image.get_rect()
                width = self.image.get_rect().width
                height = self.image.get_rect().height
                self.image = pygame.transform.scale(self.image, (int(width * 0.5), int(height * 0.5)))
                self.rect.x = 130
                self.msgx = 140
                self.msgy = 10
                self.cost_msg("2. Cost: " + str(sw_settings.fast_cost))
            case "ranged":
                self.image = pygame.image.load(AR_BUTTON)
                self.rect = self.image.get_rect()
                width = self.image.get_rect().width
                height = self.image.get_rect().height
                self.image = pygame.transform.scale(self.image, (int(width * 0.5), int(height * 0.5)))
                self.rect.x = 260
                self.msgx = 270
                self.msgy = 10
                self.cost_msg("3. Cost: " + str(sw_settings.range_cost))
            case "tank":
                self.image = pygame.image.load(AT_BUTTON)
                self.rect = self.image.get_rect()
                width = self.image.get_rect().width
                height = self.image.get_rect().height
                self.image = pygame.transform.scale(self.image, (int(width * 0.5), int(height * 0.5)))
                self.rect.x = 390
                self.msgx = 400
                self.msgy = 10
                self.cost_msg("4. Cost: " + str(sw_settings.tank_cost))
            case "laser":
                self.image = pygame.image.load(LZR_BUTTON)
                self.rect = self.image.get_rect()
                width = self.image.get_rect().width
                height = self.image.get_rect().height
                self.image = pygame.transform.scale(self.image, (int(width * 0.3), int(height * 0.3)))
                self.rect.x = 178
                self.rect.y = 300
                self.msgx = 190
                self.msgy = 310
                self.cost_msg("Cost: " + str(sw_settings.laser_cost))
    
    def cost_msg(self, msg):
        if msg == "Cost: 400":
            self.font = pygame.font.SysFont(None, 20)
            self.cost = self.font.render(msg, True, (0,0,0))
        else:
            self.cost = self.font.render(msg, True, (0,0,0))
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.cost, (self.msgx, self.msgy))

        

