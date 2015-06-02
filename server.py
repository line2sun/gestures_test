import socket


class GesturesSocketServer(object):
    """
    This class is a server that redirects the text messages to a client.
    """
    __MAX_CONNECTIONS = 5

    def __init__(self, host, port):
        self.conn_pool = []
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind()


    def bind(self):
        self.socket.bind((self.host, self.port))

    def start_listening(self):
        self.socket.listen(self.__MAX_CONNECTIONS)

    def start(self):
        self.start_listening()
        while True:
            print 'True'
            if len(self.conn_pool) < 2:
                conn, addr = self.socket.accept()
                print "Got a connection from: ", addr
                self.conn_pool.append((conn, addr))

            msg = self.receive()
            if not msg == '':
                print msg
                try:
                    self.send(1, msg)
                except IndexError:
                    print "there is no other external connections"
            elif msg == 'X':
                self.send(1, 'Server is shutting down!')
                self.close_conn(1)
                self.close_conn(0)
            else:
                continue

    def send(self, conn_id, msg):
        self.conn_pool[conn_id][0].send(msg)

    def receive(self):
        return self.conn_pool[0][0].recv(1024)

    def close_conn(self, conn_id):
        self.conn_pool[conn_id][0].shutdown(socket.SHUT_RDWR)
        self.conn_pool[conn_id][0].close()



if __name__ == '__main__':
    host = socket.gethostname()
    port = 5004

    #import pdb
    #pdb.set_trace()
    server = GesturesSocketServer(host, port)
    server.start()