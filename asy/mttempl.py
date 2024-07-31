import threading
class Server(threading.Thread):
    factory = [] # 0 is server thread, other elements are client threads
    def __init__(self):
    '''initialize and start server thread.
    '''
    Server.factory.append(self)
    def new_client_thread(self):
    '''create and register a new client thread.
    '''
    Server.factory.append(Client())
    
class Client(threading.Thread):
    def __init__(self):
    '''initialize and start a client thread.
    '''
    self.status='running'
    Server.factory.append(self)
    def dispatch(self, char, val)
        if char == 'q':
            self.stop()
        elif char == 's':
            return self.status
        elif char =='u':
            self.status=val
