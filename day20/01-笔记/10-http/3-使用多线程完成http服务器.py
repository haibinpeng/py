# 作者: Michael(phb)
# 2022年06月26日15时16分42秒
import socket
import re
import threading


def server_client(client_socket):
    request = client_socket.recv(1024).decode('utf8')
    request_lines = request.splitlines()
    print('')
    print('>' * 20)
    print(request_lines)
    if request_lines:
        url = ''
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            url = ret.group(1)
            if url == '/':
                url = '/index.html'
        try:
            f = open('./html' + url, 'rb')
        except:
            response = 'HTTP/1.1 404 NOT FOUND\r\n'
            response += '\r\n'
            response += 'not found'
            client_socket.send(response.encode('utf8'))
        else:
            html_content = f.read()
            f.close()
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            client_socket.send(response.encode('utf8'))
            client_socket.send(html_content)
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 7890))
    server_socket.listen(100)
    while True:
        client_socket, client_addr = server_socket.accept()
        p = threading.Thread(target=server_client, args=(client_socket,))
        p.start()
        # 多线程时，client_socket传递给子线程以后，主线程不能关闭
        # client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
