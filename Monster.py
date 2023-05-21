import Interactable

class Monster(Interactable):
    
    def __init__(self):
        self.mon_speed: int
        self.mon_health: int
        self.mon_damage: int
        super().__init__(loc_x,loc_y)

    def mon_die(self):
        pass

    def mon_move(self):
        pass

    def respawn(self):
        pass

    def change_direction(self):
        pass

    def is_get_hit(self):
        pass 

    def lose_health(self):
        pass

