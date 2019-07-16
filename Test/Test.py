import socket
import time
from threading import Thread
from tune_up.settings import Settings


class Client(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket()
        self.sock.bind(("192.168.1.56", 9091))
        self.sock.listen(4)

        pathSettings = r'C:\Users\admin\Desktop\Project\Exhibition\Test\settingsTest'
        self.testSettings = Settings(pathSettings)
        self.RPI = self.testSettings.settings

    def run(self):
        while True:
            self.conn, addr = self.sock.accept()
            for i in self.RPI:
                print(self.RPI[i][0])
                if self.RPI[i][0] == addr[0]:
                    self.RPI[i][1] = self.conn
            print(self.RPI)

    def status(self):
        while True:
            time.sleep(1)
            try:
                self.conn.send(b"Test")  # отправляем любые данные
            except BaseException:
                print('connection timed out1')  # соединение разорвано

    def startStatus(self):
        thread0 = Thread(target=self.status())#, daemon=True
        thread0.start()


test = Client()
test.start()
test.startStatus()
