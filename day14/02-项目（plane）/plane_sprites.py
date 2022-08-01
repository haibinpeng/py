# 作者: Michael(phb)
# 2022年06月14日21时37分18秒
import random
import pygame

# 屏幕大小的常量对象
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 15
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹的事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        """
        :param image_name: image 精灵图像，使用image_name加载
        :param speed: speed 精灵移动速度，默认为1
        """
        # 调用父类的初始化方法
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self, *args):
        """重写update"""
        # 默认在垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        image_name = './images/background.png'
        super().__init__(image_name)
        # 判断是否交替图片，如果是，将图片设置到屏幕顶部
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1. 调用父类的方法实现
        super().update()
        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类方法，创建敌机精灵，并且指定敌机的图像
        super().__init__("./images/enemy1.png")
        # 设置敌机的随机初始速度 1-3
        self.speed = random.randint(1, 3)
        # 设置敌机的随机初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，让敌机在垂直方向运动
        super().update()
        # 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print('敌机挂了 %s' % self.rect)


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类方法，创建英雄精灵，并且指定英雄的图像和初始速度
        super().__init__('./images/me1.png', 0)
        # 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 飞机水平移动
        self.rect.x += self.speed
        # 判断屏幕边界
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 一次创建3颗子弹
        for i in (1, 2, 3):
            # 创建子弹精灵
            bullet = Bullet()
            # 摄制精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        super().update()
        # 判断是否超出屏幕，如果是，从精灵组删除
        if self.rect.bottom < 0:
            self.kill()
