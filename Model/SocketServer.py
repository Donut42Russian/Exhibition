#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from threading import Thread


class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket()
        self.sock.bind(('', 9090))
        self.sock.listen(4)
        self.RPI = {}
        # RPI['RPI1'] = ('127.0.0.1', None)
        self.RPI['RPI2'] = ['192.168.1.56', None]
        self.RPI['RPI3'] = ['192.168.1.187', None] #192.168.1.171
        # RPI['RPI4'] = ('127.0.0.1', None)


    def run(self):
        while True:
            conn, addr = self.sock.accept()
            for i in self.RPI:
                print(self.RPI[i][0])
                if self.RPI[i][0] == addr[0]:
                    self.RPI[i][1] = conn
                    print(addr[0])

            print(self.RPI)

    def get_message(self):
        data = test.conn.recv(1024)
        print(data)

    def run_video(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"run_video")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def stop_video(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"stop_video")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def disconnect(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"disconnect")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1



    def run_projector(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"run_projector")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1

    def stop_projector(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"stop_projector")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def run_monitor1(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"run_monitor1")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def stop_monitor1(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"stop_monitor1")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def run_monitor2(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"run_monitor2")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def stop_monitor2(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send (b"stop_monitor2")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def run_monitor3(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"run_monitor3")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


    def stop_monitor3(self):
        for i in self.RPI:
            try:
                conn = self.RPI[i][1]
                if not conn is None:
                    conn.send(b"stop_monitor3")
                else:
                    return 0
            except socket.error as e:
                print('error', str(e))
                return 0
        return 1


if __name__ == '__main__':
    test = Server()
    test.connect()
