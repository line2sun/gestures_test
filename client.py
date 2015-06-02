import socket

class Client(object):
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.connect(host, port)

    def connect(self, host, port):
        self.socket.connect((host, port))

    def receive(self, buff_size=1024):
        return self.socket.recv(buff_size)

    def start_recv(self):
        while True:
            msg = self.receive()
            print msg



if __name__ == '__main__':
    host = socket.gethostname()
    port = 5004

    client = Client(host, port)
    client.start_recv()