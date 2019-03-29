#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Server():
    import socket

    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(4)

    RPI = {}
    #RPI['RPI1'] = ('127.0.0.1', None)
    RPI['RPI2'] = ['192.168.1.56', None]
    RPI['RPI3'] = ['192.168.1.171', None]
    #RPI['RPI4'] = ('127.0.0.1', None)
    print(len(RPI))
    te = 0
    while te != len(RPI):
        conn, addr = sock.accept()

        for i in RPI:
            print(RPI[i][0])
            if RPI[i][0] == addr[0]:
                RPI[i][1] = conn
                te += 1
                print(te)
                print(addr[0])
        print(RPI)
    for i in RPI:
           RPI[i][1].send(b"run_video")
           RPI[i][1].send(b"stop_video")
    while True:
        data = conn.recv(1024)
