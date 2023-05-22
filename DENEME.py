import pygame
from Player import Player
from pygame.locals import *
from MonsterD import MonsterD
from MonsterH import MonsterH
from MonsterS import MonsterS

class Game:
    def __init__(self):

        
        self.player: Player

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
        self.canavar_height = 30
        self.canavar_width = 30

        #Key ayarları
        self.key_height = 60
        self.key_width = 90

        #Arrayler
        self.walls = []
        self.floors = []
        self.stairs = []
        self.canavarlar = []
        self.keys = []
        


    
    def run(self):

        pygame.display.set_caption(self._name)


        self.start()
        
        while True:
            self._screen.fill((0,0,0))
            self.time_tick()

            self._screen.blit(self._life_image,(0,0))
            self._screen.blit(self._life_image,(35,0))
            self._screen.blit(self._life_image,(70,0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()

            pygame.display.update()

    def start(self):
        self.player = Player()
        self.player.create(60,675)
        self.monsterD1 = MonsterD(840,675,10,3,2)
        self.monsterD1.create(840,675,"heart.png",30,30)
        self.monsterD2 = MonsterD(570,555,10,3,2)
        self.monsterD2.create(570,555,"heart.png",30,30)
        self.monsterD3 = MonsterD(480,435,10,3,2)
        self.monsterD3.create(480,435,"heart.png",30,30)
        self.monsterD4 = MonsterD(360,315,10,3,2)
        self.monsterD4.create(360,315,"heart.png",30,30)
        self.monsterD5 = MonsterD(780,195,10,3,2)
        self.monsterD5.create(780,195,"heart.png",30,30)
        self.monsterH1 = MonsterH(810,555,10,4,1)
        self.monsterH1.create(810,555,"heart.png",30,30)
        self.monsterH2 = MonsterH(510,435,10,4,1)
        self.monsterH2.create(510,435,"heart.png",30,30)
        self.monsterH3 = MonsterH(600,75,10,4,2)
        self.monsterH3.create(600,75,"heart.png",30,30)
        self.monsterS1 = MonsterS(660,675,20,3,1)
        self.monsterS1.create(660,675,"heart.png",30,30)
        self.monsterS2 = MonsterS(540,435,20,3,1)
        self.monsterS2.create(540,435,"heart.png",30,30)
        self.monsterS3 = MonsterS(570,315,20,3,1)
        self.monsterS3.create(570,315,"heart.png",30,30)
        self.monsterS4 = MonsterS(180,195,20,3,1)
        self.monsterS4.create(180,195,"heart.png",30,30)
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
            stair_rect = pygame.Rect(stair.left,stair.top,stair.width,stair.height)
            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.stair_image = pygame.transform.scale(pygame.image.load("stair.png"),(self.stair_width,self.stair_height))
            self._screen.blit(self.stair_image,stair_rect)

    
        """visible_canavarlar = [canavar for canavar in self.canavarlar if canavar.top > self.player.varying_y - self._window_height/2 and canavar.top < self.player.varying_y + self._window_height/2 ] 

        for visible_canavar in visible_canavarlar:
            new_rect_top = self.player.loc_y + (visible_canavar.top - self.player.varying_y)
            new_rect = pygame.Rect(visible_canavar.left,new_rect_top,visible_canavar.width,visible_canavar.height)
            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.canavar_image = pygame.transform.scale(pygame.image.load("heart.png"),(self.canavar_width,self.canavar_height))
            self._screen.blit(self.canavar_image,new_rect)

        visible_keys = [key for key in self.keys if key.top > self.player.varying_y - self._window_height/2 and key.top < self.player.varying_y + self._window_height/2 ] 

        for visible_key in visible_keys:
            new_rect_top = self.player.loc_y + (visible_key.top - self.player.varying_y)
            new_rect = pygame.Rect(visible_key.left,new_rect_top,visible_key.width,visible_key.height)
            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.key_image = pygame.transform.scale(pygame.image.load("key.png"),(self.key_width,self.key_height))
            self._screen.blit(self.key_image,new_rect)"""


        self.player.draw(screen=self._screen)
        self.monsterD1.draw(screen=self._screen)
        self.monsterD2.draw(screen=self._screen)
        self.monsterD3.draw(screen=self._screen)
        self.monsterD4.draw(screen=self._screen)
        self.monsterD5.draw(screen=self._screen)
        self.monsterS1.draw(screen=self._screen)
        self.monsterS2.draw(screen=self._screen)
        self.monsterS3.draw(screen=self._screen)
        self.monsterS4.draw(screen=self._screen)
        self.monsterH3.draw(screen=self._screen)
        self.monsterH2.draw(screen=self._screen)
        self.monsterH1.draw(screen=self._screen)


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
        default_walls_right = pygame.Rect((0,self._window_width-self.default_wall_width,self.default_wall_width,self.default_wall_height))
        self.walls.append(default_walls_right)
        
        wall1 = pygame.Rect(630,480,self.wall_width,self.wall_height)
        wall2 = pygame.Rect(90,480,self.wall_width,self.wall_height)
        wall3 = pygame.Rect(480,240,self.wall_width,self.wall_height)
        wall4 = pygame.Rect(660,120,self.wall_width,self.wall_height)

        self.walls.append(wall2)
        self.walls.append(wall1)
        self.walls.append(wall3)
        self.walls.append(wall4)


    def game_over(self):
        pass

    def respawn(self):
        pass

    def create_bullet(self, loc_x, loc_y):
        pass

    def are_there_enough_keys(self):
        pass

    def check_respawn_time_is_over(self):
        pass

    def is_there_a_wall(self,loc_x,loc_y):
        pass

    def is_there_stairs(self,loc_x,loc_y):
        pass

my_game = Game()
my_game.run()
