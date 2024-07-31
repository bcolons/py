import socket
import time
HOST='localhost' # or socket.gethostbyname()
PORT=8000
HEADER=64
FORMAT='utf-8'
DISCONNECT_MSG='DIS_CONNNNNN'
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(f"socket.socket(..) {c}\n")
c.connect((HOST,PORT))
def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    if msg_len:
        send_length = str(msg_len).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        c.send(send_length)
        c.send(message)
print(f"post connect:\n socket.socket(..) {c}\n")
send("123")
time.sleep(2)
send("12345")
time.sleep(2)
send("12345678")
time.sleep(2)
send("12")
time.sleep(2)
send(DISCONNECT_MSG)

"""===

def handle_client(conn,addr):
    print(f"new connection {addr} connected")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        msg_len= int(msg_len)
        msg = conn.recv(msg_len).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
def start():
    s.listen(1)
    print(f"listening on {PORT}")
    while True:
        conn,addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"\n active connections:{(threading.activeCount()-1)}")
"""
