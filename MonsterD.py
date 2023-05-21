import Interactable, Monster

class MonsterD(Monster):
    def __init__(self):
        self.rect: Rect
        self.image: Surface
        self.mon_damage: int
        super().__init__(loc_x,loc_y,mon_speed,mon_health)