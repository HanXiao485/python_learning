import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game) -> None:
        """初始化飞船，设置初始位置"""
        self.screen = ai_game.screen                    #将屏幕赋给ship的一个属性？？？
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()    #获取屏幕的矩形信息 .get_rect()

        self.image = pygame.image.load('images/ship.bmp')    #加载图像
        self.rect = self.image.get_rect()                    #获取图像的矩形信息

        self.rect.midbottom = self.screen_rect.midbottom     #将飞船放置在屏幕中间？？？

        self.x = float(self.rect.x)                          #采用浮点数形式储存飞船位置

        self.moving_right = False                            #设置右移标志
        self.moving_left = False                             #设置左移标志

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x                                 #根据self.x更新rect.x对象
        

    def bltime(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)