from socket import *
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_DGRAM)
print gethostbyname(gethostname())
serverSocket.bind(('',12345))
print  'the server is ready'
while 1:
	data, clientAddress = serverSocket.recvfrom(2048)
        newdata =sorted(data)
        newdata = ' '.join(reversed(newdata))
	serverSocket.sendto(newdata, clientAddress)
