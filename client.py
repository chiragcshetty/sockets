import socket
import sys
import threading

def get_lines(sock):
    sock.settimeout(200)
    try:
        message = 'me'
        print('sending "%s"' % message)
        sock.send(message.encode())
        ip_add, machine_port = sock.getpeername();
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(64).decode()
            amount_received += len(data)
            print('received form machine:%d \n %s' % (machine_port,data))

    except socket.timeout:
           print("Done Searching")
    finally:
        print('closing socket')
        print("\n")
        sock.close()


port_list = [10000,10001,10002]

machine_list=[]
sockets   = []

print("\n\n")
for i in range(len(port_list)):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port_list[i])
    print('connecting to %s port %s' % server_address)
    try:
        s.connect(server_address)
        sockets.append(s)
        machine_list.append(i+1)
    except:
        print('%s port %s is down' % server_address)
    

print("\n\n")
machine_no = -1
for sc in sockets:
    threading.Thread(target=get_lines, args=(sc,)).start()
    
