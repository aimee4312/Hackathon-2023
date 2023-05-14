class GameStats:
    """Tracks stats for Space Wars"""

    def __init__(self, sw_settings):
        """Init stats"""
        self.sw_settings = sw_settings
        self.reset_stats()

        # Game isn't active until the play button is pressed
        self.game_active = False

        # Currency gained per second
        self.passive_income_rate = 5


    def reset_stats(self):
        """Init stats"""
        self.currency = 0
        self.level = 1