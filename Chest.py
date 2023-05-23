from Interactable import Interactable
import pygame

class Chest(Interactable):
    def __init__(self,loc_x,loc_y):
        self.image = pygame.transform.scale(pygame.image.load("closedchest.png"),(120,75))
        self.rect: pygame.Rect
        super().__init__(loc_x,loc_y)
