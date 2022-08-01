# 作者: Michael(phb)
# 2022年06月17日22时59分51秒
import struct

a = '我很帅你很牛'.encode('utf8')
print(len(a))

print('-'*50)

len_bytes = struct.pack('I', len(a))
print(len_bytes)
print('length:', len(len_bytes))

print('-'*50)

b = struct.unpack('I', len_bytes)
print(b[0])
print(type(b[0]))

print('-'*50)

# 网络中传输时，标准是要求都是大端
temp_big_bytes = struct.pack(">I", len(a))
print('length:', len(temp_big_bytes))
print(temp_big_bytes)
