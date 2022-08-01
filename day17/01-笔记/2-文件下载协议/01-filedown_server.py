# 作者: Michael(phb)
# 2022年06月17日23时34分23秒
from socket import *
import struct

server_socket = socket(AF_INET, SOCK_STREAM)

# 端口重用
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

address = ('192.168.35.1', 2000)
server_socket.bind(address)
server_socket.listen(10)
client_socket, client_addr = server_socket.accept()
print(client_addr)

file_name = 'Readme'
# 发文件名长度
b_file_name = file_name.encode('utf8')
client_socket.send(struct.pack('I', len(b_file_name)))  # 整型对象转化为字节流
# 发文件名
client_socket.send(b_file_name)
# 发文件内容
f = open(file_name, 'rb')
content = f.read()
# 发内容长度
client_socket.send(struct.pack('I', len(content)))
# 发内容
client_socket.send(content)

f.close()
client_socket.close()
server_socket.close()
