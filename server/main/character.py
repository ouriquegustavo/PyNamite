
class Character():
    def __init__(self, client, id_ent, x, y):
        self.kind = 'character'
        self.client = client
        self.id_ent = id_ent
        self.x=x
        self.y=y
        
        self.width=50
        self.height=50
        
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
