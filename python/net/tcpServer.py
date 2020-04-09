from socket import *
serverPort=12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print('This server is ready to receive.')
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024)
    upper=sentence.upper()
    connectionSocket.send(upper)
    connectionSocket.close()