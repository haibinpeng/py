class MusicPlayer:
    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        #  返回类属性的单例引用
        return cls.instance

    def __init__(self, music_name):
        print('初始化:'+music_name)


player1 = MusicPlayer('青花瓷')
player2 = MusicPlayer('夜曲')
print(player1)
print(player2)
print(player1 is player2)
