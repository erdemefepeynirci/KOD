import pygame
from Monster import Monster



class MonsterH(Monster):
    def __init__(self,loc_x,loc_y):

        self._mon_health = 5
        self._rect: pygame.Rect
        self._image = pygame.transform.scale(pygame.image.load("MonsterH.png"),(35,45))
        super().__init__(loc_x,loc_y)

    def here_is_mon_loc(self):
        return (self._loc_x,self._loc_y)

