#pip3 install tftpy
from tftpy import TftpServer

server = TftpServer('/opt/transfer')

try:
    server.listen('0.0.0.0', 69)
except KeyboardInterrupt:
    pass
