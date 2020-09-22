import socket
import threading
import time

def dealClient(sock,addr):
    print('Accept new connetction from %s : %s ...' % addr)
    sock.send(b'Hello ,I am server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('-->>%s!' % data.decode('utf-8'))
        sock.send(('Loop_Msg:%s!' % data.decode('utf-8')).encode('utf-8'))

        sock.close()
        print('Connetction from %s:%s')
