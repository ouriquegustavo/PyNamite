import pygame
from main.networking import Networking
from main.entity_manager import EntityManager
from main.character import Character
from main.bomb import Bomb
import math
import time
import random

class Server():
    def __init__(self):
        self.tps=60
        self.clock = pygame.time.Clock()
        self.time = int(1000*time.time())
        self.is_running=True
        self.x_size = 1600.
        self.y_size = 900.
        self.entity_manager=EntityManager(self)
        self.start_networking()
        self.start_server()
        
    def start_networking(self):
        self.ip='192.168.0.57'
        self.port=7777
        self.networking=Networking(self, self.ip, self.port)
        self.networking.start_server_thread()
        
        
    def start_server(self):
        self.is_running=True
        self.tick=0
        
        while self.is_running:
            self.clock.tick(self.tps)
            self.tick+=1
            
            self.entity_manager.update()
            

            #print('server thread')
