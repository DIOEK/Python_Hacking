#step by step udp client
import socket

#host and port can be adapted for the situation 
target_host = "127.0.0.1"
target_port = 9997

#socket object
client = socet.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET informs that the host shall be IPV4 and SOCK_DGRAM says that the client is going to be UDP

#sending data
client.sendto(b"AAABBBCCC",(target_host, target_port) #sending binary data to (b"AAABBBCCC") to specified port in targer host

#recieving data
data, addr = client.recvfrom(4096) #the recvfrom function is reponsible for recieving data from specified port

print(data.decode())
client.close()

#data shall be returned with host and port details
