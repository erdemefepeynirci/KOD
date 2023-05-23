import pygame

class Bullet:
    _damage= 1
    def __init__(self, loc_x, loc_y,direction,color=(255,255,255)):
        self._loc_x = loc_x
        self._loc_y = loc_y
        self._direction = direction
        self._color = color
        self._speed= 4
        self._flag = False

    def is_hit_wall(self):
        pass

    def is_hit_monster(self):
        pass

    def draw(self,screen):
        pygame.draw.line(screen,self._color, (self._loc_x,self._loc_y), (self._loc_x+5,self._loc_y),4)

    def bullet_move(self):
        if self._direction == "R":
            self._loc_x += 5*self._speed
        if self._direction == "L":
            self._loc_x -= 5*self._speed

    def increase_damage():
        Bullet._damage+=1

    def remove_bullet(self):
        del self
