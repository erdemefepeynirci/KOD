from Interactable import Interactable

class Buff(Interactable):
    def __init__(self):
        self.effect_time: int
        self.remaining_time: int
        super().__init__(loc_x,loc_y)


    def create():
        pass