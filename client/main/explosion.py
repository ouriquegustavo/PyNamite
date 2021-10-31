import pygame

class Explosion():
    def __init__(self, client, id_ent, x, y, **kwargs):
        self.client = client
        self.id_ent = id_ent
        self.x=x
        self.y=y
        self.colour = (255, 0, 0, 255)
        
        self.radius=0
        self.radius_delta=37
        self.max_radius=200
        self.growth_ticks = 5
        self.shrink_ticks = 5
        self.max_ticks = self.growth_ticks+self.shrink_ticks
        
        self.sprite=pygame.Surface(
            (2*self.max_radius, 2*self.max_radius), pygame.SRCALPHA
        )
        self.sprite.fill((0,0,0,0))
        
        self.tick=0
        
        self.is_hidden=False
        self.is_updating=True
        
    def draw(self):
        if not self.is_hidden:
            self.client.display.blit(
                self.sprite, (self.x-self.radius,self.y-self.radius)
            )
            
    def update(self):
        self.tick+=1
        if self.tick <= self.growth_ticks:
            self.radius+=self.radius_delta
        if (
            self.tick > self.growth_ticks and
            self.tick <= self.max_ticks
        ):
            self.radius-=self.radius_delta
            
        self.sprite.fill((0,0,0,0))
        pygame.draw.circle(
            self.sprite, self.colour,
            (self.radius, self.radius), self.radius
        )

        if self.tick >= self.max_ticks:
            self.remove=True
