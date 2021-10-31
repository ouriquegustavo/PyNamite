import random
import math

def calc_dr_sq(ient, fent):
    dx = ient.x-fent.x
    dy = ient.y-fent.y
    dr_sq = dx*dx+dy*dy
    return dr_sq

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
        self.max_tick=180
        
        self.is_updating=True
        
        self.damage_radius = 150
        self.damage_radius_sq = self.damage_radius*self.damage_radius
        
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
            for id_ent, ent in self.server.entity_manager.entities.items():
                if ent.kind=='character':
                    dr_sq = calc_dr_sq(self, ent)
                    if dr_sq < self.damage_radius_sq:
                        ent.x=random.random()*self.server.x_size
                        ent.y=random.random()*self.server.y_size
                if ent.kind=='bomb':
                    dr_sq = calc_dr_sq(self, ent)
                    if dr_sq < self.damage_radius_sq:
                        ent.tick = self.max_tick
