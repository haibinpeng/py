# 作者: Michael(phb)
# 2022年06月14日20时44分07秒
import pygame

clock = pygame.time.Clock()
i = 0

while True:
    # 设置屏幕刷新帧率
    clock.tick(60)  # 每秒60次
    print(i)
    i += 1
