import socket
import sys


port_list = [10000,10001,10002]

machine_list=[]
sockets   = []

print("\n\n")
for i in range(len(port_list)):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port_list[i])
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    try:
        s.connect(server_address)
        sockets.append(s)
        machine_list.append(i+1)
    except:
        print >>sys.stderr, '%s port %s is down' % server_address
    

print("\n\n")
machine_no = -1
for sock in sockets:
    machine_no +=1
    try:
        message = 'find'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(64)
            amount_received += len(data)
            print >>sys.stderr, 'received form machine:\n %s' % data
    finally:
        print >>sys.stderr, 'closing socket'
        print("\n")
        sock.close()
