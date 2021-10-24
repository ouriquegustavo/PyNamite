from main.character import Character
from main.bomb import Bomb
from main.explosion import Explosion
import time
import random

def explosion(client, x, y):
    client.entity_manager.create_local_entity(Explosion, x=x, y=y)
    #client.entity_manager[id_player].width=client.entity_manager[id_player].width*2


class EntityManager():
    def __init__(self, client):
        self.client=client
        self.entities = {}
        self.local_entities = {}
        self.events = {}
        self.id_ent_max = 8192
        self.duration_event_max = 1000
        self.kind_from_to = {
            'character': Character,
            'bomb': Bomb,
        }
        
        self.event_from_to = {
            'explosion': explosion
        }
        
        
    def create_entity(self, obj, id_ent, **kwargs):
        ent = obj(self.client, id_ent, **kwargs)
        self.entities[id_ent]=ent
        return ent
        
        
    def create_local_entity(self, obj, **kwargs):
        id_ent = random.randint(0,self.id_ent_max)
        while id_ent in self.entities:
            id_ent = random.randint(0, self.id_ent_max)
        ent = obj(self.client, id_ent, **kwargs)
        self.local_entities[id_ent]=ent
        return ent
        
        
    def update(self):
        s=int(1000*time.time())-self.client.time
        for id_event, data in self.client.networking.data.get(
            'events',{}
        ).items():
            if not id_event in self.events:
                self.events[id_event] = data
                func=self.event_from_to[data['c']]
                func(self.client, **data['d'])
        
        event_list = list(self.events.keys())
        for event in event_list:
            if s-self.events[event]['t'] > self.duration_event_max:
                del self.events[event]
    
        ## Networked entities
        remove_list=[]
        networking_entity_list = self.client.networking.data.get(
            'entities',{}
        ).keys()
        for id_ent, data in self.client.networking.data.get(
            'entities',{}
        ).items():
            if not id_ent in self.entities:
                self.create_entity(
                    self.kind_from_to[data['kind']],
                    id_ent,
                    **data['import']
                )
        for id_ent, ent in self.entities.items():
            if (
                hasattr(ent, 'import_data') and
                id_ent in self.client.networking.data['entities']
            ):
                ent.import_data(
                    self.client.networking.data['entities'][id_ent]['import']
                )
            if (
                hasattr(ent, 'update')
                and hasattr(ent, 'is_updating')
                and ent.is_updating
            ):
                ent.update()

            if not id_ent in networking_entity_list:
                ent.remove = True
            if hasattr(ent, 'remove') and ent.remove:
                remove_list.append(id_ent)
                
        for id_ent in remove_list:
            del self.entities[id_ent]
                
        ## Local Entities
        remove_list=[]
        for id_ent, ent in self.local_entities.items():
            if (
                hasattr(ent, 'update')
                and hasattr(ent, 'is_updating')
                and ent.is_updating
            ):
                ent.update()
            if hasattr(ent, 'remove') and ent.remove:
                remove_list.append(id_ent)
        for id_ent in remove_list:
            del self.local_entities[id_ent]
                

