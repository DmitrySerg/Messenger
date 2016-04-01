# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:33:49 2016

@author: Auditore
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print('C>', data.decode('utf-8'))
        
        data = bytes(input('S>'), 'utf-8')
        if not data:
            break
        tcpCliSock.send(data)
    tcpCliSock.close()
tcpSerSock.close()
        
        

        
        
    
