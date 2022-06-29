# 作者: Michael(phb)
# 2022年06月15日16时28分08秒
from socket import *
import sys

# 创建套接字
server = socket(AF_INET, SOCK_DGRAM)

# 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
# local_addr = ('', 2000)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
local_addr = (sys.argv[1], 2000)
server.bind(local_addr)

# 等待接收对方发送的数据,1024表示本次接收的最大字节数
recv_data = server.recvfrom(1024)

# 显示接收到的数据
print(recv_data[0].decode('utf8'))
print(recv_data[1])  # 这里是对方的ip地址和端口号

# 给客户端发送数据
server.sendto('world'.encode('utf8'), recv_data[1])
server.close()
