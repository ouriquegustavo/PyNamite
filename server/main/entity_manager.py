

class EntityManager():
    def __init__(self, client):
        self.client=client
        self.entities = {}
        self.id_max = 8192
        
        
    def create_entity(self, obj, id_ent, **args):
        ent = obj(self.client, id_ent, **args)
        self.entities[id_ent]=ent
        return ent
