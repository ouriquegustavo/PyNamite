import pygame
from main.networking import Networking
from main.entity_manager import EntityManager
from main.character import Character
import math

class Server():
    def __init__(self):
        self.tps=60
        self.clock = pygame.time.Clock()
        self.is_running=True
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
            
            for id_player in self.networking.client_data:
                client_data = self.networking.client_data[id_player]
                
                self.entity_manager.entities[id_player].x+=(
                    -client_data['l']+client_data['r']
                )
                self.entity_manager.entities[id_player].y+=(
                    -client_data['u']+client_data['d']
                )

            #print('server thread')
