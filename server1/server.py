import socket
import sys
import time
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        file = open("machine.1.log", "r")

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16).decode()
            print('received "%s"' % data)
            #time.sleep(10)
            if data:
                found_lines = "Lines found: \n"
                for line in file:
                    if re.search(data, line):
                        found_lines = found_lines + line

                print('sending data back to the client')
                connection.sendall(found_lines.encode())
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()