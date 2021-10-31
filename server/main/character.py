import random
import math
from main.bomb import Bomb

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
        
        self.acc = 1.5
        self.max_speed = 10
        self.vmsq = self.max_speed*self.max_speed
        self.damping = 3
        
        self.width=50
        self.height=50
        
        self.is_updating=True
        
        self.bomb_distance=50
        
        self.bomb_delay = 0 
        self.max_bomb_delay = 20
        
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
        vr_sq = self.vx*self.vx+self.vy*self.vy
        if dr_sq > 0:
            dr = math.sqrt(dr_sq)
            dx=dx/dr
            dy=dy/dr
            nvx=self.vx+dx*self.acc
            nvy=self.vy+dy*self.acc
            nvr=nvx*nvx+nvy*nvy
            if nvr > self.vmsq:
                sqrt_nvr = math.sqrt(nvr)
                nvx=self.max_speed*nvx/sqrt_nvr
                nvy=self.max_speed*nvy/sqrt_nvr

            self.vx=nvx
            self.vy=nvy
        else:
            if vr_sq > 0:
                vr_x = self.vx/vr_sq
                vr_y = self.vy/vr_sq
                if (self.vx - vr_x*self.damping)*(self.vx) < 0:
                    self.vx=0
                else:
                    self.vx-= vr_x*self.damping
                if (self.vy - vr_y*self.damping)*(self.vy) < 0:
                    self.vy=0
                else:
                    self.vy-= vr_y*self.damping

        self.x+=self.vx
        self.y+=self.vy
        
        if self.x < 0:
            self.x = 0
            self.vx *= -1
        if self.x > self.server.x_size:
            self.x = self.server.x_size
            self.vx *= -1
        if self.y < 0:
            self.y = 0
            self.vy *= -1
        if self.y > self.server.y_size:
            self.y = self.server.y_size
            self.vy *= -1
            
        if self.bomb_delay > 0:
            self.bomb_delay-=1
            
        if client_data['m1'] and self.bomb_delay <= 0:
            dx_pos = client_data['x']-self.x
            dy_pos = client_data['y']-self.y
            angle = math.atan2(dy_pos, dx_pos)
            
            self.server.entity_manager.create_entity(
                Bomb, -1,
                x=self.x+self.bomb_distance*math.cos(angle),
                y=self.y+self.bomb_distance*math.sin(angle)
            )
            self.bomb_delay = self.max_bomb_delay

