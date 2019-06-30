import socket
from threading import Thread

clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.101', 7777)
sock.bind(server_address)


def acceptConnection():
    sock.listen(100)
    while True:
        connection, client_address = sock.accept()
        if connection is not None:
            addresses[connection] = client_address
            print('CONNECTED')
        Thread(target=handleConnection, args=(connection,)).start()


def handleConnection(connection):
    name = connection.recv(1024).decode("utf8")
    clients[connection] = name
    while True:
        msg = connection.recv(1024)
        broadcast(msg)


def broadcast(msg, prefix=''):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


ACCEPT_THREAD = Thread(target=acceptConnection)
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
sock.close()