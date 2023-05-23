import pygame

class Player:
    def __init__(self,locx,locy):
        self._rect: pygame.Rect
        self._image = pygame.transform.scale(pygame.image.load("player.png"),(30,40))
        self._loc_x = locx
        self._loc_y = locy
        self._speed = 1
        self._direction = "R"
        self._life = 3
        

    def go_right(self):
        self._loc_x +=5*self._speed
        self._direction = "R"

    def go_left(self):
        self._loc_x -=5*self._speed
        self._direction = "L"

    def go_up(self):
        self._loc_y -=5*self._speed

    def go_down(self):
        self._loc_y +=5*self._speed
    
    # def shoot(self):
    #     pass

    def get_key(self):
        pass
    
    def get_buff(self):
        pass

    def lose_life(self,num):
        self._life-= num

    def increase_life(self):
        if self._life<3:
            self._life+=1

    def increase_speed(self):
        self._speed+=1.5


    def draw(self,screen: pygame.Surface):
        screen.blit(self._image,(self._loc_x,self._loc_y))

    def turn_to_initial_pos(self):
        self._loc_x =60
        self._loc_y= 655

    def here_is_loc(self):
        return (self._loc_x,self._loc_y)
    
    def here_is_direc(self):
        return self._direction

    def check_if_dead(self):
        if self._life <=0:
            return True
        else:
            return False