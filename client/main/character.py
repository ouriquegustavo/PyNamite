import pygame

class Character():
    def __init__(self, client, id_ent, x, y, **kwargs):
        self.client = client
        self.id_ent = id_ent
        self.x=x
        self.y=y
        self.colour = (255,255,255, 255)
        
        self.radius=25
        
        self.sprite=pygame.Surface((2*self.radius, 2*self.radius), pygame.SRCALPHA)
        self.sprite.fill(self.colour)
        
        self.is_hidden=False
        
    def draw(self):
        if not self.is_hidden:
            self.client.display.blit(
                self.sprite, (self.x-self.radius,self.y-self.radius)
            )
            
    def import_data(self, data):
        self.x=data['x']
        self.y=data['y']
        if self.colour != data['c']:
            self.colour=(data['c'][0], data['c'][1], data['c'][2], 255)
            self.sprite.fill((0,0,0,0))
            pygame.draw.circle(
                self.sprite, self.colour,
                (self.radius, self.radius), self.radius
            )
