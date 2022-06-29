# 作者: Michael(phb)
# 2022年06月16日20时50分22秒
from socket import *
import sys


def get_file(file_name):
    """获取文件的内容"""
    try:
        with open(file_name, 'rb') as f:
            data = f.read()
        return data
    except:
        print(f'没有文件{file_name}')


def main():
    if len(sys.argv) != 2:
        print("请按照如下方式运行：python3 xxx.py 7890")
        return
    else:
        # 运行方式为python3 xxx.py 7890
        port = int(sys.argv[1])
    server_socket = socket(AF_INET, SOCK_STREAM)
    address = ('', port)
    server_socket.bind(address)
    server_socket.listen(10)
    while True:
        client_socket, _ = server_socket.accept()
        recv_data = client_socket.recv(1024)
        file_name = recv_data.decode('utf8')
        print(f'要下载的文件是{file_name}')
        file_content = get_file(file_name)
        # 因为获取打开文件时是以rb方式打开，所以file_content中的数据已经是二进制的格式，因此不需要encode编码
        if file_content:
            client_socket.send(file_content)
        client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
