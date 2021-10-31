import pygame
from main.networking import Networking
from main.display import Display
from main.entity_manager import EntityManager
from main.character import Character
from main.controls import Controls

class Client():
    def __init__(self):
        self.tps=60
        self.clock = pygame.time.Clock()
        self.is_running=True
        self.data='N'
        self.controls=Controls(self)
        self.start_networking()
        self.start_display()
        
        self.time = 1635690553843
        
        self.server_x_size = 1600.
        self.server_y_size = 900.
        
        self.x_scale = self.display_width/self.server_x_size
        self.y_scale = self.display_height/self.server_y_size
        
        self.start_client()
        
    def start_networking(self):
        self.networking=Networking(self)
        self.networking.start_client_thread()
        
    def start_display(self):
        self.display_width = 1366
        self.display_height = 768
        self.display=Display(self, self.display_width, self.display_height)
        self.display.start_display()
        
    def start_client(self):
        self.is_running=True
        self.entity_manager = EntityManager(self)
        #self.entity_manager.create_entity(Character, 45, x=15, y=10)
        
        while self.is_running:
            self.clock.tick(self.tps)
            #print('client thread')
            
            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT or
                    (
                        event.type==pygame.KEYDOWN and
                        event.key==pygame.K_ESCAPE
                    )
                ):
                    self.is_running = False
                    
            self.controls.get_keys()
                    
            self.entity_manager.update()
                    
            self.display.update()
            
            #print(self.networking.data)
            #keys=pygame.key.get_pressed()
            #self.data=keys[pygame.K_w] and 'W' or 'N'
            #print(self.data)
