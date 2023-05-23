from Interactable import Interactable

class Buff(Interactable):
    def __init__(self,loc_x,loc_y):
        super().__init__(loc_x,loc_y)

    def affect(self,player):
        del self

    def create(self):
        pass