import pygame
from Monster import Monster



class MonsterS(Monster):
    def __init__(self,loc_x,loc_y):
        self._mon_speed = 3
        self._rect: pygame.Rect
        self._image = pygame.transform.scale(pygame.image.load("MonsterS.png"),(35,45))
        super().__init__(loc_x,loc_y)

    def here_is_mon_loc(self):
        return (self._loc_x,self._loc_y)
