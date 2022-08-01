# 作者: Michael(phb)
# 2022年06月17日23时54分30秒
from socket import *
import struct

client_socket = socket(AF_INET, SOCK_STREAM)

address = ('192.168.35.1', 2000)

client_socket.connect(address)

# 接文件名
file_name_len = client_socket.recv(4)  # 先接文件名大小
file_name = client_socket.recv(struct.unpack('I', file_name_len)[0])  # 再接文件名

f = open('【接收】' + file_name.decode('utf8'), 'wb')
# 接文件内容
file_content_len = client_socket.recv(4)  # 先接文件内容大小
file_content = client_socket.recv(struct.unpack('I', file_content_len)[0])  # 再接文件内容
# 写入文件内容
f.write(file_content)
f.close()
client_socket.close()
