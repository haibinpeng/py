# 作者: Michael(phb)
# 2022年06月14日21时18分15秒
from plane_sprites import *
import time


class PlaneGame:
    """飞机大战主游戏"""

    def __init__(self):
        print('游戏初始化')
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时针
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 设置定时器事件 - 每秒创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 1000毫秒
        # 设置定时器事件 - 每隔0.5秒发射一次子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        """创建精灵、精灵组"""
        # # 背景精灵
        # 根据面向对象设计原则，应该将对象的职责，封装到类的代码内部，所以不按下面这么写
        # bg1 = Background('./images/background.png')
        # bg2 = Background('./images/background.png')
        # # 第二张背景图置于屏幕的正上方
        # bg2.rect.y = -bg2.rect.height
        # 修改后
        bg1 = Background()
        bg2 = Background(True)
        # 背景组
        self.back_group = pygame.sprite.Group(bg1, bg2)  # 初始化组对象
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('开始游戏')
        while True:
            # 1. 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新精灵组
            self.__update_sprites()
            # 5. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        event_list = pygame.event.get()
        for event in event_list:
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 监听定时器事件，定时出现敌机
            elif event.type == CREATE_ENEMY_EVENT:
                # 向敌机精灵组中添加精灵
                self.enemy_group.add(Enemy())
            # 监听定时器事件，定时发射子弹
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 获取用户按键，得到的是一个按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            m = "./sound/use_bomb.wav"
            pygame.mixer.music.load(m)
            pygame.mixer.music.play()
            time.sleep(2)
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        for group in [self.back_group, self.enemy_group, self.hero_group, self.hero.bullets]:
            group.update()
            # 将精灵的image绘制在rect位置
            group.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束"""
        print('游戏结束')
        pygame.quit()
        # 结束进程
        exit()


if __name__ == '__main__':
    pygame.init()
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
