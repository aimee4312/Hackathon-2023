import pygame.font

class CurrencyDisplay:
    """Class that displays the current currency amount"""

    def __init__(self, sw_settings, screen, stats):
        """Initializing currency display attributes""" 
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sw_settings
        self.stats = stats

        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prep initial currency image
        self.prep_amount()


    def prep_amount(self):
        """Turn currency amount into rendered img"""
        currency_str = str(self.stats.currency)
        self.currency_image = self.font.render(currency_str, True, self.text_color, self.settings.bg_color)

        # Display score at top left
        self.currency_rect = self.currency_image.get_rect()
        self.currency_rect.left = self.screen_rect.left + 20
        self.currency_rect.top = 20

    def show_currency(self):
        """Draw currency amount to screen"""
        self.screen.blit(self.currency_image, self.currency_rect)


