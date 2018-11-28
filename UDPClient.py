from socket import *
serverName = '192.168.43.12'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)
data = raw_input('enter the numbers:')
clientSocket.sendto(data,('',serverPort))
newdata, serverAddress = clientSocket.recvfrom(2048)
print 'In sorted Order:',newdata
clientSocket.close()
