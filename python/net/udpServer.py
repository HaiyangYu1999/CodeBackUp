from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print('This server is ready to receive.')
while True:
    message,addr=serverSocket.recvfrom(2048)
    capitalizedSentence=message.upper()
    serverSocket.sendto(capitalizedSentence,addr)