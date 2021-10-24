import pygame
import math


class Bomb():
    def __init__(self, client, id_ent, x, y, **kwargs):
        self.client = client
        self.id_ent = id_ent
        self.x=x
        self.y=y
        self.colour = (0, 0, 0, 255)
        
        self.min_radius=20
        self.max_radius=25
        self.radius=self.min_radius
        
        self.sprite=pygame.Surface(
            (2*self.max_radius, 2*self.max_radius), pygame.SRCALPHA
        )
        self.sprite.fill((0,0,0,0))
        
        self.tick=0
        self.freq=60
        
        self.is_hidden=False
        
    def draw(self):
        if not self.is_hidden:
            self.client.display.blit(
                self.sprite, (self.x-self.radius,self.y-self.radius)
            )
            
    def import_data(self, data):
        self.tick+=1
        self.x=data['x']
        self.y=data['y']
        dr=self.max_radius-self.min_radius
        var_radius=(math.cos(2*math.pi*self.tick/self.freq)+1)/2*dr
        self.radius=self.min_radius+var_radius
        self.sprite.fill((0,0,0,0))
        pygame.draw.circle(
            self.sprite, self.colour,
            (self.radius, self.radius), self.radius
        )
