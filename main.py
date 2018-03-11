import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 3000))

sock.listen(1)

connections = []

def handler(ctn, address):
    global connections
    while True:
        data = ctn.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(ctn)
            ctn.close()
            break

while True:
    ctn, address = sock.accept()
    ctn_thread = threading.Thread(target=handler, args=(ctn, address))
    ctn_thread.daemon = True
    ctn_thread.start()
    connections.append(ctn)
    print(connections)
