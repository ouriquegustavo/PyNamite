import random

class Character():
    def __init__(self, server, id_ent, x, y):
        self.kind = 'character'
        self.server = server
        self.id_ent = id_ent
        self.x=x
        self.y=y
        self.colour = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        
        self.width=50
        self.height=50
        
        self.is_updating=True
        
        self.bomb_delay = 0 
        self.max_bomb_delay = 60
        
    def export_data(self):
        data = {
            'kind': self.kind,
            'id': self.id_ent,
            'import': {
                'x': self.x,
                'y': self.y,
                'c': self.colour
            }
        }
        return data
        
    def update(self):
        if self.bomb_delay > 0:
            self.bomb_delay-=1
        if random.random() < 0.03:
            self.colour = (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            )
