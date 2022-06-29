# 作者: Michael(phb)
# 2022年06月16日21时01分51秒
from socket import *

from socket import *


def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))
    client_socket.connect((server_ip, server_port))
    file_name = input("请输入要下载的文件名：")
    client_socket.send(file_name.encode("utf-8"))
    recv_data = client_socket.recv(1024)
    if recv_data:
        with open("[接收]" + file_name, 'wb') as f:
            f.write(recv_data)
    client_socket.close()


if __name__ == '__main__':
    main()
