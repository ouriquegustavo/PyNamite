import pygame
from main.networking import Networking

class Server():
    def __init__(self):
        self.tps=6
        self.clock = pygame.time.Clock()
        self.is_running=True
        self.start_networking()
        self.start_server()
        
    def start_networking(self):
        self.ip='192.168.0.57'
        self.port=7777
        self.networking=Networking(self, self.ip, self.port)
        self.networking.start_server_thread()
        
        
    def start_server(self):
        self.is_running=True
        
        while self.is_running:
            self.clock.tick(self.tps)
            #print('server thread')
