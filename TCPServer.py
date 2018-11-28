from socket import *
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
print gethostbyname(gethostname())
serverSocket.bind(('',12345))
serverSocket.listen(1)
print ' Server is ready'
while 1:
 	connectionsocket, address = serverSocket.accept()
	print 'Connection established'
	numbers = connectionsocket.recv(1024)
	l1 = [int(x) for x in numbers.split()]
	l2 = l1.sort()
	l1 = [str(x) for x in l1]
	new = " "
	for p in l1:
		new = new + p + " "
	connectionsocket.send(new)
	print 'Connection closed'
	connectionsocket.close()
