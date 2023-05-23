import pygame

class Player:
    def __init__(self,locx,locy):
        self.rect: pygame.Rect

        self.image = pygame.transform.scale(pygame.image.load("player.png"),(30,40))
        self.loc_x = locx
        self.loc_y = locy
        self.speed = 1
        self.direction = "R"
        self.life = 3
        

    def go_right(self):
        self.loc_x +=5*self.speed
        self.direction = "R"

    def go_left(self):
        self.loc_x -=5*self.speed
        self.direction = "L"

    def go_up(self):
        self.loc_y -=5*self.speed

    def go_down(self):
        self.loc_y +=5*self.speed
    
    # def shoot(self):
    #     pass

    def get_key(self):
        pass
    
    def get_buff(self):
        pass

    def lose_life(self,num):
        self.life-= num


    def draw(self,screen: pygame.Surface):
        screen.blit(self.image,(self.loc_x,self.loc_y))



    def here_is_loc(self):
        return (self.loc_x,self.loc_y)
    
    def here_is_direc(self):
        return self.direction

    def check_life(self):
        pass