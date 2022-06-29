# 作者: Michael(phb)
# 2022年06月17日22时24分35秒
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
address = ('192.168.35.1', 2000)
client_socket.connect(address)
client_socket.send(b'python')
client_socket.close()
