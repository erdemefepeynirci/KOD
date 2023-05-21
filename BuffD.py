import Interactable,Buff

class BuffD(Buff):
    def __init__(self):
        self.rect: Rect
        self.image: Surface
        super().__init__(loc_x,loc_y)

    def increase_damage(self):
        pass