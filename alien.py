import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """标识单个飞机的类"""
    def __init__(self, ai_settings, screen):
        """初始化飞机并设置起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞机图像，并设置其 rect 属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #每个飞机最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储飞机的准确位置
        self.x = float(self.rect.x)
    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        """如果飞机位于屏幕边缘，就返回 True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """向左向右移动飞机"""
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x


