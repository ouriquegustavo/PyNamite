import threading
import socket
import time
import random
import json

def json_eval(string):
    if not string:
        return {}
    try:
        return json.loads(string)
    except:
        return {}

class Networking():
    def __init__(self, server, ip, port):
        self.server=server
        self.ip = ip
        self.port = port
        self.max_connections=64
        self.max_id=8192
        self.client_threads = {}
        self.client_data = {}
        self.setup_networking()
        
    def setup_networking(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.socket.bind((self.ip, self.port))
        except self.socket.error as e:
            return False
        
        self.socket.listen(self.max_connections)

        return True
        
        
    def wait_for_client_loop(self):
        print('Waiting for client connection...')
        while self.server.is_running:
            if len(self.client_threads) >= self.max_connections:
                continue
            conn, addr = self.socket.accept()
            id_player = random.randint(0,self.max_connections)
            while id_player in self.client_threads:
                id_player = random.randint(0, self.max_connections)
            client_thread=threading.Thread(target=self.client_thread, args=(conn,id_player,))
            client_thread.start()
            self.client_threads[id_player]=client_thread
        
    
    def client_thread(self, conn, id_player):
        print(id_player)
        s=time.time()
        conn.send( str(id_player).encode() )
        while self.server.is_running:
            s=time.time()
            data = conn.recv(2048).decode()
            data = json_eval(data)
            self.client_data[id_player] = data
            ####
            reply = self.gen_reply()

            conn.sendall(reply)
            
    def gen_reply(self):
        entities = {
            id_ent:ent.export_data() for id_ent, ent in
            self.server.entity_manager.entities.items()
        }
        reply = {
            'entities': entities
        }
        return json.dumps(reply).encode()
    
    def start_server_thread(self):
        self.server_thread=threading.Thread(
            target=self.wait_for_client_loop, args=()
        )
        self.server_thread.start()
