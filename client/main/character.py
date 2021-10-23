import pygame

class Character():
    def __init__(self, client, id_ent, x, y, **kwargs):
        self.client = client
        self.id_ent = id_ent
        self.x=x
        self.y=y
        
        self.width=50
        self.height=50
        
        self.sprite=pygame.Surface((self.width, self.height))
        self.sprite.fill((255,255,255))
        
        self.is_hidden=False
        
    def draw(self):
        if not self.is_hidden:
            self.client.display.blit(
                self.sprite, (self.x-self.width/2,self.y-self.height/2)
            )
            
    def import_data(self, data):
        self.x=data['x']
        self.y=data['y']
