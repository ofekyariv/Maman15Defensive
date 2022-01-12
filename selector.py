import socket
import selectors
import logging


class Selector:
    def __init__(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.bind(('localhost', port))
            self.s.listen(100)
            self.s.setblocking(False)
            self.sel = selectors.DefaultSelector()
            self.sel.register(self.s, selectors.EVENT_READ, self.accept)
            self.run_server()

    def accept(self, sock, mask):
        conn, addr = sock.accept()
        logging.info(f'accepted connection from {addr}')
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn, mask):
        full_data = b''
        data = conn.recv(1024)
        conn.send(data)
        '''while data:
            full_data += data
            logging.info(f'got {repr(data)} from {conn}')
            data = conn.recv(1024)'''
        logging.info(f'closing {conn}')
        self.sel.unregister(conn)
        conn.close()

    def run_server(self):
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)
