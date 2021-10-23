import pygame

class Explosion():
    def __init__(self, client, id_ent, x, y, **kwargs):
        self.client = client
        self.id_ent = id_ent
        self.x=x
        self.y=y
        self.colour = (255, 0, 0)
        
        self.width=7
        self.height=7
        
        self.sprite=pygame.Surface((self.width, self.height))
        self.sprite.fill(self.colour)
        
        self.tick=0
        self.max_tick=20
        
        self.is_hidden=False
        self.is_updating=True
        
    def draw(self):
        if not self.is_hidden:
            self.client.display.blit(
                self.sprite, (self.x-self.width/2,self.y-self.height/2)
            )
            
    def update(self):
        self.tick+=1
        if self.tick <= 10:
            self.width += 6
            self.height += 6
        else:
            self.width -= 6
            self.height -= 6
            
        
        self.sprite=pygame.Surface((self.width, self.height))
        self.sprite.fill(self.colour)
        if self.tick >= self.max_tick:
            self.remove=True
