import pygame
from Player import Player
import random
from pygame.locals import *

class Game:
    def __init__(self):

        
        self.player: Player

        #Genel ayarlar
        self._name = "Treasure Hunter"
        self._window_height = 720
        self._window_width = 720


        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._window_width,self._window_height))
        #self._rect: Rect
        self._life_image = pygame.transform.scale(pygame.image.load("heart.png"),(30,30))
        self._key_number = 0


        #Duvar Ayarları
        self.wall_width = 40

        #Zemin Ayarları
        self.floor_count = 20
        self.floor_height = 15
        self.floor_seperation = 120

        #Merdiven Ayarları
        self.stair_width = 30
        self.max_stair_count = 4

        #Canavar Ayarları
        self.canavar_height = 30
        self.canavar_width = 30

        #Key ayarları
        self.key_height = 20
        self.key_width = 55

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
        self.player.create((self._window_width/2)-15,(self._window_height/2)-15)


        self.create_map()


    def time_tick(self):
       
        visible_walls = [wall for wall in self.walls if wall.bottom > self.player.varying_y - self._window_height/2 and wall.top < self.player.varying_y + self._window_height/2 ] 
        for visible_wall in visible_walls:
            new_rect_top = self.player.loc_y + (visible_wall.top - self.player.varying_y)
            new_rect = pygame.Rect(visible_wall.left,new_rect_top,visible_wall.width,visible_wall.height)
            pygame.draw.rect(self._screen,(255,0,255),new_rect)

            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.wall_image = pygame.transform.scale(pygame.image.load("Wall.png"),(self.wall_width,self.floor_seperation+15))
            self._screen.blit(self.wall_image,new_rect)

        
        visible_floors = [floor for floor in self.floors if floor.top > self.player.varying_y - self._window_height/2 and floor.top < self.player.varying_y + self._window_height/2 ] 

        for visible_floor in visible_floors:
            new_rect_top = self.player.loc_y + (visible_floor.top - self.player.varying_y)
            new_rect = pygame.Rect(0,new_rect_top,self._window_width,self.floor_height)

            #pygame.draw.rect(self._screen,(255,255,255),new_rect)

            self.floor_image = pygame.transform.scale(pygame.image.load("platform.png"),(self._window_width,self.floor_height))
            self._screen.blit(self.floor_image,new_rect)

        visible_stairs = [stair for stair in self.stairs if stair.bottom > self.player.varying_y - self._window_height/2 and stair.top < self.player.varying_y + self._window_height/2 ] 

        for visible_stair in visible_stairs:
            new_rect_top = self.player.loc_y + (visible_stair.top - self.player.varying_y)
            new_rect = pygame.Rect(visible_stair.left,new_rect_top,visible_stair.width,visible_stair.height)
            #pygame.draw.rect(self._screen,(255,0,255),new_rect)

            self.stair_image = pygame.transform.scale(pygame.image.load("stair.png"),(self.stair_width,self.floor_seperation+15))
            self._screen.blit(self.stair_image,new_rect)

    
        visible_canavarlar = [canavar for canavar in self.canavarlar if canavar.top > self.player.varying_y - self._window_height/2 and canavar.top < self.player.varying_y + self._window_height/2 ] 

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
            self._screen.blit(self.key_image,new_rect)


        self.player.draw(screen=self._screen)
        self._clock.tick(60)
        



            

    
    def quit(self):
        pygame.quit()


    def create_map(self):
        
        self.current_y = self._window_height
        
        for i in range(0,self.floor_count):
            self.current_y -= (self.floor_seperation + self.floor_height)

            floor = pygame.Rect(0,self.current_y,self._window_width,self.floor_height)
            self.floors.append(floor)

            stair_count = random.randint(1,3)

            last_stair_left = 0
            if(i == self.floor_count-1):
                break
            for j in range(stair_count):
                
                if (last_stair_left + self.stair_width + 100 > self._window_width):
                    break

                if (last_stair_left == 0):
                    stair = pygame.Rect(random.randrange(last_stair_left + self.stair_width,self._window_width/2),floor.top-(self.floor_seperation+self.floor_height),self.stair_width,self.floor_seperation+self.floor_height)
                else:
                    stair = pygame.Rect(random.randrange(last_stair_left + self.stair_width+100,self._window_width),floor.top-(self.floor_seperation+self.floor_height),self.stair_width,self.floor_seperation+self.floor_height)

                self.stairs.append(stair)
                last_stair_left = stair.left

                #If there is any stair before this
                if (j != 0):
                    new_wall = pygame.Rect((self.stairs[-2].right+stair.left)/2-self.wall_width/2,stair.top,self.wall_width,stair.height)
                    self.walls.append(new_wall)
            
                default_walls_left = pygame.Rect((0,stair.top,self.wall_width,stair.height))
                self.walls.append(default_walls_left)

                default_walls_right = pygame.Rect((self._window_width,stair.top,self.wall_width,stair.height))
                self.walls.append(default_walls_right)
            
            spawned_monster = False
            while not spawned_monster:  
                spawn_x = random.randrange(0,self._window_width)
                spawn_y = floor.top - self.canavar_height

                canavar_rect = pygame.Rect(spawn_x,spawn_y,self.canavar_width,self.canavar_height)

                bu_kattaki_duvarlar = [duvar for duvar in self.walls if duvar.top == floor.top+self.floor_height+self.floor_seperation]

                cakisiyor_mu = canavar_rect.collidelist(bu_kattaki_duvarlar)

                if (cakisiyor_mu != -1):
                    break
                else:
                    self.canavarlar.append(canavar_rect)
                    spawned_monster = True
            
            spawned_key = False
            while not spawned_key:
                
                spawn_x = random.randrange(0,self._window_width)
                spawn_y = floor.top - self.key_height

                key_rect = pygame.Rect(spawn_x,spawn_y,self.key_width,self.key_height)

                bu_kattaki_duvarlar = [duvar for duvar in self.walls if duvar.top == floor.top+self.floor_height+self.floor_seperation]

                cakisiyor_mu = key_rect.collidelist(bu_kattaki_duvarlar)

                if (cakisiyor_mu != -1):
                    break
                else:
                    self.keys.append(key_rect)
                    spawned_key = True










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

    def can_spawn_here(self,rect):
        pass

    def is_there_stairs(self,loc_x,loc_y):
        pass

my_game = Game()
my_game.run()
