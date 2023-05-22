import pygame
class Interactable:
    def __init__(self,loc_x, loc_y):
        self.rect: pygame.Rect
        self.image: pygame.Surface    
        self.loc_x = loc_x
        self.loc_y = loc_y

    def is_interacted(self,locx,locy):
        if locx==self.loc_x and locy==self.loc_y:
            return True
        else:
            return False
        
    def create(self,locx,locy,image,height,width):
        self.image = pygame.transform.scale(pygame.image.load(image),(height,width))
        self.loc_x = locx
        self.loc_y = locy
        
    def draw(self,screen: pygame.Surface):
        screen.blit(self.image,(self.loc_x,self.loc_y))

    def affect(self):
        pass



