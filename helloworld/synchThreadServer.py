import socket
import threading
#HOST='localhost' # or socket.gethostbyname()
#HOST='92.40.213.118'
HOST=''
PORT=8080
HEADER=64
FORMAT='utf-8'
DISCONNECT_MSG='DIS_CONN'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(f"\n socket.socket(..) returns:\n{s}\n")
s.bind((HOST,PORT))
print(f"\n socket.socket(..).bind() returns:\n{s}\n")
def handle_client(conn,addr):
    print(f"new connection {addr} connected")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len= int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
def start():
    s.listen(1)
    print(f"{HOST} listening on {PORT}")
    while True:
        conn,addr = s.accept()
        print(f"\n s.accept() returns (conn,addr):\n{conn}\n,\n{addr}")
        thread = threading.Thread(target=handle_client, args=((conn,addr)))
        thread.start()
        print(f"\n active connections:{(threading.activeCount()-1)}")
        print(f"\n thread stack size: {threading.stack_size()}")
start()
