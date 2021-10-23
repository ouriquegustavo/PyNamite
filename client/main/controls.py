import pygame

class Controls():
    def __init__(self, client):
        self.client=client
        self.keys = {
            'u': 0,
            'd': 0,
            'l': 0,
            'r': 0,
        }
        
    def get_keys(self):
        get_pressed=pygame.key.get_pressed()
        self.keys['u'] = int(get_pressed[pygame.K_w])
        self.keys['d'] = int(get_pressed[pygame.K_s])
        self.keys['l'] = int(get_pressed[pygame.K_a])
        self.keys['r'] = int(get_pressed[pygame.K_d])
