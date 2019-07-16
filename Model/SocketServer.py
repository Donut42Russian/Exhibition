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
        self.n = 0
        self.RPI = self.Settings.settings

        #self.RPI1 = self.RPI[0]
        #self.RPI2 = self.RPI[1]
        #self.RPI3 = self.RPI[2]
        #self.RPI4 = self.RPI[3]

    def run(self):
        while True:
            self.conn, self.addr = self.sock.accept()
            for i in self.RPI:
                print(self.RPI[i][0])
                if self.RPI[i][0] == self.addr[0]:
                    self.RPI[i][1] = self.conn
                    self.n = self.n +1
            print(self.RPI)
            # if self.n == 2:
            #     self.startControlConnection()

    # def startControlConnection(self):
    #     while self.n == 2:
    #         time.sleep(5)
    #         self.status1()
    #         self.status2()
            #self.status3()

# def status1(self):
#     print("Пошло1")
#     for i in self.RPI1:
#         if self.RPI1[1] != None:
#             try:
#                 self.conn.send(b"Test1")  # отправляем любые данные
#                 print("Дошло1")
#             except BaseException:
#                 print('connection timed out1')  # соединение разорвано
#                 self.n = self.n - 1

    # def status2(self):
    #     print("Пошло2")
    #     for i in self.RPI:
    #         if self.RPI2[1] != None:
    #             try:
    #                 self.conn.send(b"Test2")  # отправляем любые данные
    #                 print("Дошло2")
    #             except BaseException:
    #                 print('connection timed out2')  # соединение разорвано
    #                 self.n = self.n - 1

    # def status3(self):
    #     print("Пошло3")
    #     time.sleep(5)
    #     for i in self.RPI:
    #         if self.RPI[i][1] != None:
    #             try:
    #                 self.conn.send(b"Test3")  # отправляем любые данные
    #                 print("Дошло3")
    #             except BaseException:
    #                 print('connection timed out3')  # соединение разорвано
    #                 self.n = self.n - 1

    # --------------------------------------------------------------
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
