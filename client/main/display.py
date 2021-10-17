import pygame

class Display():
    def __init__(self, client, width, height):
        self.client=client
        self.width=width
        self.height=height
    
    def start_display(self):
        self.diplay = pygame.display.set_mode(
            (self.width, self.height), pygame.DOUBLEBUF
        )
