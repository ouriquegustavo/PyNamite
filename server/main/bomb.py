import random

class Bomb():
    def __init__(self, server, id_ent, x, y):
        self.kind = 'bomb'
        self.server = server
        self.id_ent = id_ent
        self.x=x
        self.y=y
        
        self.width=40
        self.height=40
        
        self.tick=0
        self.max_tick=120
        
        self.is_updating=True
        
    def export_data(self):
        data = {
            'kind': self.kind,
            'id': self.id_ent,
            'import': {
                'x': self.x,
                'y': self.y,
            }
        }
        return data
        
    def update(self):
        self.tick+=1
        if self.tick > self.max_tick:
            self.server.entity_manager.create_event(
                'explosion', data={'x': self.x, 'y': self.y}
            )
            self.remove=True
