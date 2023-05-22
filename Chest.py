from Interactable import Interactable
import pygame

class Chest(Interactable):
    def __init__(self,loc_x,loc_y):
        self.rect: pygame.Rect
        self.image: pygame.Surface
        super().__init__(loc_x,loc_y)

    def open(self):
        pass