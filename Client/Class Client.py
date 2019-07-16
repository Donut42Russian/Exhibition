import time
import socket
from threading import Thread
from tune_up.settings import Settings


class Client():

    def __init__(self, ip_server, port_server=9090):

        ##################  Настройка Сервера  ##########################
        self.sock = socket.socket()
        self.sock.bind(('', port_server))
        self.sock.listen(4)
        self.ip_server = ip_server

        self.ip = None
        self.conn = None

    def __connectclient(self):
        self.ip, self.conn = self.sock.accept()

    def Status(self):
        status_old = False
        time_old = 0
        while True:
            Time = time.time()
            if Time - time_old >= 5:
                time_old = Time
                print("OK")


test = Client()
test.Status()
