f_read = open('Readme', encoding='utf8')
f_write = open('Readme1', 'w', encoding='utf8')
# 读取并写入文件
txt = f_read.read()
f_write.write(txt)
f_read.close()
f_write.close()
