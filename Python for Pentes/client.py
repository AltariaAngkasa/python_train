import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.43.85'
host = socket.gethostname()
port = 444

clientsocket.connect(('192.168.43.85', port))

message = clientsocket.recv(1024) # maximum amount of data your client

clientsocket.close()

print(message.decode('ascii'))
