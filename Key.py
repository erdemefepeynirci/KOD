from Interactable import Interactable
import pygame

class Key(Interactable):
    def __init__(self,loc_x,loc_y):
        self._image = pygame.transform.scale(pygame.image.load("key.png"),(30,15))
        self._rect: pygame.Rect
        super().__init__(loc_x,loc_y)

    def affect(self):
        del self
        
