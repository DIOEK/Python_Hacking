import socket #objeto socket para os parâmetros AF_INET e SOCK_STREAM

target_host = "www.google.com"
target_port = 80

#criar objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indica que o endereço ou nome de host será IPV4, SOCK_STREAM indica que o cliente será TCP

#conectar com o cliente
client.connect((target_host, target_port)) #conexão com o client         

#enviar alguns dados
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #dados são enviados como bytes

#receber alguns dados
response = client.recv(4096) #receber alguns dados de volta

#fechar o socket
print(response.decode())
client.close()
