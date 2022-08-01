# 作者: Michael(phb)
# 2022年06月24日15时53分03秒
from socket import *
import re


def serve_client(client_socket):
    """接收浏览器的请求，并给予响应"""
    # 1.接收浏览器发过来的请求，即http请求
    # GET / HTTP/1.1
    # .....
    request = client_socket.recv(1024).decode('utf8')
    # 将头部进行剥离，得到头部的每一行
    request_line = request.splitlines()
    print('')
    print('>' * 20)
    print(request_line)
    if request_line:
        url = ''
        # 使用正则表达式去处理第一行，为了得到请求的url
        # [^/]+ 不是斜杠一直吃，[^ ]*不是空格一直吃，(/[^ ]*)拿到的就是url
        ret = re.match(r'[^/]+(/[^ ]*)', request_line[0])
        if ret:
            url = ret.group(1)
            print('*' * 50, url)
            if url == '/':
                url = '/index.html'
        # 2.返回http格式的数据给浏览器
        try:
            # 打开请求的资源
            f = open('./html' + url, 'rb')
        except:
            # 如果没有就返回404
            response = 'HTTP/1.1 404 NOT FOUND\r\n'
            response += '\r\n'
            response += 'not find'
            client_socket.send(response.encode('utf8'))
        else:
            html_content = f.read()
            f.close()
            # 准备发送给浏览器的数据---header
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            # 将response header发送给浏览器
            client_socket.send(response.encode("utf-8"))
            # 将response body发送给浏览器
            client_socket.send(html_content)
    client_socket.close()


def main():
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 设置端口重用
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定
    server_socket.bind(('', 7890))
    # 监听
    server_socket.listen(100)
    while True:
        # 等待客户端（浏览器）连接
        client_socket, client_addr = server_socket.accept()
        # 为这个客户服务
        serve_client(client_socket)
    server_socket.close()


if __name__ == '__main__':
    main()
