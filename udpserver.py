#Assignment 1 UDP Server
#Raushan Kumar
#15/CA/406


import socket




UDP_IP = "127.0.0.1"
UDP_PORT = 5004


serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
serverSocket.bind((UDP_IP, UDP_PORT))
print 'SERVER'
while True:
       data, addr = serverSocket.recvfrom(100)
       print "received message:", data
       message=raw_input('enter message to send to Client:')
       serverSocket.sendto(message, addr)
       
serverSocket.close()
#comment