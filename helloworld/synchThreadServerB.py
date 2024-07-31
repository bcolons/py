import socket
import time
import threading
#HOST='localhost' # or socket.gethostbyname()
#HOST='92.40.213.118'
HOST='localhost'
PORT=8080
HEADER=6400
FORMAT='utf-8'
DISCONNECT_MSG='DIS_CONN'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
t=time.time()
print(f"{t} socket.socket(..) returns: {s}\n")
s.bind((HOST,PORT))
t=time.time()
print(f"{t} socket.socket(..).bind() returns: {s}\n")
def handle_client(conn,addr):
    print(f"{time.time()} new connection conn,addr -- {conn},{addr} -- connected")
    connected = True
    while connected:
        msg_raw = conn.recv(HEADER).decode(FORMAT)
        if msg_raw:
            try: 
                print(f"{time.time()} msg_raw=conn.recv(HEADER) is: {msg_raw}\n")
                msg_raw= int(msg_raw)
                msg = conn.recv(msg_raw).decode(FORMAT)
                print(f"{time.time()} msg=conn.recv(msg_raw).decode(utf8) is: {msg}\n")
                if msg == DISCONNECT_MSG:
                    conn.close()
            except ValueError:
                print(f"{time.time()} ValueError: msg_raw = conn.recv(HEADER) not an int\n")
def start():
    s.listen(1)
    print(f"{time.time()} {HOST} listening on {PORT}")
    while True:
        conn,addr = s.accept()
        print(f"\n{time.time()} s.accept() returns (conn,addr):\n{conn}\n,\n{addr}")
        thread = threading.Thread(target=handle_client, args=((conn,addr)))
        thread.start()
        print(f"\n{time.time()} active connections:{(threading.activeCount()-1)}")
        print(f"\n{time.time()}  thread stack size: {threading.stack_size()}")
start()
