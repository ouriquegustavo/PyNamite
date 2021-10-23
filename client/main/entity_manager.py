from main.character import Character

class EntityManager():
    def __init__(self, client):
        self.client=client
        self.entities = {}
        self.id_max = 8192
        self.kind_from_to = {
            'character': Character,
        }
        
        
    def create_entity(self, obj, id_ent, **kwargs):
        ent = obj(self.client, id_ent, **kwargs)
        self.entities[id_ent]=ent
        return ent
        
        
    def update(self):
        remove_list=[]
        for id_ent, data in self.client.networking.data['entities'].items():
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
            if hasattr(ent, 'remove') and ent.remove:
                remove_list.append(id_ent)
        for id_ent in remove_list:
            del self.entities[id_ent]
