import pygame
from pygame import mixer

import assets

from settings import Settings
from troop import Troop
from tower import Ship
from tower import Tower
from tower import Laser
from game_stats import GameStats
from button import Button


def _check_play_button(mouse_pos):
    """Start new game when player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not stats.game_active:
        # Reset stats
        stats.reset_stats()
        stats.game_active = True

        # TODO: get rid of troops and create new aliens?


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


# Background
background = pygame.image.load('Sprites/background.png')

# Background sound
mixer.music.load('Sounds/background_sound.ogg')
mixer.music.set_volume(6)
mixer.music.play(-1)


# Enemies
enemyImg = []
enemyX = []
enemyX_change = []

#for i in range(num_of_enemies):
#    enemyImg.append(pygame.image.load('alien.png'))
#    enemyX.append(random.randint(0, 735))
#    enemyX_change.append(2)

#test_troop = Troop(sw_settings, screen)

# Play Button
play_button = Button(screen, "Play")

gameover = False
running = True
while running:

    screen.fill(sw_settings.bg_color)
    screen.blit(background, (0, 0))
    
    tower = Tower(sw_settings, screen)
    tower.blitme()

    ship = Ship(sw_settings, screen)
    ship.blitme()

    #test_troop.blitme()
    #test_troop.update()

    # Draw play button if inactive game
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

    for event in pygame.event.get():
        # close the game when close button is clicked
        if event.type == pygame.QUIT:
            running = False
        # Player Controls
        # Each button corresponds to a specific unit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: # summon reg unit
                pass
            if event.key == pygame.K_2: # summon  unit
                pass
            if event.key == pygame.K_3: # summon stronk unit
                pass
            if event.key == pygame.K_4: # summon tank
                pass 
            if event.key == pygame.K_SPACE: # summon laser
                laser = Laser(sw_settings, screen)
                laser.blitme()
                end_time = pygame.time.get_ticks() + 200
                current_time = pygame.time.get_ticks()
                if current_time > end_time:
                    laser.kill()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            _check_play_button(mouse_pos)

    
    if not gameover:
        # game stuff           
        pass
    
    
    
    #pygame.display.update()

#run_game()