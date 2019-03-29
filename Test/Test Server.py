import socket

# слушаем и отправляем данные
s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind((host, port))

s.listen(4)
while True:
    c, addr = s.accept()
    print('adr：', addr)
    c.send(b'test')
    c.close()