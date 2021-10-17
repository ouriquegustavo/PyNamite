import pygame
from main.networking import Networking

class Client():
    def __init__(self):
        self.tps=30
        self.clock = pygame.time.Clock()
        self.is_running=True
        self.start_networking()
        self.start_client()
        
    def start_networking(self):
        #self.ip='127.0.0.1'
        #self.port=7777
        self.networking=Networking(self)
        self.networking.start_client_thread()
        
        
    def start_client(self):
        self.is_running=True
        
        while self.is_running:
            self.clock.tick(self.tps)
            #print('client thread')
