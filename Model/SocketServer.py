#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
from threading import Thread

from tune_up.settings import Settings


class Server(Thread):

    def __init__(self, Settings: Settings):
        Thread.__init__(self)
        self.Settings = Settings
        self.sock = socket.socket()
        self.sock.bind(('', 9090))
        self.sock.listen(4)

        self.RPI = self.Settings.settings
    #--------------------------------------------------------------

    def run(self):
        while True:
            self.conn, self.addr = self.sock.accept()
            for i in self.RPI:
                print(self.RPI[i][0])
                if self.RPI[i][0] == self.addr[0]:
                    self.RPI[i][1] = self.conn
            print(self.RPI)

    def status(self):
            time.sleep(5)
            try:
                self.conn.send(b"Test")  # отправляем любые данные
            except BaseException:
                print('connection timed out1')  # соединение разорвано

    # def startStatus(self):
    #     thread0 = Thread(target=self.status())
    #     thread0.start()

    def stop(self):
        print("stop EXHIBITION")
        self.terminate()

    def run_video(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"run_video")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def stop_video(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"stop_video")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def disconnect(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"disconnect")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def run_projector(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"run_projector")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def stop_projector(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"stop_projector")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def run_monitor1(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"run_monitor1")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def stop_monitor1(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"stop_monitor1")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def run_monitor2(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"run_monitor2")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def stop_monitor2(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"stop_monitor2")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def run_monitor3(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"run_monitor3")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def stop_monitor3(self):
        for i in self.RPI:
            try:
                self.conn = self.RPI[i][1]
                if not self.conn is None:
                    self.conn.send(b"stop_monitor3")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

