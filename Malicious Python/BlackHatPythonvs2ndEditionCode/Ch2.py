
#1st edition

# Modules and their functions...
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM





# TCP CLIENT
#-----------------------------------------------------------------

def tcp_client(target_host, target_port):

  # socket obj
  client = socket(AF_INET, SOCK_STREAM)

## AF_INET = using ipv4 addressing or hostnaming
## SOCK_STREAM = indicates a TCP client

# making a lot of assumptions...


# connect to the client
  client.connect((target_host, target_port))

# send data
  client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
  
# receive data
  response = client.recv(4096)

  print(response)
#-----------------------------------------------------------------



# UDP ClIENT
#-----------------------------------------------------------------

def udp_client(target_host, target_port):

  # sock obj
  client = socket(AF_INET, SOCK_DGRAM) # This time using DGRAM for UDP, a connectionless protocol

## AF_INET = using ipv4 addressing or hostnaming
## SOCK_STREAM = indicates a TCP client

# making a lot of assumptions...


# connect to the client
  client.connect((target_host, target_port))

# send data
  client.sendto(b"AAABBBCCC",(target_host, target_port))

# receive some data
  data, addr = client.recvfrom(4096)

  print(data)


#-----------------------------------------------------------------


# TCP SERVER
#-----------------------------------------------------------------






# main
def main():
  print("Welcome to the simple TCP/UDP/Server!")
  target_host = input("Give me the target: ")
  target_port = input("Give me the port: ")
  tcp_or_udp = input("Would you like a TCP/UDP client? [T/U]: ")
  if tcp_or_udp == "T":
    tcp_client(target_host, int(target_port))
  elif tcp_or_udp == "U":
    udp_client(target_host, int(target_port))
  else:
    return "Sorry that's not a valid input..."



main()