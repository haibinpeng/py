# 作者: Michael(phb)
# 2022年06月24日14时05分28秒
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ('', 2000)
server_socket.bind(server_addr)
server_socket.listen(10)
client_socket, client_addr = server_socket.accept()
recv_data = client_socket.recv(1024)
print(recv_data.decode('utf8'))

http_header = 'HTTP/1.1 200 ok\r\n'
response = http_header + '\r\n'
response += 'hello world'
client_socket.send(response.encode('utf8'))
client_socket.close()
server_socket.close()
