import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner():
    if s.connect_ex((host, port)):
        print("The Port is closed")
    else:
        print("The port is open")

portScanner()