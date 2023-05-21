import code.Interactable as Interactable

class Keys(Interactable):
    def __init__(self):
        self.rect: Rect
        self.image: Surface
        super().__init__(loc_x,loc_y)

    def create(self):
        pass
