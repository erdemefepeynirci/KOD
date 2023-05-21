import Interactable, Monster

class MonsterH(Monster):
    def __init__(self):
        self.rect: Rect
        self.image: Surface
        self.mon_health:int
        super().__init__(loc_x,loc_y,mon_speed,mon_damage)
