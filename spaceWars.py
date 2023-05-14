import pygame
from time import sleep
from pygame import mixer
from pygame.locals import *

from settings import Settings
from troop import Troop
from tower import Ship
from tower import Tower
from tower import Laser
from game_stats import GameStats
from button import Button
from currency_display import CurrencyDisplay
from constructors import *
from assets import *


def _check_play_button(mouse_pos):
    """Start new game when player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not stats.game_active:
        # Reset stats
        stats.reset_stats()
        stats.game_active = True

        # TODO: get rid of troops and create new aliens?

        # Hides mouse cursor
        pygame.mouse.set_visible(False)
        
        # Sets passive income generation timer
        pygame.time.set_timer(sw_settings.passive_income_event_id, sw_settings.passive_income_interval)


# def run_game():
# Always the first step in using pygame
pygame.init()

#Initializes settings
sw_settings = Settings()

# Creates an 800 x 600 p screen for the game
screen = pygame.display.set_mode((sw_settings.screen_width, sw_settings.screen_height))

# Set name and icon
pygame.display.set_caption("Space Wars")
#icon = pygame.image.load('spaceship.png')
#pygame.display.set_icon(icon)

# Stats
stats = GameStats(sw_settings)
currency_display = CurrencyDisplay(sw_settings, screen, stats)


# Background
background = pygame.image.load(BG_IMG)

# Background sound
pygame.mixer.Channel(0).play(pygame.mixer.Sound(BG_MUSIC), loops = -1)
pygame.mixer.Channel(0).set_volume(6)

# Spawned Troops
ally_troops = []
enemy_troops = []
ally_attacking_troops = []
enemy_attacking_troops = []

#for i in range(num_of_enemies):
#    enemyImg.append(pygame.image.load('alien.png'))
#    enemyX.append(random.randint(0, 735))
#    enemyX_change.append(2)

#test_troop = Troop(sw_settings, screen)


# Play Button
play_button = Button(screen, "Play")


gameover = False
running = True
laser_use = True
while running:
    
    screen.fill(sw_settings.bg_color)
    screen.blit(background, (0, 0))

    laser = Laser(sw_settings, screen)
    tower = Tower(sw_settings, screen)
    tower.blitme()

    ship = Ship(sw_settings, screen)
    ship.blitme()

    # Draw currency info
    currency_display.show_currency()

    # Draw play button if inactive game
    if not stats.game_active:
        play_button.draw_button()

    if enemy_troops:
        target_enemy = min(enemy_troops, key=lambda x: x.rect.centerx)
        print(target_enemy)
    else:
        target_enemy = 0
    if ally_troops:
        target_user = max(ally_troops, key=lambda x: x.rect.centerx)
    else: target_user = 0

    for event in pygame.event.get():
        # close the game when close button is clicked
        if event.type == pygame.QUIT:
            running = False
        # Player Controls
        # Each button corresponds to a specific unit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                stats.currency += 100
            if event.key == pygame.K_1 and stats.currency >= 10: # summon reg units
                #make conditional if currency > cost
                a = spawn_p_reg(sw_settings, screen)
                ally_troops.append(a)
                stats.currency -= 25
            if event.key == pygame.K_2 and stats.currency >= 20: # summon  unit
                spawn_p_fast(sw_settings, screen)
                stats.currency -= 75
            if event.key == pygame.K_3 and stats.currency >= 40: # summon stronk unit
                spawn_p_range(sw_settings, screen)
                stats.currency -= 200
            if event.key == pygame.K_4 and stats.currency >= 80: # summon tank
                spawn_p_tank(sw_settings, screen)
                stats.currency -= 150
            if event.key == pygame.K_SPACE and stats.currency >= 400: # summon laser (CURRENTLY DOESNT WORK)
                if laser_use == True:
                    laser.blitme()
                    laser.laser_sound()
                    sleep(0.5)
                    laser.laser_explosion()
                    laser_use = False
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            _check_play_button(mouse_pos)

        elif event.type == sw_settings.passive_income_event_id:
            stats.currency += stats.passive_income_rate
            currency_display.prep_amount()
        

    if not gameover:
        # game stuff           
        for troop in ally_troops:
            ally_attacking_troops = troop.update(target_enemy, ally_attacking_troops)
        for troop in enemy_troops:
            enemy_attacking_troops = troop.update(target_user, enemy_attacking_troops)
            
    
    
    pygame.display.flip()
    #pygame.display.update()
#run_game()