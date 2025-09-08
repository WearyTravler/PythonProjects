
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

import threading, errno

def server_spawn():
  bind_ip = "0.0.0.0"
  bind_port = input("Which port would you like to use: ")
  server = socket(AF_INET, SOCK_STREAM)

  server.bind((bind_ip, bind_port))

  server.listen(5)

  print("[*] Listening on %s:%d" %(bind_ip, bind_port))

  # client-handling thread
  def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    #send back a packet
    client_socket.send("ACK!")

    client_socket.close()

  while True:
    client,addr = server.accept()
    print("[*] Accepted connection from: %s:%d " % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()








# main
def main():
  print("Welcome to the simple TCP/UDP/Server!")
  choice = input("Would you like a TCP/UDP client or possibly spawn a local server? [T/U/S]: ")
  target_host = input("Give me the target: ")
  target_port = input("Give me the port: ")
  if choice == "T":
    tcp_client(target_host, int(target_port))
  elif choice == "U":
    udp_client(target_host, int(target_port))
  elif choice == "S":
    server_spawn()
  else:
    return "Sorry that's not a valid input..."



main()