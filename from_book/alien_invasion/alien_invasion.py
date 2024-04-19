import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self) -> None:
        """初始化游戏，创建游戏资源"""
        pygame.init()    #初始化pygame
        self.clock = pygame.time.Clock()                     #创建time模块中Clock类的一个实例
        self.settings = Settings()
        self.bg_color = (230,230,230)                        #设置游戏背景颜色，将颜色赋给bg_color
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))    #创建显示窗口
        pygame.display.set_caption('Alien Invasion')         #
        self.ship = Ship(self)                               #self指向当前AlienInvasion实例，让Ship能够访问游戏资源？？？？？
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()                         #接受屏幕响应
            self.ship.update()                           #更新飞船位置
            self.bullets.update()                        #更新子弹
            self._updat_screen()                         #更新屏幕
            self.clock.tick(60)                          #接受一个参数：游戏帧率=60

    def _check_events(self):
        """按键、鼠标响应"""
        for event in pygame.event.get():        #对于每一次事件
            if event.type ==pygame.QUIT:        #如果事件类别为退出游戏
                sys.exit()                      #退出
            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)      
            
    def _check_keydown_events(self,event):
        """检测按键按下事件"""
        if event.key == pygame.K_RIGHT:           #event.key？？？？？
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self,event):
        """检测按键抬起事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    
    def _updat_screen(self):
         """更新屏幕上的图像，切换新屏幕"""
         self.screen.fill(self.settings.bg_color)     #每次循环重绘屏幕
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.ship.bltime()                           #将飞船绘制到屏幕           
         pygame.display.flip()                        #让最近的绘制屏幕可见
         



if __name__ == '__main__':
    #创建游戏实例，运行游戏
    ai = AlienInvasion()
    ai.run_game()
