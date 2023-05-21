import Interactable, Monster

class MonsterS(Monster):
    def __init__(self):
        self.rect: Rect
        self.image: Surface
        self.mon_speed: int
        super().__init__(loc_x,loc_y,mon_damage,mon_health)