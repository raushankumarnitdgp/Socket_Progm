#Assignment 1 tcp SERVER
#Raushan Kumar
#15/CA/406

#server
import socket

host = "127.0.0.1"
port = 9998

serversocket = socket.socket()
serversocket.bind((host, port))

serversocket.listen(1)

while True:
    clientsocket,addr = serversocket.accept()
    data = clientsocket.recv(20)
    print "Data: ",data
    message=raw_input('enter message to send to Client:')
    clientsocket.send(message)
    clientsocket.close()
    
serversocket.close()