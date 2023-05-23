import pygame
from Buff import Buff
from Bullet import Bullet

class BuffD(Buff):
    def __init__(self,loc_x,loc_y):
        #self.rect: pygame.Rect
        self.image = pygame.transform.scale(pygame.image.load("buffd.png"),(30,30))
        # self.buffd_bool= False
        super().__init__(loc_x,loc_y)

    def affect(self,player):
        Bullet.damage = 2
        start_time = pygame.time.get_ticks()
        if self.effect_time == pygame.time.get_ticks() - start_time:
            Bullet.damage = 1
        # self.buffd_bool=True

    def increase_damage(self):
        pass