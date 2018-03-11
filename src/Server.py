import socket
import threading


class Server:

    connections = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.sock.bind(('0.0.0.0', 3000))
        self.sock.listen(1)


    def handler(self, ctn, address):
        while True:
            data = ctn.recv(1024)
            for connection in self.connections:
                if connection != ctn:
                    connection.send(bytes(data))
            if not data:
                print(str(address[0]) + ':' + str(address[1]) + ' disconnected')
                self.connections.remove(ctn)
                ctn.close()
                break

    def run(self):
        while True:
            ctn, address = self.sock.accept()
            ctn_thread = threading.Thread(target=self.handler, args=(ctn, address))
            ctn_thread.daemon = True
            ctn_thread.start()
            self.connections.append(ctn)
            print(str(address[0]) + ':' + str(address[1]) + ' connected')
