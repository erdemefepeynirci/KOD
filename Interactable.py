import pygame

class Interactable:
    def __init__(self,locx,locy):
        self._loc_x = locx
        self._loc_y = locy


    def is_interacted(self,locx,locy):
        if (locx>self._loc_x-15 and locx<=self._loc_x+15) and (locy>self._loc_y-15 and locy<=self._loc_y+15):
            return True
        else:
            return False
        
        
    def draw(self,screen: pygame.Surface):
        screen.blit(self._image,(self._loc_x,self._loc_y))

    # def affect(self,key_number):
    #     pass



