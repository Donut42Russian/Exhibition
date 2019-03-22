#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Server():
    import socket

    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(4)

    RPI = {}
    #RPI['RPI1'] = ('127.0.0.1', None)
    RPI['RPI2'] = ['192.168.1.17', None]
    RPI['RPI3'] = ['192.168.1.56', None]
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
                print (te)
                print(addr[0])
        print(RPI)
    for i in RPI:
           RPI[i][1].send(b"Hello")
    while True:
        data = conn.recv(1024)
        if not data:
            print('No Data')
            break
         else:
            print(data)
    # WSA error codes
    if sys.platform.lower().startswith("win"):
        errorTab = {}
        errorTab[10004] = "The operation was interrupted."
        errorTab[10009] = "A bad file handle was passed."
        errorTab[10013] = "Permission denied."
        errorTab[10014] = "A fault occurred on the network??" # WSAEFAULT
        errorTab[10022] = "An invalid operation was attempted."
        errorTab[10035] = "The socket operation would block"
        errorTab[10036] = "A blocking operation is already in progress."
        errorTab[10048] = "The network address is in use."
        errorTab[10054] = "The connection has been reset."
        errorTab[10058] = "The network has been shut down."
        errorTab[10060] = "The operation timed out."
        errorTab[10061] = "Connection refused."
        errorTab[10063] = "The name is too long."
        errorTab[10064] = "The host is down."
        errorTab[10065] = "The host is unreachable."
         __all__.append("errorTab")
