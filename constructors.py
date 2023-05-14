from troop import Troop
from assets import *

#self, sw_settings, screen, health, speed, range, dps, image, isPlayer
def spawn_p_reg(sw_settings, screen):
    return Troop(sw_settings, screen, 100, 1, 20, 20, ALIEN, True)
    
def spawn_p_fast(sw_settings, screen):
    return Troop(sw_settings, screen, 40, 3, 20, 25, ALIEN, True)

def spawn_p_range(sw_settings, screen):
    return Troop(sw_settings, screen, 80, 1, 150, 20, ALIEN, True)
    
def spawn_p_tank(sw_settings, screen):
    return Troop(sw_settings, screen, 240, .5, 20, 50, A_TANK, True)
    
def spawn_np_reg(sw_settings, screen):
    return Troop(sw_settings, screen, 100, 1, 20, 20, ALIEN, False)
    
def spawn_np_fast(sw_settings, screen):
    return Troop(sw_settings, screen, 40, 3, 20, 25, ALIEN, False)

def spawn_np_range(sw_settings, screen):
    return Troop(sw_settings, screen, 80, 1, 150, 20, ALIEN, False)
    
def spawn_np_tank(sw_settings, screen):
    return Troop(sw_settings, screen, 240, .5, 20, 50, ALIEN, False)