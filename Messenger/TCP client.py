# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 00:07:04 2016

@author: Auditore
"""

from socket import *

HOST = '127.0.0.1' or 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
print('Testing client')
while True:
    data = bytes(input('C>'), 'utf-8')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print('S>', data.decode('utf-8'))
    
tcpCliSock.close()
