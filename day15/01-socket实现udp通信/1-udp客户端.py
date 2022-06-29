# 作者: Michael(phb)
# 2022年06月15日16时19分52秒
import socket

# socket.AF_INET代表ipv4, socket.SOCK_DGRAM代表udp
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ('192.168.221.1', 2000)
client.sendto('hello'.encode('utf8'), dest_addr)
recv_data = client.recvfrom(1024)
print(recv_data[0].decode('utf8'))
client.close()
