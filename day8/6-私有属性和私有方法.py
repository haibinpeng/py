# class Women:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18  # 私有属性
#
#     def secret(self):
#         print(f'我的年龄是{self.__age}')
#
#
# xiaomei = Women('小美')
# xiaomei.secret()
# print(__age)  # 私有属性，直接访问会报错

class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性

    def __secret(self):  # 私有方法
        print(f'我的年龄是{self.__age}')

    def boy_friend(self):
        self.__secret()


xiaomei = Women('小美')
xiaomei.boy_friend()

# print(xiaomei._Women__age)  # 强行访问
