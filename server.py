#!/usr/bin/env python

import SocketServer

clients = []

class ChatHandler(SocketServer.BaseRequestHandler):
    """
    One instance of this class gets instantiated per client by the
    ThreadingTCPServer.
    """
    def setup(self):
        """
        This function gets called after a client connects. We want to add the
        client to a global list of clients, so we can later send it messages
        """
        clients.append(self)
    def handle(self):
        """
        This function gets called to recieve the user's input. We loop forever,
        asking for more data. When we get it, we loop through the list of
        clients, sending each one the text we recieved.
        """
        while True:
            data = self.request.recv(1024).strip()
            for client in clients:
                if client != self:
                    try:
                        client.request.send(data)
                    except:
                        clients.remove(client)
    def finish(self):
        """
        This function gets called when the client disconnects. When this
        occurs, we remove it from the list of clients so we stop sending it
        new messages
        """
        clients.remove(self)

# Run this code if this is the main file (i.e., it's not being included elsewhere
if __name__ == "__main__":
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 1234), ChatHandler)
    server.serve_forever()
