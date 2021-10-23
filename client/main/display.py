import pygame

class Display():
    def __init__(self, client, width, height):
        self.client=client
        self.width=width
        self.height=height
    
    def start_display(self):
        self.display = pygame.display.set_mode(
            (self.width, self.height), pygame.DOUBLEBUF
        )
        
    def blit(self,*args):
        self.display.blit(*args)
        
        
    def update(self):
        self.display.fill((0,0,255))
    
        for id_ent, ent in self.client.entity_manager.entities.items():
            if not ent.is_hidden:
                ent.draw()
                
        for id_ent, ent in self.client.entity_manager.local_entities.items():
            if not ent.is_hidden:
                ent.draw()
            
            
        pygame.display.flip()
