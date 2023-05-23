from Interactable import Interactable

class Buff(Interactable):
    def __init__(self,loc_x,loc_y):
        self.effect_time = 10
        self.remaining_time = 10
        super().__init__(loc_x,loc_y)

    def affect(self,player):
        del self

    def create(self):
        pass