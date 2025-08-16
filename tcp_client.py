import socket #socket object to AF_INET e SOCK_STREAM

target_host = "www.google.com"
target_port = 80

#criating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicates IPV4 connection, SOCK_STREAM indicates TCP client

#client connection
client.connect((target_host, target_port)) #idicating host and port         

#data sending
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #data is sent as bytes

#recieving data
response = client.recv(4096) #recieving data back

#closing socking
print(response.decode())
client.close()
