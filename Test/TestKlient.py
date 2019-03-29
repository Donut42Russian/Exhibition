# получаем данные
import socket
s_get = socket.socket()
host = socket.gethostname()
port = 12345
s_get.connect((host, port))
print(s_get.recv(1024).decode())