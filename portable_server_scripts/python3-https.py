# PUT for upload and GET for download
# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
import socket, os
from socketserver import BaseServer
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import ssl

CERT = 'cert.pem'
KEY = 'key.pem'

class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ctx.load_cert_chain(certfile=CERT, keyfile=KEY)
        self.socket = ctx.wrap_socket(socket.socket(self.address_family, self.socket_type), server_side=True)
        self.server_bind()
        self.server_activate()

def test(HandlerClass = SimpleHTTPRequestHandler,
             ServerClass = SecureHTTPServer):
        server_address = ('', 443) # (address, port)
        httpd = ServerClass(server_address, HandlerClass)
        sa = httpd.socket.getsockname()
        print("Serving HTTPS on", sa[0], "port", sa[1], "...")
        httpd.serve_forever()

if __name__ == '__main__':
    test()
