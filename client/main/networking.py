import threading
import socket
import time
import random
import requests

class Networking():
    def __init__(self, client, ip=None, port=None):
        self.client=client
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
            
            
    def send(self, data):
        try:
            self.socket.send(str.encode(data))
            return self.socket.recv(2048).decode()
        except socket.error as e:
            print('ERROR', e)
            exit()
            
    def connection_thread(self):
        time.sleep(1)
        try:
            self.socket.connect(self.addr)
            self.player_id=self.socket.recv(2048).decode()
        except Exception as e:
            print(e)
            
        while self.client.is_running:
            self.data = self.send(self.client.data)
            #print(self.data)

    def start_client_thread(self):
        self.client_thread=threading.Thread(
            target=self.connection_thread, args=()
        )
        self.client_thread.start()
