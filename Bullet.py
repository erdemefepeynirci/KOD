class Bullet:

    def __init__(self, loc_x, loc_y):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.color = (255,255,255)
        self.damage= 1
        self.speed= 3

    def is_hit_wall(self):
        pass

    def is_hit_monster(self):
        pass

    def draw(self):
        pass

    def bullet_move(self):
        pass

    def create(self):
        pass

    def remove_bullet(self):
        pass
