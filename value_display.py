import pygame.font

class ValueDisplay:
    """Class that displays the entered value"""

    def __init__(self, sw_settings, screen, stats, value, x, y):
        """Initializing value display attributes""" 
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sw_settings
        self.stats = stats
        self.value = value
        self.x = x
        self.y = y

        # Font settings
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont('bahnschrift', 36)

        # Prep initial currency image
        self.prep_value()


    def prep_value(self):
        """Turn value into rendered img"""
        value_str = str(self.value)
        self.value_image = self.font.render(value_str, True, self.text_color, self.settings.bg_color)

        # Default loc score at top right
        self.value_rect = self.value_image.get_rect()
        self.value_rect.x = self.x
        self.value_rect.y = self.y

    def show_value(self):
        """Draw value amount to screen"""
        self.screen.blit(self.value_image, self.value_rect)


