# 作者: Michael(phb)
# 2022年06月16日20时32分57秒
from socket import *

server = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM代表tcp
server_addr = ('', 2000)
server.bind(server_addr)
server.listen(10)
# 有新的客户端来连接服务器，那么就产生一个新的套接字专门为这个客户端服务
new_socket, _ = server.accept()
data = new_socket.recv(1024)
print(data.decode('utf8'))
new_socket.send('python'.encode('utf8'))
new_socket.close()
server.close()
