import pygame
import Bullet
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
        self.default_wall_height = self._window_height
        self.default_wall_width = 60
        self.wall_width = 60
        self.wall_height = 105
                
        #Zemin Ayarları
        self.floor_count = 6
        self.floor_height = 15
        self.floor_width = self._window_width-self.wall_width*2
        self.floor_seperation = 105



        #Merdiven Ayarları
        self.stair_width = 30
        self.stair_height = 120
        self.max_stair_count = 3

        #Canavar Ayarları
        self.canavar_height = 40
        self.canavar_width = 50

        #Key ayarları
        self.key_height = 15
        self.key_width = 30

        #Arrayler
        self.walls = []
        self.floors = []
        self.stairs = []
        self.canavarlar = []
        self.keys = []
        self.interactable = []
        self.bullets = []
        self.buffs = []
        self.effective_buff = []
        


    
    def run(self):

        pygame.display.set_caption(self._name)


        self.start()
        
        while True:

            keys=pygame.key.get_pressed()
            loc_x,loc_y = self.player.here_is_loc()
            if keys[K_LEFT]:
                if self.is_there_a_wall(loc_x-5,loc_y) is False:
                    self.player.go_left()
            if keys[K_RIGHT]:
                if self.is_there_a_wall(loc_x+5,loc_y) is False:
                    self.player.go_right()

            if keys[K_UP]:
                if self.are_there_stairs(loc_x,loc_y-5):
                    self.player.go_up()


            if keys[K_DOWN]:
                if self.are_there_stairs(loc_x,loc_y+5):
                    self.player.go_down()

            if keys[K_SPACE]:
                self.create_bullet(loc_x,loc_y)
                # if BuffD.buffd_bool:
                #     self.create_bullet(loc_x,loc_y,(255,0,255))                    

            self._screen.fill((0,0,0))
            self.time_tick()

            self._screen.blit(self._life_image,(0,0))
            self._screen.blit(self._life_image,(35,0))
            self._screen.blit(self._life_image,(70,0)) 

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()

            pygame.display.update()

    def start(self):
        self.player = Player(60,665)

        self.monsterD1 = MonsterD(840,660)
        self.monsterD2 = MonsterD(570,540)
        self.monsterD3 = MonsterD(480,420)
        self.monsterD4 = MonsterD(360,300)
        self.monsterD5 = MonsterD(780,180)
        self.monsterH1 = MonsterH(810,540)
        self.monsterH2 = MonsterH(510,420)
        self.monsterH3 = MonsterH(600,60)
        self.monsterS1 = MonsterS(660,660)
        self.monsterS2 = MonsterS(540,420)
        self.monsterS3 = MonsterS(570,300)
        self.monsterS4 = MonsterS(180,180)

        
        self.chest = Chest(930,40)

        
        self.key1 = Key(810,75)
   
        self.key2 = Key(720,195)
        
        self.key3 = Key(420,315)
      
        self.key4 = Key(990,315)
     
        self.key5 = Key(60,435)
        self.key6 = Key(600,435)
        self.key7 = Key(930,435)
        self.key8 = Key(510,555)
        self.key9 = Key(690,555)
        self.key10 = Key(960,675)


        self.canavarlar.append(self.monsterD1)
        self.canavarlar.append(self.monsterD2)
        self.canavarlar.append(self.monsterD3)
        self.canavarlar.append(self.monsterD4)
        self.canavarlar.append(self.monsterD5)
        self.canavarlar.append(self.monsterS1)
        self.canavarlar.append(self.monsterS2)
        self.canavarlar.append(self.monsterS3)
        self.canavarlar.append(self.monsterS4)
        self.canavarlar.append(self.monsterH1)
        self.canavarlar.append(self.monsterH2)
        self.canavarlar.append(self.monsterH3)


        self.keys.append(self.key1)
        self.keys.append(self.key2)
        self.keys.append(self.key3)
        self.keys.append(self.key4)
        self.keys.append(self.key5)
        self.keys.append(self.key6)
        self.keys.append(self.key7)
        self.keys.append(self.key8)
        self.keys.append(self.key9)
        self.keys.append(self.key10)

        self.create_map()


    def time_tick(self):
        for wall in self.walls:

            wall_rect = pygame.Rect(wall.left,wall.top,wall.width,wall.height)
            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.wall_image = pygame.transform.scale(pygame.image.load("Wall.png"),(wall.width,wall.height))
            self._screen.blit(self.wall_image,wall_rect)

         

        for floor in self.floors:
            floor_rect = pygame.Rect(floor.left,floor.top,self.floor_width,self.floor_height)
            #pygame.draw.rect(self._screen,(255,255,255),new_rect)

            self.floor_image = pygame.transform.scale(pygame.image.load("platform.png"),(self.floor_width,self.floor_height))
            self._screen.blit(self.floor_image,floor_rect)

        for stair in self.stairs:
            stair_rect = pygame.Rect(stair.left+10,stair.top-5,stair.width+10,stair.height+10)
            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.stair_image = pygame.transform.scale(pygame.image.load("stair.png"),(self.stair_width,self.stair_height))
            self._screen.blit(self.stair_image,stair_rect)



        self.player.draw(screen=self._screen)

        self.chest.draw(screen=self._screen)

        for key in self.keys:
            key.draw(screen=self._screen)

        for mon in self.canavarlar:
            mon.draw(screen=self._screen)

        for buff in self.buffs:
            buff.draw(self._screen)

        for bullet in self.bullets:
            bullet.draw(screen=self._screen)
            bullet.bullet_move()
            b2 = self.is_there_a_wall(bullet.loc_x,bullet.loc_y)
            if b2:
                self.bullets.remove(bullet)
                bullet.remove_bullet  
            for mon in self.canavarlar:
                b1 = mon.is_get_hit(bullet.loc_x,bullet.loc_y)
                if b1:
                    self.bullets.remove(bullet)
                    bullet.remove_bullet()
                if mon.mon_health == 0:
                    self.mon_die(mon)

        loc = self.player.here_is_loc()
        for key in self.keys:
            if key.is_interacted(loc[0],loc[1]):
                self._key_number+=1
                key.affect()
                self.keys.remove(key)
                if self.are_there_enough_keys():
                    self.open_chest()

        for buff in self.buffs:
             if buff.is_interacted(loc[0],loc[1]):
                buff.affect(self.player)   
                self.buffs.remove(buff)


        for mon in self.canavarlar:
            if mon.is_interacted(loc[0],loc[1]):
                mon.affect(self.player)
                self.respawn()

        for mon in self.canavarlar:  
            loc = mon.here_is_mon_loc()
            b = self.is_there_a_wall(loc[0],loc[1])
            if b:
                mon.change_direction()
            mon.mon_move()


        if self.player.life <= 0:
            self.die(self.player)

        

        self._clock.tick(60)

    
    def quit(self):
        pygame.quit()


    def create_map(self):
        
        self.current_y = self._window_height
        
        for i in range(0,self.floor_count):

            floor = pygame.Rect(self.wall_width,self.current_y-self.floor_height,self.floor_width,self.floor_height)
            self.floors.append(floor)
            self.current_y -= (self.floor_seperation + self.floor_height)

        stair1 = pygame.Rect((180,585, self.stair_width,self.stair_height))
        stair2 = pygame.Rect((900,585, self.stair_width,self.stair_height))
        stair3 = pygame.Rect((840,465, self.stair_width,self.stair_height))
        stair4 = pygame.Rect((750,345, self.stair_width,self.stair_height))
        stair5 = pygame.Rect((150,345, self.stair_width,self.stair_height))
        stair6 = pygame.Rect((570,225, self.stair_width,self.stair_height))
        stair7 = pygame.Rect((900,225, self.stair_width,self.stair_height))
        stair8 = pygame.Rect((90,105 , self.stair_width,self.stair_height))

        self.stairs.append(stair1)
        self.stairs.append(stair2)
        self.stairs.append(stair3)
        self.stairs.append(stair4)
        self.stairs.append(stair5)
        self.stairs.append(stair6)
        self.stairs.append(stair7)
        self.stairs.append(stair8)
            
        default_walls_left = pygame.Rect((0,0,self.default_wall_width,self.default_wall_height))
        self.walls.append(default_walls_left)
        default_walls_right = pygame.Rect((self._window_width-self.default_wall_width,0,self.default_wall_width,self.default_wall_height))
        self.walls.append(default_walls_right)
        
        wall1 = pygame.Rect(630,480,self.wall_width,self.wall_height)
        wall2 = pygame.Rect(90,480,self.wall_width,self.wall_height)
        wall3 = pygame.Rect(480,240,self.wall_width,self.wall_height)
        wall4 = pygame.Rect(660,120,self.wall_width,self.wall_height)

        self.walls.append(wall2)
        self.walls.append(wall1)
        self.walls.append(wall3)
        self.walls.append(wall4)


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
        self.player.loc_x =60
        self.player.loc_y= 655
        

    def create_bullet(self, loc_x, loc_y):
        direction = self.player.here_is_direc()
        self.bullets.append(Bullet.Bullet(loc_x,loc_y,direction))
        

    def are_there_enough_keys(self):
        if self._key_number==10:
            return True
        else:
            return False

    def check_respawn_time_is_over(self):
        pass

    def is_there_a_wall(self,loc_x,loc_y):
        for wall in self.walls:
            if pygame.Rect.collidepoint(wall,loc_x,loc_y):
                return True
        return False

    def are_there_stairs(self,loc_x,loc_y):
        for stair in self.stairs:
            if pygame.Rect.collidepoint(stair,loc_x,loc_y+40):
                return True
        return False
    
    def mon_die(self,canavar):
        loc = canavar.here_is_mon_loc()
        if isinstance(canavar,MonsterD):
            buff = BuffD(loc[0],loc[1])
            self.buffs.append(buff)
        elif isinstance(canavar,MonsterS):
            buff = BuffS(loc[0],loc[1])
            self.buffs.append(buff)
        else:
            buff = BuffH(loc[0],loc[1])
            self.buffs.append(buff)

        self.canavarlar.remove(canavar)
        del canavar

    
    def die(self,player):
        self.game_over("lost")


    def open_chest(self):
        self.game_over("won")

my_game = Game()
my_game.run()


# to do
# bulleta cooldown ekle
# remaining effect time ekle
# heath barı düzenle
# merdiven çıkmayı düzelt
# buff alındığında bullet rengi
# monsterlar respawn olacak
# mons yavaşşşş hareket ediyo
# duvara girme
# açık chest resmi