#!/usr/bin/env python
'''
This is an simple implementation of the Diffie-Hellman keys exchange algorithm.

Mateus-n00b, Setembro 2016

Version 1.0

License GPL

'''
import os,json
from socket import *
import random

tcp = socket(AF_INET,SOCK_STREAM)
TEMP = ''
DICT = {}


tcp.connect(('localhost',2222))
tcp.send('NEGOCIATION')

msg = tcp.recv(1024)
TEMP = json.loads(msg)
#-----------------------------------
# Generating vars
# My secret number
a = random.randint(1,35535)
# The prime number
p = TEMP['p']

# The base
g = TEMP['base']

#-----------------------------------
# Calculating A = g^a mod p
B = (int(g)**a)%int(p)
DICT = {'B':B}

# Sending my B = g^a mod p
print "Sending my g^a mod p"
tcp.send(json.dumps(DICT))

# Receiving B = g^a mod p
msg = tcp.recv(1024)
TEMP = json.loads(msg)
A = TEMP['A']

# Calculating s = A ^ a mod p
s = (A**a)%p
print "The secret is %d" % (s)