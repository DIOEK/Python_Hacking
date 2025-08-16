#generic TCP server
import socket
import threading #must be imported so that the server can support multiple connections

IP = "0.0.0.0"
PORT = 9998

#main function 
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) #passing the ip and port that we want the server to listen to 
    server.listen(5) #setting that this server can listen to a total of five clients
    print(f'[*] Listening in {IP}:{PORT}')
    
    #setting up the main loop, waiting for an entry connection
    while True: 
        client, address = server.accept() #accept() returns a tuple, the first component of it being sent to client and the second sent to address, which by itself is another tuple
        print(f'[*] Connection accepted from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,)) #setting the new thread that handles the connection, args being the one element tuple that's passed to 
        client_handler.start() #initiates the client connection thread and reestarts the loop making it ready for another connection

def handle_client(client_socket):
    with client_sock as sock: 
        request = sock.recv(1024) # sets maximum buffer size to 1024 bytes or 1KB
        print(f'[*] Received: {resquest.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ = '__main__': #this server can be integrated inside other projects
    main()

