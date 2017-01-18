#Assignment 1 TCP client
#Raushan Kumar
#15/CA/406

import socket


clientSocket = socket.socket()


host = "127.0.0.1"
port = 9998

clientSocket.connect((host, port))
while True:
    message=raw_input('Enter the message to server:')
    clientSocket.sendto(message, (host,port))
    recvdata = clientSocket.recv(20)
    print "Message from Server:", recvdata
clientSocket.close()



