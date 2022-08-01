class Game:
    top_score = 0  # 类属性，历史最高分

    def __init__(self, name):
        self.name = name

    @classmethod  # 定义类方法
    def show_top_score(cls):
        print(f'历史最高分为{cls.top_score}')

    def start_game(self):
        print(f'{self.name}开始游戏')


Game.show_top_score()  # 查看历史最高分

game = Game('小明')  # 创建游戏对象
game.start_game()
