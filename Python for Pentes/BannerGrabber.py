import socket


def banner(ip_addr, port):
    s = socket.socket()
    s.connect((ip_addr, int(port)))
    # s.settimeout(5)
    print(str(s.recv(1024)).strip('b'))

def main():
    ip_addr = input("Please enter the IP: ")
    port = str(input("Please enther the port: "))
    banner(ip_addr, port)

main()


#####################TESTING#######################
#import socket

# def banner(ip_addr, port):
#     try:
#         s = socket.socket()
#         s.connect((ip_addr, int(port)))
#         print(s.recv(1024))
#         s.close()
#     except ConnectionRefusedError:
#         print("Koneksi ditolak. Pastikan server berjalan dan port tersedia.")
#     except Exception as e:
#         print(f"Terjadi kesalahan: {e}")
#
# def main():
#     ip_addr = input("Please enter the IP: ")
#     port = input("Please enter the port: ")
#     banner(ip_addr, port)
#
# if __name__ == "__main__":
#     main()
