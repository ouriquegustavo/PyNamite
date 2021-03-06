import threading
import socket
import time
import random
import requests
import json
import zlib

def json_eval(string):
    if not string:
        return {}
    try:
        return json.loads(string)
    except:
        return {}

class Networking():
    def __init__(self, client, ip=None, port=None):
        self.client=client
        self.data={}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip = (
            not ip and (
                socket.gethostname()=='brynhildr' 
                and '192.168.0.57' or self.get_server_ip()
            )
            or ip
        )
        self.port = port and port or 7777
        self.addr = (self.ip, self.port)

    def get_server_ip(self):
        response = requests.get('https://gleenusip.herokuapp.com/')
        if response.status_code==200:
            return response.text
            
            
            self.socket.send(str.encode(data))
            return self.socket.recv(2048).decode()
            
    def send(self, data):
        try:
            data_json = zlib.compress(json.dumps(data).encode())
            self.socket.send(data_json)
            response = self.socket.recv(2048)
            return json_eval(zlib.decompress(response).decode())
        except socket.error as e:
            print('ERROR', e)
            exit()
            
    def connection_thread(self):
        time.sleep(1)
        try:
            self.socket.connect(self.addr)
            response = self.socket.recv(2048)
            response = json_eval(zlib.decompress(response).decode())
            self.id_player = response['id_player']
            self.client.time = response['time']
            print(self.id_player, self.client.time)
        except Exception as e:
            print(e)
            
        while self.client.is_running:
            keys = self.client.controls.keys
            self.data = self.send(keys)
            #print(self.data)

    def start_client_thread(self):
        self.client_thread=threading.Thread(
            target=self.connection_thread, args=()
        )
        self.client_thread.start()
