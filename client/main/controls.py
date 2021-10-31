import pygame

class Controls():
    def __init__(self, client):
        self.client=client
        self.keys = {
            'u': 0,
            'd': 0,
            'l': 0,
            'r': 0,
            'a': 0,
            'x': 0,
            'y': 0,
            'm1': 0,
            'm2': 0,
            'm3': 0,
        }
        
    def get_keys(self):
        get_pressed=pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        self.keys['u'] = int(get_pressed[pygame.K_w])
        self.keys['d'] = int(get_pressed[pygame.K_s])
        self.keys['l'] = int(get_pressed[pygame.K_a])
        self.keys['r'] = int(get_pressed[pygame.K_d])
        self.keys['a'] = int(get_pressed[pygame.K_e])
        self.keys['x'] = int(mouse_pos[0]/self.client.x_scale)
        self.keys['y'] = int(mouse_pos[1]/self.client.y_scale)
        self.keys['m1'] = int(mouse_pressed[0])
        self.keys['m2'] = int(mouse_pressed[2])
        self.keys['m3'] = int(mouse_pressed[1])
