# 作者: Michael(phb)
# 2022年06月17日22时06分18秒
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

# 设置端口重用
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

address = ('192.168.35.1', 2000)

server_socket.bind(address)
server_socket.listen(10)
# 设置server_socket为非阻塞
server_socket.setblocking(False)

client_socket = None
while True:
    try:
        client_socket, client_addr = server_socket.accept()
    except Exception as e:
        pass
    if client_socket:
        # 设置client_socket为非阻塞
        client_socket.setblocking(False)
        try:
            text = client_socket.recv(1024)
            if not text:
                print('bye')
                exit(0)
            print(text.decode('utf8'))
        except Exception as e:
            pass
