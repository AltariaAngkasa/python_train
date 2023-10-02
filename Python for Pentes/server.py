import socket

#creating the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 192.168.43.85
host = socket.gethostname()
port = 444

#Binding to socket
serverSocket.bind(('192.168.43.85', port)) #host will be replaced/subtitued with IP,
#if changed and not running on host

#starting TCP listener
serverSocket.listen(3)

while True:
    # starting the connection
    clientsocket, address = serverSocket.accept()

    print("received connection from %s" % str(address))

    message = "hello! thank you for connecting to the server" + "\r\n"
    clientsocket.send(message.encode("ascii"))


    clientsocket.close()
