import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432       # Port to listen on (non-privileged ports are > 1023)

goodAns = "SI|Invitado: ALEX TRE para el 12/03/19"
badAnd = "NO|El CODIGO presentado es INVALIDO"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Server listening')
while True:
    conn, addrs = s.accept()
    data = conn.recv(1024)
    if not data: break
    conn.sendall(goodAns)
conn.close()