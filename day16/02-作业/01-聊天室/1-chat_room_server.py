# 作者: Michael(phb)
# 2022年06月16日21时16分57秒
from socket import *
import sys
import select

server_socket = socket(AF_INET, SOCK_STREAM)
# 设置端口重用
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
address = ('192.168.221.128', 2000)
server_socket.bind(address)
server_socket.listen(100)

epoll = select.epoll()
# 注册要监控的描述符
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(server_socket.fileno(), select.EPOLLIN)

# 用来存放聊天室每个用户的client_socket
client_list = []

while True:
    events = epoll.poll()
    for fd, event in events:
        if fd == server_socket.fileno():  # 有连接请求
            client_socket, client_addr = server_socket.accept()
            print(f'{client_addr} is coming')
            client_list.append(client_socket)  # 添加到client_list中
            epoll.register(client_socket.fileno(), select.EPOLLIN)  # 注册监控
        for client in client_list:
            if fd == client.fileno():
                # 读取client的数据，然后群发给其他人
                recv_data = client.recv(1024)
                if recv_data:
                    # 群发
                    for other in client_list:
                        if other is not client:
                            other.send(recv_data)
                else:
                    # 连接断开
                    print(f'{client_addr} left')
                    epoll.unregister(client.fileno())
                    client_list.remove(client)
                    client.close()

server_socket.close()
