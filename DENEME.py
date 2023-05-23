import pygame
from Bullet import Bullet 
from Interactable import Interactable
from Player import Player
from pygame.locals import *
from MonsterD import MonsterD
from MonsterH import MonsterH
from MonsterS import MonsterS
from Chest import Chest
from Key import Key
from Buff import Buff
from BuffD import BuffD
from BuffS import BuffS
from BuffH import BuffH

class Game:
    def __init__(self):

        
        #Genel ayarlar
        self._name = "Treasure Hunter"
        self._window_height = 720
        self._window_width = 1080

    
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._window_width,self._window_height))
        #self._rect: Rect
        self._life_image = pygame.transform.scale(pygame.image.load("heart.png"),(30,30))
        self._key_number = 0

        #Duvar Ayarları
        self._default_wall_height = self._window_height
        self._default_wall_width = 60
        self._wall_width = 60
        self._wall_height = 105
                
        #Zemin Ayarları
        self._floor_count = 6
        self._floor_height = 15
        self._floor_width = self._window_width-self._wall_width*2
        self._floor_seperation = 105


        #Merdiven Ayarları
        self._stair_width = 30
        self._stair_height = 120


        #Arrayler
        self._walls = []
        self._floors = []
        self._stairs = []
        self._canavarlar = []
        self._keys = []
        self._interactable = []
        self._bullets = []
        self._buffs = []
        self._effective_buff = []
        


    
    def run(self):

        pygame.display.set_caption(self._name)

        self.start()
        
        while True:

            keys=pygame.key.get_pressed()
            loc_x,loc_y = self._player.here_is_loc()
            if keys[K_LEFT]:
                if self.is_there_a_wall(loc_x-5,loc_y) is False:
                    if self.is_there_floor(loc_x,loc_y):
                        self._player.go_left()
            if keys[K_RIGHT]:
                if self.is_there_a_wall(loc_x+5,loc_y) is False:
                    if self.is_there_floor(loc_x,loc_y):
                        self._player.go_right()

            if keys[K_UP]:
                if self.are_there_stairs(loc_x,loc_y-5):
                    self._player.go_up()


            if keys[K_DOWN]:
                if self.are_there_stairs(loc_x,loc_y+5):
                    self._player.go_down()

            if keys[K_SPACE]:
                self.create_bullet(loc_x,loc_y)                   

            self._screen.fill((0,0,0))
            self.time_tick()

            k=self._player.check_life()
            for i in range(k): 
                self._screen.blit(self._life_image,(35*i,0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()

            pygame.display.update()

    def start(self):

        self._player = Player(60,665)

        self._monsterD1 = MonsterD(840,660)
        self._monsterD2 = MonsterD(570,540)
        self._monsterD3 = MonsterD(480,420)
        self._monsterD4 = MonsterD(360,300)
        self._monsterD5 = MonsterD(780,180)
        self._monsterH1 = MonsterH(810,540)
        self._monsterH2 = MonsterH(510,420)
        self._monsterH3 = MonsterH(600,60)
        self._monsterS1 = MonsterS(660,660)
        self._monsterS2 = MonsterS(540,420)
        self._monsterS3 = MonsterS(570,300)
        self._monsterS4 = MonsterS(180,180)

        
        self._chest = Chest(930,40)
        
        self._key1 = Key(810,75)
        self._key2 = Key(720,195)
        self._key3 = Key(420,315)
        self._key4 = Key(990,315)
        self._key5 = Key(60,435)
        self._key6 = Key(600,435)
        self._key7 = Key(930,435)
        self._key8 = Key(510,555)
        self._key9 = Key(690,555)
        self._key10 = Key(960,675)

        self._canavarlar.append(self._monsterD1)
        self._canavarlar.append(self._monsterD2)
        self._canavarlar.append(self._monsterD3)
        self._canavarlar.append(self._monsterD4)
        self._canavarlar.append(self._monsterD5)
        self._canavarlar.append(self._monsterS1)
        self._canavarlar.append(self._monsterS2)
        self._canavarlar.append(self._monsterS3)
        self._canavarlar.append(self._monsterS4)
        self._canavarlar.append(self._monsterH1)
        self._canavarlar.append(self._monsterH2)
        self._canavarlar.append(self._monsterH3)


        self._keys.append(self._key1)
        self._keys.append(self._key2)
        self._keys.append(self._key3)
        self._keys.append(self._key4)
        self._keys.append(self._key5)
        self._keys.append(self._key6)
        self._keys.append(self._key7)
        self._keys.append(self._key8)
        self._keys.append(self._key9)
        self._keys.append(self._key10)

        self.create_map()


    def time_tick(self):

        for wall in self._walls:

            wall_rect = pygame.Rect(wall.left,wall.top,wall.width,wall.height)

            self._wall_image = pygame.transform.scale(pygame.image.load("Wall.png"),(self._wall_width,self._wall_height))
            self._screen.blit(self._wall_image,wall_rect)


        for floor in self._floors:
            floor_rect = pygame.Rect(floor.left,floor.top,self._floor_width,self._floor_height)

            self._floor_image = pygame.transform.scale(pygame.image.load("platform.png"),(self._floor_width,self._floor_height))
            self._screen.blit(self._floor_image,floor_rect)

        for stair in self._stairs:
            stair_rect = pygame.Rect(stair.left+10,stair.top-5,stair.width+10,stair.height+10)

            self._stair_image = pygame.transform.scale(pygame.image.load("stair.png"),(self._stair_width,self._stair_height))
            self._screen.blit(self._stair_image,stair_rect)



        self._player.draw(screen=self._screen)

        self._chest.draw(screen=self._screen)

        for key in self._keys:
            key.draw(screen=self._screen)

        for mon in self._canavarlar:
            mon.draw(screen=self._screen)

        for buff in self._buffs:
            buff.draw(self._screen)

        for bullet in self._bullets:
            bullet.draw(screen=self._screen)
            bullet.bullet_move()
            b2 = self.is_there_a_wall(bullet._loc_x,bullet._loc_y)
            if b2:
                self._bullets.remove(bullet)
                bullet.remove_bullet() 
            for mon in self._canavarlar:
                b1 = mon.is_get_hit(bullet._loc_x,bullet._loc_y)
                if b1:
                    self._bullets.remove(bullet)
                    bullet.remove_bullet()
                if mon.mon_died():
                    self.mon_die(mon)



        loc = self._player.here_is_loc()

        for key in self._keys:
            if key.is_interacted(loc[0],loc[1]):
                self._key_number+=1
                key.affect()
                self._keys.remove(key)
                if self.are_there_enough__keys():
                    self.open_chest()

        for buff in self._buffs:
             if buff.is_interacted(loc[0],loc[1]):
                buff.affect(self._player)   
                self._buffs.remove(buff)


        for mon in self._canavarlar:
            if mon.is_interacted(loc[0],loc[1]):
                mon.affect(self._player)
                self.respawn()

        for mon in self._canavarlar:  
            loc = mon.here_is_mon_loc()
            b = self.is_there_a_wall(loc[0],loc[1])
            if b:
                mon.change_direction()
            mon.mon_move()


        if self._player.check_if_dead():
            self.die(self._player)


        self._clock.tick(60)

    
    def quit(self):
        pygame.quit()


    def create_map(self):
        
        self._current_y = self._window_height
        
        for i in range(0,self._floor_count):

            floor = pygame.Rect(self._wall_width,self._current_y-self._floor_height,self._floor_width,self._floor_height)
            self._floors.append(floor)
            self._current_y -= (self._floor_seperation + self._floor_height)

        stair1 = pygame.Rect((180,585, self._stair_width,self._stair_height))
        stair2 = pygame.Rect((900,585, self._stair_width,self._stair_height))
        stair3 = pygame.Rect((840,465, self._stair_width,self._stair_height))
        stair4 = pygame.Rect((750,345, self._stair_width,self._stair_height))
        stair5 = pygame.Rect((150,345, self._stair_width,self._stair_height))
        stair6 = pygame.Rect((570,225, self._stair_width,self._stair_height))
        stair7 = pygame.Rect((900,225, self._stair_width,self._stair_height))
        stair8 = pygame.Rect((90,105 , self._stair_width,self._stair_height))

        self._stairs.append(stair1)
        self._stairs.append(stair2)
        self._stairs.append(stair3)
        self._stairs.append(stair4)
        self._stairs.append(stair5)
        self._stairs.append(stair6)
        self._stairs.append(stair7)
        self._stairs.append(stair8)
            
        default_walls_left = pygame.Rect((0,0,self._default_wall_width,self._default_wall_height))
        self._walls.append(default_walls_left)
        default_walls_right = pygame.Rect((self._window_width-self._default_wall_width,0,self._default_wall_width,self._default_wall_height))
        self._walls.append(default_walls_right)
        
        wall1 = pygame.Rect(630,480,self._wall_width,self._wall_height)
        wall2 = pygame.Rect(90,480,self._wall_width,self._wall_height)
        wall3 = pygame.Rect(480,240,self._wall_width,self._wall_height)
        wall4 = pygame.Rect(660,120,self._wall_width,self._wall_height)
 
        self._walls.append(wall2)
        self._walls.append(wall1)
        self._walls.append(wall3)
        self._walls.append(wall4)


    def game_over(self,cond):
        self._screen.fill((0,0,0))
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 50)
        if cond == "lost":
            text_surface = my_font.render('YOU LOST, TRY AGAIN', False, (255,255,255))
            self._screen.blit(text_surface, (250,340))
        if cond == "won":
            text_surface = my_font.render('CONGRATULATIONS, YOU WON', False, (255,255,255))
            self._screen.blit(text_surface, (250,340))


    def respawn(self):
        self._player.turn_to_initial_pos()
        

    def create_bullet(self, loc_x, loc_y):
        direction = self._player.here_is_direc()
        self._bullets.append(Bullet(loc_x,loc_y,direction))
        

    def are_there_enough__keys(self):
        if self._key_number==10:
            return True
        else:
            return False

    # def check_respawn_time_is_over(self):
    #     pass

    def is_there_a_wall(self,loc_x,loc_y):
        for wall in self._walls:
            if pygame.Rect.collidepoint(wall,loc_x,loc_y):
                return True
        return False

    def are_there_stairs(self,loc_x,loc_y):
        for stair in self._stairs:
            if pygame.Rect.collidepoint(stair,loc_x,loc_y+40):
                return True
        return False
    
    def is_there_floor(self,locx,locy):
        for floor in self._floors:
            if pygame.Rect.collidepoint(floor,locx,locy+40):
                return True
        return False

    
    def mon_die(self,canavar):
        loc = canavar.here_is_mon_loc()
        if isinstance(canavar,MonsterD):
            buff = BuffD(loc[0],loc[1])
            self._buffs.append(buff)
        elif isinstance(canavar,MonsterS):
            buff = BuffS(loc[0],loc[1])
            self._buffs.append(buff)
        else:
            buff = BuffH(loc[0],loc[1])
            self._buffs.append(buff)

        self._canavarlar.remove(canavar)
        del canavar

    
    def die(self,player):
        del player
        self.game_over("lost")


    def open_chest(self):
        self.game_over("won")

my_game = Game()
my_game.run()


# to do
# bulleta cooldown ekle
# remaining effect time ekle
# heath barı düzenle

# buff alındığında bullet rengi
# monsterlar respawn olacak
# mons yavaşşşş hareket ediyo
# duvara girme
# açık chest resmi