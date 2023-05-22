import pygame

class Interactable:
    def __init__(self,locx,locy):
        self.rect: pygame.Rect  
        self.loc_x = locx
        self.loc_y = locy


    def is_interacted(self,locx,locy):
        if locx>self.loc_x-15 and locx<=self.loc_x+15 and locy>self.loc_y-15 and locy<=self.loc_y+15:
            return True
        else:
            return False
        
    def create(self,locx,locy,image,height,width):
        self.image = pygame.transform.scale(pygame.image.load(image),(height,width))
        self.loc_x = locx
        self.loc_y = locy
        
    def draw(self,screen: pygame.Surface):
        screen.blit(self.image,(self.loc_x,self.loc_y))

    # def affect(self,key_number):
    #     pass



