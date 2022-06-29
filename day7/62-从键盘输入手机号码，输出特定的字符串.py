# 从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串
phone_num = input('请输入手机号：').split()
print('Mobile: ' + ' '.join(phone_num))
