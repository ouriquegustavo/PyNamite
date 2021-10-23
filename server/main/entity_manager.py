

class EntityManager():
    def __init__(self, client):
        self.client=client
        self.entities = {}
        self.id_max = 8192
        
        
    def create_entity(self, obj, id_ent, **args):
        ent = obj(self.client, id_ent, **args)
        self.entities[id_ent]=ent
        return ent
        
    def update(self):
        remove_list=[]
        for id_ent, ent in self.entities.items():
            if hasattr(ent, 'remove') and ent.remove:
                remove_list.append(id_ent)
        for id_ent in remove_list:
            del self.entities[id_ent]
