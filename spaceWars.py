import pygame
from time import sleep
from pygame import mixer
from pygame.locals import *

from settings import Settings
from tower import Ship
from tower import Tower
from tower import Laser
from computer_play import Enemy_ai
from computer_play import Enemy_ai
from game_stats import GameStats
from button import Button
from button import spawnButtons
from currency_display import CurrencyDisplay
from value_display import ValueDisplay
from constructors import *
from assets import *

laser_use = True
def _check_play_button(mouse_pos):
    """Start new game when player clicks Play"""
    play_button_clicked = play_button.rect.collidepoint(mouse_pos)

    wcollision_rect = pygame.Rect(wButton.rect.left - 90, wButton.rect.top - 90, wButton.rect.width - 90, wButton.rect.height - 90)
    fcollision_rect = pygame.Rect(fButton.rect.left - 90, fButton.rect.top - 90, fButton.rect.width - 90, fButton.rect.height - 90)
    rcollision_rect = pygame.Rect(rButton.rect.left - 90, rButton.rect.top - 90, rButton.rect.width - 90, rButton.rect.height - 90)
    tcollision_rect = pygame.Rect(tButton.rect.left - 90, tButton.rect.top - 90, tButton.rect.width - 90, tButton.rect.height - 90)
    #lcollision_rect = pygame.Rect(lButton.rect.left - 90, lButton.rect.top - 90, lButton.rect.width - 90, lButton.rect.height - 90)

    aw_button_clicked = wcollision_rect.collidepoint(mouse_pos)
    af_button_clicked = fcollision_rect.collidepoint(mouse_pos)
    ar_button_clicked = rcollision_rect.collidepoint(mouse_pos)
    at_button_clicked = tcollision_rect.collidepoint(mouse_pos)
    #lzr_button_clicked = lcollision_rect.collidepoint(mouse_pos)
    if play_button_clicked and not stats.game_active:
        # Reset stats
        stats.reset_stats()
        stats.game_active = True

        # TODO: get rid of troops and create new aliens?

        # # Hides mouse cursor
        # # pygame.mouse.set_visible(False)
        
        # Sets passive income generation timer
        pygame.time.set_timer(sw_settings.passive_income_event_id, sw_settings.passive_income_interval)
    elif aw_button_clicked and stats.currency >= 25:
        a = spawn_p_reg(sw_settings, screen, sw_settings.reg_cost / 2)
        ally_troops.append(a)
        stats.currency -= sw_settings.reg_cost
    elif af_button_clicked and stats.currency >= 50:
        a = spawn_p_fast(sw_settings, screen, sw_settings.fast_cost / 2)
        ally_troops.append(a)
        stats.currency -= sw_settings.fast_cost
    elif ar_button_clicked and stats.currency >= 75:
        a = spawn_p_range(sw_settings, screen, sw_settings.range_cost / 2)
        ally_troops.append(a)
        stats.currency -= sw_settings.range_cost
    elif at_button_clicked and stats.currency >= sw_settings.tank_cost:
        a = spawn_p_tank(sw_settings, screen, sw_settings.tank_cost / 2)
        ally_troops.append(a)
        stats.currency -= sw_settings.tank_cost
    # elif lzr_button_clicked and stats.currency >= sw_settings.laser_cost and laser_use == True:
    #     laser.blitme()
    #     laser.laser_sound()
    #     sleep(0.5)
    #     laser.laser_explosion()
    #     laser_use = False

        


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

# Time and Clock
clock = pygame.time.Clock

# Enemy Spawn AI
enemy_ai = Enemy_ai()
interval = enemy_ai.interval * 1000 # 1000 milliseconds = 1s
nme_event_id = pygame.USEREVENT+1
pygame.time.set_timer(nme_event_id, interval)

# Spawned Troops
ally_troops = []
enemy_troops = []
ally_attacking_troops = []
enemy_attacking_troops = []

#test_troop = Troop(sw_settings, screen)

