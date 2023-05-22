from Interactable import Interactable

class Monster(Interactable):
    
    def __init__(self,loc_x,loc_y,mon_speed,mon_damage,mon_health):
        self.mon_speed = mon_speed
        self.mon_health = mon_health
        self.mon_damage = mon_damage
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

