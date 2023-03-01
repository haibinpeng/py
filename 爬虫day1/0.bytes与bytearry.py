# 作者: Michael(phb)
# 2023年02月28日22时21分56秒

print(type('xbb'))  # str
print(type(b'xbb'))  # bytes

print('*'*50)

str1 = '人生苦短，我用python'
print(type(str1))  # str
b = str1.encode()
print(type(b))  # bytes
print(b)
print(b.decode())
# print(b[:6])
# b[:6] = bytes('生命'.encode())
print(type(b.decode()))  # str

print('*'*50)

# bytearray是可变的
str2 = '人生苦短，我用python'
print(str2.encode())
b1 = bytearray(str2.encode())
print(b1)
print(type(b1))  # bytearray
print(b1.decode())
print(b1[:6])
b1[:6] = bytearray('生命'.encode())
print(b1.decode())
