#Assignment 1 UDP Server
#Raushan  Kumar
#15/CA/406


import socket
import thread

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
serverSocket.bind((UDP_IP, UDP_PORT))

def sendto_u(message,saddr):
  serverSocket.sendto(message,addr)

def recvfrom_u():
  data, addr = serverSocket.recvfrom(100)
  print "Message from client ... .. :", data

print 'SERVER'

data, addr = serverSocket.recvfrom(100)
print "Message from client .. ... :", data

while True:
       thread.start_new_thread (recvfrom_u,())
       message=raw_input('... .')
       thread.start_new_thread(sendto_u,( message,addr,))
       
serverSocket.close()
