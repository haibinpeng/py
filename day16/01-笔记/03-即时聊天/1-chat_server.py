# 作者: Michael(phb)
# 2022年06月16日21时16分57秒
from socket import *
import sys
import select

server_socket = socket(AF_INET, SOCK_STREAM)
address = ('192.168.221.128', 2000)
server_socket.bind(address)
server_socket.listen(10)

epoll = select.epoll()
# 注册要监控的描述符
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(server_socket.fileno(), select.EPOLLIN)

client_socket = None

while True:
    events = epoll.poll(-1, 3)
    for fd, event in events:
        if fd == server_socket.fileno():
            # 有连接请求
            client_socket, _ = server_socket.accept()
            epoll.register(client_socket.fileno(), select.EPOLLIN)
        if fd == sys.stdin.fileno():
            if not client_socket:  # 客户端还没连接
                print('暂无客户端连接')
                continue
            data = sys.stdin.readline().rstrip('\n')
            if data:
                client_socket.send(data.encode('utf8'))
        if fd == client_socket.fileno():
            recv_data = client_socket.recv(1024)
            if not recv_data:
                # 对端断开
                print('对方已断开')
                epoll.unregister(client_socket.fileno())
                client_socket.close()
                continue
            print(recv_data.decode('utf8'))

server_socket.close()
