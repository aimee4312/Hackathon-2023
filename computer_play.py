import pygame
import random
from constructors import *
from queue import Queue

# 1 = reg, 2 = fast, 3 = range, 4 = tank
    
ez_q1 = Queue(5)
ez_q1.put(1)
ez_q1.put(1)
ez_q1.put(1)
ez_q1.put(3)
ez_q1.put(1)

ez_q2 = Queue(5)
ez_q2.put(1)
ez_q2.put(1)
ez_q2.put(2)
ez_q2.put(1)
ez_q2.put(1)

ez_q3 = Queue(5)
ez_q3.put(1)
ez_q3.put(1)
ez_q3.put(2)
ez_q3.put(3)
ez_q3.put(1)

med_q1 = Queue(7)
med_q1.put(1)
med_q1.put(2)
med_q1.put(4)
med_q1.put(2)
med_q1.put(3)
med_q1.put(1)
med_q1.put(3)

med_q2 = Queue(7)
med_q2.put(1)
med_q2.put(2)
med_q2.put(3)
med_q2.put(1)
med_q2.put(2)
med_q2.put(1)
med_q2.put(4)

med_q3 = Queue(7)
med_q3.put(3)
med_q3.put(4)
med_q3.put(1)
med_q3.put(2)
med_q3.put(1)
med_q3.put(2)
med_q3.put(1)

hard_q1 = Queue(7)
hard_q1.put(2)
hard_q1.put(4)
hard_q1.put(2)
hard_q1.put(3)
hard_q1.put(2)
hard_q1.put(2)
[2, 4, 2, 3, 2, 1, 4]
hard_q2 = [4, 2, 3, 4, 3, 1, 2]
hard_q3 = [2, 2, 2, 4, 4, 3, 3]

ez_qs = [ez_q1, ez_q2, ez_q3]
med_qs = [med_q1, med_q2, med_q3]
hard_qs = [hard_q1, hard_q2, hard_q3] 

class Enemy_ai():
    def __init__(self, clock):
        self.clock = clock
        self.wave = 1
        self.interval = 7
        self.stage = 1
        self.current_q = []
           
      
    def get_random_q(self):
        rand = random.randint(0, 2)
        difficulty = self.stage % 5
        
        if difficulty == 1: 
            self.current_q = ez_qs[rand]
        elif difficulty == (2 or 3 or 5): 
            self.current_q = med_qs[rand]
        else: 
            self.current_q = hard_qs[rand]
            
    def get_next_troop(self):
        num = self.current_q.pop
        
        #if self.current_q.empty()
        
        match num:
            case 1:
                return spawn_np_reg()
            case 2:
                return spawn_np_fast()
            case 3:
                return spawn_np_range()
            case 4:
                return spawn_np_tank()
                