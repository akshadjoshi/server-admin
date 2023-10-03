# generate a self-signed SSL/TLS certificate using OpenSSL
# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
# PUT for upload and GET for download

import BaseHTTPServer, SimpleHTTPServer
import ssl


httpd = BaseHTTPServer.HTTPServer(('0.0.0.0',443),
        SimpleHTTPServer.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="key.pem",
        certfile='cert.pem', server_side=True)

httpd.serve_forever()
