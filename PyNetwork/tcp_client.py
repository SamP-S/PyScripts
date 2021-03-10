import socket

# create scocket
# AF_INET = ipv4
# AF_INET6 = ipv6

# SOCK_STREAM = TCP
# SOCK_DGRAM = UDP

IP = socket.gethostname()   # public ip
IP = "127.0.0.1"    # local ip
IP = "localhost"    # local ip
PORT = 5005

# CLIENT #
# create socket
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
try:
    clientsock.connect((IP, PORT))
    buff = clientsock.recv(1024)
    print(buff.decode("utf-8"))
except socket.error as err:
    print("Failed to connect to server:\n", err)

clientsock.close()