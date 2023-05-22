import pygame
from Monster import Monster


class MonsterD(Monster):
    def __init__(self,loc_x,loc_y,mon_speed,mon_health,mon_damage):
        self.rect: pygame.Rect
        self.image: pygame.Surface
        super().__init__(loc_x,loc_y,mon_speed,mon_health,mon_damage)
