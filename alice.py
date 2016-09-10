#!/usr/bin/env python
'''
This is an simple implementation of the Diffie-Hellman keys exchange algorithm.

Mateus-n00b, Setembro 2016

Version 1.0

License GPL
Execute-me first!
'''

import os,json
from socket import *
import random

tcp = socket(AF_INET,SOCK_STREAM)
tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp.bind(('',2222))
tcp.listen(2)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
TEMP = {}
FOO = ''

# ------------------------------------
# Generating vars
# My secret number
a = random.randint(1,35535)
# My prime number
p = random.choice(PRIMES)

#My basestring
g = random.randint(1,35535)
# ------------------------------------
# Wainting for requests
TEMP = {'p':p,'base':g}
conn, addr = tcp.accept()
while 1:
    msg = conn.recv(1024)
    if "NEGOCIATION" in msg:
        conn.send(json.dumps(TEMP)) 
        print "Sending base and prime number..."
        break
# Calculating A = g^a mod p
A = (g**a)%p
# Receiving B = g^a mod p
msg = conn.recv(1024)
FOO = json.loads(msg)

# Calculating s = B^a mod p 
B = FOO['B']
s = (B ** a)%p 

#Sending my A = g^a mod p
print "Sending my g^a mod p"
TEMP = {'A':A}
conn.send(json.dumps(TEMP))

print "The secret is %d " % (s)