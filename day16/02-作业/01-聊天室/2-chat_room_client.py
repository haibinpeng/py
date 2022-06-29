# 作者: Michael(phb)
# 2022年06月16日21时45分28秒
from socket import *
import select
import sys

client_socket = socket(AF_INET, SOCK_STREAM)
address = ('192.168.221.128', 2000)
client_socket.connect(address)

epoll = select.epoll()

epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(client_socket.fileno(), select.EPOLLIN)

while True:
    events = epoll.poll(-1, 2)
    for fd, _ in events:
        if fd == sys.stdin.fileno():
            data = sys.stdin.readline().rstrip('\n')
            if data:
                client_socket.send(data.encode('utf8'))
        if fd == client_socket.fileno():
            recv_data = client_socket.recv(1024)
            if not recv_data:
                # 对端断开
                print('聊天室已关闭')
                client_socket.close()
                exit()
            print(recv_data.decode('utf8'))

client_socket.close()
