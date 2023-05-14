import pygame
from pygame.sprite import Sprite
from assets import *

# Alien class
class Troop(Sprite):
    def __init__(self, sw_settings, screen, health, speed, range, dps, worth, image, isPlayer):
        # Initialize the troop, and set its starting position.
        super(Troop, self).__init__()
        self.screen = screen
        self.sw_settings = sw_settings

        # Load the troop image, and get its rect.
        if image == A_RANGE:
            self.image = pygame.image.load(image)
            width = self.image.get_rect().width
            height = self.image.get_rect().height
            self.image = pygame.transform.scale(self.image, (int(width * 0.2), int(height * 0.2)))
        else:
            self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new troop at the ???bottom center??? of the screen.
        self.rect.centerx = 150
        if not isPlayer:
            self.rect.centerx = sw_settings.screen_width - 150
        self.rect.centery = sw_settings.screen_height - 75
        

        # Store a decimal value for the troop's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving = True 
        self.count = 0
        
        # initialize stats
        self.isPlayer = isPlayer
        self.health = health
        self.speed = speed
        self.dps = dps
        self.worth = worth
        self.range = range
        if not isPlayer:
            self.range *= -1
         
    
    def check_collisions(self, enemy):
        rad = self.rect.centerx + self.range
        if self.isPlayer:
            return (rad - enemy.rect.centerx) >= 0
        else:
            return (rad - enemy.rect.centerx) <= 0
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # Checks if the troops right is greater than the screen right
        # meaning that it's passed the screen 
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self, enemy, attacking_list):
        # Update the troop's movement and existence
        self.blitme()
        if enemy and self.check_collisions(enemy):
            if self.moving:
                attacking_list.append(self)
                self.moving = False
        else:
            self.rect.centerx += self.speed
        return attacking_list


    def blitme(self):
        # Draw the troop at its current location.
        self.screen.blit(self.image, self.rect)
    

def deal_damage(user_attack_list, enemy_attack_list, user_list, enemy_list, user_target, enemy_target):
    user_damage_total = 0
    for troop in user_attack_list:
        user_damage_total += troop.dps
    enemy_damage_total = sum(troop.dps for troop in enemy_attack_list)
    user_target.health -= enemy_damage_total
    enemy_target.health -= user_damage_total
    if user_target.health <= 0:
        if user_target in user_attack_list:
            user_attack_list.remove(user_target)
        user_list.remove(user_target)
    if enemy_target.health <= 0:
        if enemy_target in enemy_attack_list:
            enemy_attack_list.remove(enemy_target)
        enemy_list.remove(enemy_target)
    return user_attack_list, enemy_attack_list, user_list, enemy_list
