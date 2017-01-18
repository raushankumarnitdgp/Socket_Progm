#Assignment 1 UDP Client
#Raushan Kumar
#15/CA/406

import socket
import thread


UDP_IP = "127.0.0.1"
UDP_PORT = 5006
  
clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP


def sendto_u( message,IP,PORT):
  clientSock.sendto(message, (IP, PORT))
  
def recvfrom_u():
  data, addr = clientSock.recvfrom(100)
  print "... .Message from Server:", data


print 'CLIENT'
while True:
  message=raw_input('...')
  thread.start_new_thread ( sendto_u,(message,UDP_IP,UDP_PORT,))
  
  thread.start_new_thread (recvfrom_u,())
  
  
clientSock.close()
