import pygame
from Buff import Buff

class BuffS(Buff):
    def __init__(self,loc_x,loc_y):
        #self.rect: pygame.Rect
        self.image = pygame.transform.scale(pygame.image.load("buffs.png"),(30,30)) 
        super().__init__(loc_x,loc_y)

    def affect(self,player):
        player.speed += 1.5
        start_time = pygame.time.get_ticks()
        if self.effect_time == pygame.time.get_ticks() - start_time:
            player.speed -= 1.5

    def increase_speed(self):
        pass