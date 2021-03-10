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

# SERVER #
# create socket
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind to host to listen
serversock.bind((IP, PORT))
# set 20 second timeout to stop it getting stuck
serversock.settimeout(20)
# listen for data for upto 1 connections
serversock.listen(1)

# main loop
while True:
    # accept connection to socket
    # waits until a connection is made before proceeding
    (clientsock, address) = serversock.accept()
    print("Connection from : \n", clientsock)
    clientsock.send(bytes("Hello","utf-8"))
    break
    