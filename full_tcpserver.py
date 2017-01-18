#Raushan Kumar
#15/CA/406
#server
import socket
import thread

host = socket.gethostname()#"127.0.0.1"
port = 9999#5005

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen(5)
def sendto_u(message,saddr):

  clientsocket.sendto(message,addr)

def recvfrom_u():
  data, addr = clientsocket.recvfrom(1024)
  print "Message from client ... .. :", data




print 'SERVER'

clientsocket,addr = serversocket.accept()
data = clientsocket.recv(1024)
print "Message from client .. ... :", data




while True:
    thread.start_new_thread (recvfrom_u,())
    message=raw_input('... .')
    thread.start_new_thread(sendto_u,( message,addr,))
    #clientsocket.close()

serversocket.close()
