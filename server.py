#!/usr/bin/env python

import SocketServer

clients = []

class ChatHandler(SocketServer.BaseRequestHandler):
    def setup(self):
        clients.append(self)
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            for client in clients:
                if client != self:
                    try:
                        client.request.send(data)
                    except:
                        clients.remove(client)
    def finish(self):
        clients.remove(self)

if __name__ == "__main__":
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 1234), ChatHandler)
    server.serve_forever()
