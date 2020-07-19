import socket
import os
import time
import logging

a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host,port = 'localhost',3133

a.bind((host,port))

a.listen(5)

print('server is listening.....from: ',host)

conn,addr = a.accept()
print('reveive form:',addr)
# print(conn.recv(4096).decode()) # 1 receive......

# connection established......
logging.basicConfig(level=logging.INFO,format='%(asctime)s--%(message)s')

while True:
    data = conn.recv(4096).decode()
    logging.info(data)
    pass
