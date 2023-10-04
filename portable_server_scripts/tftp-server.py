#pip3 install tftpy
from tftpy import TftpServer

server = TftpServer('/opt/transfer') # you need to change the share location depending on dir you are running this server

try:
    server.listen('0.0.0.0', 69)
except KeyboardInterrupt:
    pass
