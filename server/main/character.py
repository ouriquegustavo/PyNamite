import random
import math

class Character():
    def __init__(self, server, id_ent, x, y):
        self.kind = 'character'
        self.server = server
        self.id_ent = id_ent
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.colour = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        
        self.acc = 0.2
        self.max_speed = 5
        self.damping = 0.1
        
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
        dx=0
        dy=0
        dr_sq=0
        if self.id_ent in self.server.networking.client_data:
            client_data = self.server.networking.client_data[self.id_ent]
            dx=-client_data['l']+client_data['r']
            dy=-client_data['u']+client_data['d']
            dr_sq=dx*dx+dy*dy
        if dr_sq > 0:
            dr = math.sqrt(dr_sq)
            dx=dx/dr
            dy=dy/dr
            self.vx+=dx*self.acc
            self.vy+=dy*self.acc
            
        vr_sq = self.vx*self.vx+self.vy*self.vy
        if vr_sq < 0.01:
            self.vx=0
            self.vy=0
        if vr_sq > 0:
            vr_x = self.vx/vr_sq
            vr_y = self.vy/vr_sq
            self.vx = self.vx*(1-self.damping*abs(vr_x))
            self.vy = self.vy*(1-self.damping*abs(vr_y))
        
            
        self.x+=self.vx
        self.y+=self.vy
    
        if self.bomb_delay > 0:
            self.bomb_delay-=1
