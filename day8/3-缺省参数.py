# 缺省参数
def print_info(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s是%s" % (name, gender_text))


print_info('yf')
print_info('lily', False)

print('-' * 50)


def print_info1(name, title="", gender=True):  # 缺省的title默认为没有职位，gender为男性
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s是%s" % (title, name, gender_text))


print_info1("yf")
print_info1("bob", title="班长")
print_info1("lily", gender=False)