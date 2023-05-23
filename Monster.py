from Interactable import Interactable
import random

class Monster(Interactable):
    
    def __init__(self,loc_x,loc_y):
        self.mon_speed = 2
        self.mon_health = 3
        self.mon_damage = 1
        self.r = random.randint(0,1)
        if self.r == 0:
            self.direction = "R"
        else:
            self.direction = "L"
        
        super().__init__(loc_x,loc_y)

    def mon_die(self):
            del self
            

    def mon_move(self):
        if self.direction == "R":
            self.loc_x += 5*self.mon_speed
        else:
            self.loc_x -= 5* self.mon_speed

    def respawn(self):
        pass

    def change_direction(self):
        if self.direction == "R":
            self.direction = "L"
        else:
            self.direction = "R"


    def is_get_hit(self,locx,locy):
        if locx>self.loc_x-15 and locx<=self.loc_x+15 and locy>self.loc_y-15 and locy<=self.loc_y+15:
            self.lose_health()
            return True
        else:
            return False

    def lose_health(self):
        self.mon_health -=1

    def here_is_mon_loc(self):
        return (self.loc_x,self.loc_y)

    def affect(self,player):
        player.lose_life(1)
        
