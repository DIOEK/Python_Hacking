#Generic Listener made using netcat as a base

#necessary libraries
import argparse
import socket
import shlex
import subprocess #important for client interaction and process creation
import sys
import textwrap
import threading

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
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='archive uploading')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()

