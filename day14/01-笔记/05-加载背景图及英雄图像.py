# 作者: Michael(phb)
# 2022年06月14日20时39分55秒
import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load('./images/background.png')
# 2> blit 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄图像
# 1> 加载图像
hero = pygame.image.load('./images/me1.png')
# 2> 绘制在屏幕
screen.blit(hero, (200, 500))

# update 更新屏幕显示
pygame.display.update()

while True:
    pass

pygame.quit()
