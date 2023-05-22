import pygame

class Bullet:

    def __init__(self, loc_x, loc_y,direction):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.direction = direction
        self.color = (255,255,255)
        self.damage= 1
        self.speed= 2

    def is_hit_wall(self):
        pass

    def is_hit_monster(self):
        pass

    def draw(self,screen):
        pygame.draw.line(screen,self.color, (self.loc_x,self.loc_y), (self.loc_x+5,self.loc_y),4)

    def bullet_move(self):
        if self.direction == "R":
            self.loc_x += 5*self.speed

    def create(self):
        pass

    def remove_bullet(self):
        pass
