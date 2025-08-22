#Generic Listener made using netcat as a base

#necessary libraries
import argparse #creates command line interface
import socket
import shlex
import subprocess #important for client interaction and process creation
import sys
import textwrap
import threading

#NetCat client class
class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object created
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

    def run(self):
        if self.args.listen:
            self.listen() #for listener
        else:
            self.send() # for client

    def send(self):
        self.socket.connect((self.args.target, self.args.port)) # establishes connection to target and port
        if self.buffer #if buffer sends it first to target
            self.socket.send(self.buffer)
        
        try: #try catch allows Ctrl-C out of programe execution
            while True: #loop for data receiving, breaks if there is no data anymore
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                    if response: #if there is a response, there is output
                        print(response)
                        buffer = input('> ')
                        buffer += '\n'
                        self.socket.send(buffer.encode())#sends interactive response, loop continues
        except KeyboardInterrupt: #ctrl-c exit
            print('Interrupted by user')
            self.socket.close()
            sys.exit()
    
    def listen(self):
        self.socket.bind((self.args.target, self.args.port)) #sets connection to target and port
        self.socket.listen(5)
        while True: #loop that initiates listening
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                    target=self.handle, args=(client_socket,) #sends connected socket to handle
            )
            client_thread.start()
    
    def handle(self, client_socket): # executes arg that program was set to

        if self.args.execute: #block for command execution
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload: #block for uploading
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.sed(message.encode())

        elif self.args.command: #block for shell creation
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server closed {e}')
                    self.socket.close()
                    sys.exit()

#execute function that recieves commands
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = suprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT) #check output method for executing commands in system and pushing outputs
    return output.decode()

#main block
if __name__)) == '__main__':
    parser = argparse.ArgumentParser(
            description='BHP Net Tool',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:
                netcat.py -t 192.168.1.108 -p 5555 -l -c #command shell
                netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #archive upload
                netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # command
                                                                             # execution
                echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 #sending text to
                                                                 # server door 135
                netcat.py -t 192.168.1.108 -p 5555 #server connection
            '''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell') #configures interactive shell (needs -l)
    parser.add_argument('-e', '--execute', help='execute specified command') #executes specific commands (needs -l)
    parser.add_argument('-l', '--listen', action='store_true', help='listen') #configures listener
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port') #sets target port
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP') #specifies IP
    parser.add_argument('-u', '--upload', help='archive uploading') #uploads a selected archive (needs -l)
    args = parser.parse_args()
    if args.listen: 
        buffer = '' #if set as a listener the buffer string must be empty
    else: #if set in client mode, the content from the stdin buffer is sent instead
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()


