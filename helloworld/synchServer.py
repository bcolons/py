import socket
HOST='localhost'
PORT=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr =s.accept()
print("Connected to", addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
    print(conn)
conn.close()
