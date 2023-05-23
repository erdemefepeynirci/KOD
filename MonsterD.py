import pygame
from Monster import Monster


class MonsterD(Monster):
    def __init__(self,loc_x,loc_y):

        self.mon_damage = 2
        self.rect: pygame.Rect
        self.image = pygame.transform.scale(pygame.image.load("monsterD.png"),(35,45))
        self.mon_damage = 2
        super().__init__(loc_x,loc_y)


    def here_is_mon_loc(self):
        return (self.loc_x,self.loc_y)
    

    def affect(self,player):
        player.lose_life(2)
