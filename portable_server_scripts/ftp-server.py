from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/opt/transfer", perm="elradfmw") # you need to change the share location depending on dir you are running this server
authorizer.add_anonymous("/opt/transfer", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
# works with python3
