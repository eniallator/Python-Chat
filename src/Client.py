import socket
import threading


class Client:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, nickname, address):
        self.sock.connect((address, 3000))
        self.nickname = nickname


    def send_msg(self):
        while True:
            prefix = '<' + self.nickname + '>: '
            self.sock.send(bytes(prefix + input(''), 'utf-8'))
    

    def run(self):
        inp_thread = threading.Thread(target=self.send_msg)
        inp_thread.daemon = True
        inp_thread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
