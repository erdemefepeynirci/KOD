import pygame
from Monster import Monster



class MonsterS(Monster):
    def __init__(self,loc_x,loc_y,mon_speed,mon_health,mon_damage):
        self.rect: pygame.Rect
        self.image: pygame.Surface
        self.mon_speed = mon_speed
        super().__init__(loc_x,loc_y,mon_health,mon_damage)
