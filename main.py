import pygame
from pygame import mixer

# Always the first step in using pygame
pygame.init()

# Creates an 800 x 600 p screen for the game
screen = pygame.display.set_mode((800, 600))

# Set name and icon
pygame.display.set_caption("Space Wars")
#icon = pygame.image.load('spaceship.png')
#pygame.display.set_icon(icon)


# Background
# background = pygame.image.load('background.png')

# Background sound
mixer.music.load("alien swamp.ogg")
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



def win_con():
    pass

gameover = False
running = True
while running:
    screen.fill((0, 0, 0))
    # screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        # close the game when close button is clicked
        if event.type == pygame.QUIT:
            running = False

        # Player Controls
        # Each button corresponds to a specific unit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: # summon weak unit
                pass
            if event.key == pygame.K_2: # summon mid unit
                pass
            if event.key == pygame.K_3: # summon stronk unit
                pass
    
    if not gameover:
        # game stuff           
        pass
    
    
    
    pygame.display.update()