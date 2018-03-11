import sys
from src.Server import Server
from src.Client import Client

if len(sys.argv) > 1:
    client = Client(sys.argv[1], sys.argv[2])
    client.run()
else:
    server = Server()
    server.run()
