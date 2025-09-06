
# Modules and their functions...
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM





# TCP CLIENT
#-----------------------------------------------------------------
target_host = "www.google.com"
target_port = 80

# socket obj
client = socket(AF_INET, SOCK_STREAM)

## AF_INET = using ipv4 addressing or hostnaming
## SOCK_STREAM = indicates a TCP client

# making a lot of assumptions...


# connect to the client
client.connect((target_host, target_port))

# send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response)
#-----------------------------------------------------------------



# UDP ClIENT
#-----------------------------------------------------------------
target_host = "127.0.0.1"
target_port = 80

# sock obj
client = socket(AF_INET, SOCK_DGRAM) # This time using DGRAM for UDP, a connectionless protocol

# send data
client.sendto("AAABBBCCC",(target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)
#-----------------------------------------------------------------