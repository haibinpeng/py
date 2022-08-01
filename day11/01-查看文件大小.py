# 作者: Michael(phb)
# 2022年06月10日20时35分59秒
import os
import time

file_info = os.stat('file')
print(
    'size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid, file_info.st_mode, file_info.st_mtime))
# 把秒数转为字符串时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(file_info.st_mtime)))
