# 打开,默认以文本方式打开
file = open('Readme', encoding='utf8')
# 读取
txt = file.read()
print(txt)

print('-'*50)

txt = file.read()  # 读到文件尾，再读什么读不到
print(txt)
# 关闭
file.close()
