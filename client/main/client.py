import pygame
from main.networking import Networking
from main.display import Display

class Client():
    def __init__(self):
        self.tps=30
        self.clock = pygame.time.Clock()
        self.is_running=True
        self.data='N'
        self.start_networking()
        self.start_display()
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
                    
            keys=pygame.key.get_pressed()
            self.data=keys[pygame.K_w] and 'W' or 'N'
            print(self.data)
