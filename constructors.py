from troop import Troop
from assets import *

#self, sw_settings, screen, health, speed, range, dps, image, isPlayer
def spawn_p_reg(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 100, 1, 20, 20, worth, A_WEAK, True)
    
def spawn_p_fast(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 40, 3, 20, 25, worth, A_FAST, True)

def spawn_p_range(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 80, 1, 150, 20, worth, A_RANGE, True)
    
def spawn_p_tank(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 240, .5, 20, 50, worth, A_TANK, True)
    
def spawn_np_reg(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 100, 1, 20, 20, worth, E_WEAK, False)
    
def spawn_np_fast(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 40, 3, 20, 25, worth, E_FAST, False)

def spawn_np_range(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 80, 1, 150, 20, worth, E_RANGE, False)
    
def spawn_np_tank(sw_settings, screen, worth):
    return Troop(sw_settings, screen, 240, .5, 20, 50, worth, E_TANK, False)