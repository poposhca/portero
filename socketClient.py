import socket

def sendMessage(HOST, PORT, data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(data)
    data = s.recv(1024)
    print('Received', repr(data))
    s.close()
    return repr(data)
