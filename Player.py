import pygame

class Player:
    def __init__(self):
        self.rect: pygame.Rect
        self.image: pygame.Surface
        self.loc_x: float
        self.loc_y: float

        self.life: int
        self.speed: int
        self.direction: str

    def go_right(self):
        pass

    def go_left(self):
        pass

    def go_up(self):
        pass

    def go_down(self):
        pass
    
    def shoot(self):
        pass

    def get_key(self):
        pass
    
    def get_buff(self):
        pass

    def lose_life(self):
        pass

    def die(self):
        pass

    def draw(self,screen: pygame.Surface):
        screen.blit(self.image,(self.loc_x,self.loc_y))


    def create(self,locx,locy):
        self.image = pygame.transform.scale(pygame.image.load("player.png"),(30,30))
        self.loc_x = locx
        self.loc_y = locy
        


    def here_is_loc(self):
        return (self.loc_x,self.loc_y)

    def check_life(self):
        pass