# Ally and enemy bases
laser = Laser(sw_settings, screen)
tower = Tower(sw_settings, screen)
ship = Ship(sw_settings, screen)

# Spawn Buttons
wButton = spawnButtons(screen, sw_settings, "weak")
fButton = spawnButtons(screen, sw_settings, "fast")
rButton = spawnButtons(screen, sw_settings, "ranged")
tButton = spawnButtons(screen, sw_settings, "tank")
lButton = spawnButtons(screen, sw_settings, "laser")

# List of spawn buttons for my convenience
spawn_buttons = [wButton, fButton, rButton, tButton]

# Tower Health Displays
tower_health_display = ValueDisplay(sw_settings, screen, stats, tower.health)
ship_health_display = ValueDisplay(sw_settings, screen, stats, ship.health)

# Play Button
play_button = Button(screen, "Play")


gameover = False
running = True

while running:
    
    screen.fill(sw_settings.bg_color)
    screen.blit(background, (0, 0))

    tower.blitme()
    ship.blitme()
    
    # Draw currency info
    currency_display.show_currency()

    # Draw play button if inactive game
    if not stats.game_active:
        play_button.draw_button()
    else:
        for button in spawn_buttons:
            button.blitme()
    

    
    for event in pygame.event.get():
        # close the game when close button is clicked
        if event.type == pygame.QUIT:
            running = False
        # Player Controls
        # Each button corresponds to a specific unit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                stats.currency += 100
            
            # summon units
            if event.key == pygame.K_1 and stats.currency >= sw_settings.reg_cost: # summon reg units
                a = spawn_p_reg(sw_settings, screen, sw_settings.reg_cost / 2)
                ally_troops.append(a)
                stats.currency -= sw_settings.reg_cost
            if event.key == pygame.K_2 and stats.currency >= sw_settings.fast_cost: # summon unit
                a = spawn_p_fast(sw_settings, screen, sw_settings.fast_cost / 2)
                ally_troops.append(a)
                stats.currency -= sw_settings.fast_cost
            if event.key == pygame.K_3 and stats.currency >= sw_settings.range_cost: # summon stronk unit
                a = spawn_p_range(sw_settings, screen, sw_settings.range_cost / 2)
                ally_troops.append(a)
                stats.currency -= sw_settings.range_cost
            if event.key == pygame.K_4 and stats.currency >= sw_settings.tank_cost: # summon tank
                a = spawn_p_tank(sw_settings, screen, sw_settings.tank_cost / 2)
                ally_troops.append(a)
                stats.currency -= sw_settings.tank_cost
            if event.key == pygame.K_SPACE and stats.currency >= sw_settings.laser_cost: # summon laser (CURRENTLY DOESNT WORK)
                if laser_use == True:
                    laser.blitme()
                    laser.laser_sound()
                    sleep(0.5)
                    laser.laser_explosion()
                    laser_use = False
        

        # free money baybee
        elif event.type == sw_settings.passive_income_event_id:
            stats.currency += stats.passive_income_rate
            currency_display.prep_amount()

        # enemy spawn
        elif event.type == nme_event_id:
            e = enemy_ai.get_next_troop
            enemy_troops.append(e)
        
        # click buttons        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            _check_play_button(mouse_pos)

        

    
    if not gameover:
        # update state of troops          
        for troop in ally_troops:
            ally_attacking_troops = troop.update(target_enemy, ally_attacking_troops)
        for troop in enemy_troops:
            pass
            #enemy_attacking_troops = troop.update(target_user, enemy_attacking_troops)
            
        # combat ai
        if enemy_troops:
            #target_enemy = min(enemy_troops, key=lambda x: x.rect.centerx)
            print(target_enemy)
        else:
            target_enemy = 0
        if ally_troops:
            target_user = max(ally_troops, key=lambda x: x.rect.centerx)
        else: target_user = 0  
                
    
    pygame.display.flip()
    #pygame.display.update()
#run_game()