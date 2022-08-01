class Game:
    top_score = 0  # 类属性，历史最高分

    def __init__(self, name):
        self.name = name

    @staticmethod  # 静态方法
    def show_help():
        print('帮助信息')

    def start_game(self):
        print(f'{self.name}开始游戏')


Game.show_help()  # 查看帮助

game = Game('小明')  # 创建游戏对象
game.start_game()
