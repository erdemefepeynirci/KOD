import pygame
from Buff import Buff

class BuffH(Buff):
    def __init__(self,loc_x,loc_y):
       # self.rect: pygame.Rect
        self._image = pygame.transform.scale(pygame.image.load("buffh.png"),(30,30)) 
        super().__init__(loc_x,loc_y)

    def affect(self,player):
        player.increase_life()