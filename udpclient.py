#Assignment 1 UDP Client
#Raushan Kumar
#15/CA/406

import socket

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP


UDP_IP = "127.0.0.1"
UDP_PORT = 5004

print 'CLIENT'
while True:
  message=raw_input('Enter the message to server:')
  clientSock.sendto(message, (UDP_IP, UDP_PORT))
  data, addr = clientSock.recvfrom(100)
  print "Message from Server:", data
  
clientSock.close()
