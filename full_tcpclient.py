#Raushan Kumar
#15/CA/406
import socket
import thread



clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()#"127.0.0.1"
port = 9999#5005

clientSocket.connect((host, port))

def sendto_u( message,IP,PORT):
  clientSocket.sendto(message, (IP, PORT))

def recvfrom_u():
  data, addr = clientSocket.recvfrom(1024)
  print "... .Message from Server:", data


print 'CLIENT'
while True:
    message=raw_input('...')
    thread.start_new_thread ( sendto_u,(message,host,port,))

    thread.start_new_thread (recvfrom_u,())


clientSocket.close()
