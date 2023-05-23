from Interactable import Interactable
import random

class Monster(Interactable):
    
    def __init__(self,loc_x,loc_y):
        self._mon_speed = 2
        self._mon_health = 3
        self._mon_damage = 1
        self._r = random.randint(0,1)
        if self._r == 0:
            self._direction = "R"
        else:
            self._direction = "L"
        
        super().__init__(loc_x,loc_y)

    def mon_die(self):
            del self
            

    def mon_move(self):
        if self._direction == "R":
            self._loc_x += 5*self._mon_speed
        else:
            self._loc_x -= 5* self._mon_speed

    def respawn(self):
        pass

    def change_direction(self):
        if self._direction == "R":
            self._direction = "L"
        else:
            self._direction = "R"


    def is_get_hit(self,locx,locy):
        if locx>self._loc_x-15 and locx<=self._loc_x+15 and locy>self._loc_y-15 and locy<=self._loc_y+15:
            self.lose_health()
            return True
        else:
            return False

    def lose_health(self):
        self._mon_health -=1

    def here_is_mon_loc(self):
        return (self._loc_x,self._loc_y)
    
    def mon_died(self):
        return self._mon_health == 0

    def affect(self,player):
        player.lose_life(self._mon_damage)
        
