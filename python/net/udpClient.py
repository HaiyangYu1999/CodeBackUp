from socket import *

servername = '192.168.1.105'    #local host ip, use cmd ipconfig to enquire
serverPort=12000                #you send the UDP message to your PC
clientSocket = socket(AF_INET,SOCK_DGRAM)
message="this is the test sentences"
clientSocket.sendto(message.encode(),(servername,serverPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()

