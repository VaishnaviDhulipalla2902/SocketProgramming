from socket import *
serverName = '192.168.43.12'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,12345))
numbers = raw_input('input numbers')
clientSocket.send(numbers)
modifiednumbers = clientSocket.recv(1024)
print 'sorted order:', modifiednumbers
clientSocket.close()
