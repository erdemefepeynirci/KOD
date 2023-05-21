import Interactable,Buff

class BuffH(Buff):
    def __init__(self):
        self.rect: Rect
        self.image: Surface
        super().__init__(loc_x,loc_y)
   
    def increase_life(self):
        pass
