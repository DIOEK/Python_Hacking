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
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer
            self.socket.send(self.buffer)
        
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                    if response:
                        print(response)
                        buffer = input('> ')
                        buffer += '\n'
                        self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('Interrupted by user')
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


