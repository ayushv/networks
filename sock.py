import socket

MSGLEN = 1000000

class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        sent = self.sock.send(msg)

    def myreceive(self):
        result = ""
        data = self.sock.recv(1024)
        while len(data)>0 :
            result+=data
            data = self.sock.recv(1024)
        return result

    def cls(self):
        self.sock.shutdown(socket.SHUT_RDWR)