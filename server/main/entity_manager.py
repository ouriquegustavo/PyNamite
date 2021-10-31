import time
import random

class EntityManager():
    def __init__(self, server):
        self.server=server
        self.entities = {}
        self.events = {}
        self.id_ent_max = 8192
        self.id_event_max = 8192
        self.duration_event_max = 1000
        
        
    def create_entity(self, obj, id_ent, **args):
        if id_ent < 0:
            id_ent = random.randint(0,self.id_ent_max)
            while id_ent in self.entities:
                id_ent = random.randint(0, self.id_ent_max)
        ent = obj(self.server, id_ent, **args)
        self.entities[id_ent]=ent
        return ent
        
    def create_event(self, callback, data):
        s=int(1000*time.time())
        id_event = random.randint(0,self.id_event_max)
        while id_event in self.events:
            id_event = random.randint(0, self.id_event_max)
        event_time = s-self.server.time
        event_data = {
            't': event_time,
            'c': callback,
            'd': data
        }
        self.events[id_event] = event_data
        
    def update(self):
        s=int(1000*time.time())-self.server.time
        event_list = list(self.events.keys())
        for event in event_list:
            if s-self.events[event]['t'] > self.duration_event_max:
                del self.events[event]
    
        remove_list = []
        ent_list=list(self.entities.items())
        for id_ent, ent in ent_list:
            if (
                hasattr(ent, 'update')
                and hasattr(ent, 'is_updating')
                and ent.is_updating
            ):
                ent.update()
            if hasattr(ent, 'remove') and ent.remove:
                remove_list.append(id_ent)
        for id_ent in remove_list:
            del self.entities[id_ent]
