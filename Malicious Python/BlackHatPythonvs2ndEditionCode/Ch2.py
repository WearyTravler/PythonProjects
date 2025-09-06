

import socket 

target_host = "www.google.com"
target_port = 80

# socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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