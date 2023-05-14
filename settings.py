import pygame

class Settings:
    # A class to store all settings 

    def __init__(self):
        # Initialize the game's static settings
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0) #change bg color


        # Currency Settings
        self.passive_income_interval = 1000; # 1 second
        self.passive_income_event_id = pygame.USEREVENT

        # # Alien settings.
        # self.fleet_drop_speed = 10
        self.reg_cost = 25
        self.fast_cost = 50
        self.range_cost = 75
        self.tank_cost = 100
        self.laser_cost = 400

        # Tower Settings
        self.tower_max_health = 1000
        self.ship_max_health = 1000
        
        self.tower_health_counter_x = 65
        self.tower_health_counter_y = 150

        self.ship_health_counter_x = 665
        self.ship_health_counter_y = 110

        # # How quickly the game speeds up.
        # self.speedup_scale = 1.1
        # # How quickly the alien point values increase.
        # self.score_scale = 1.5

        # self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game

        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        # Increase speed settings and alien point values 
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
