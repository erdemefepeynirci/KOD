class Bullet:

    def __init__(self):
        self.loc_x: int
        self.loc_y: int
        self.color: tuple
        self.damage: int
        self.speed: int

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
