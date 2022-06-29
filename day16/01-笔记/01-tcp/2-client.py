# 作者: Michael(phb)
# 2022年06月16日20时40分01秒
from socket import *

client = socket(AF_INET, SOCK_STREAM)
dest_addr = ('192.168.35.1', 2000)
client.connect(dest_addr)
client.send('hello'.encode('utf8'))
data = client.recv(1024)
print(data.decode('utf8'))
client.close()
