import pygame
from Monster import Monster


class MonsterD(Monster):
    def __init__(self,loc_x,loc_y,mon_health,mon_damage,mon_speed):
        self.rect: pygame.Rect
        self.image: pygame.Surface
        self.mon_damage = mon_damage
        super().__init__(loc_x,loc_y,mon_health,mon_speed)
