#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
     """一个对飞船发射的子弹进行管理的类"""
     def __init__(self,ai_settings,screen,ship):
           #在飞船所处的位置创建一个子弹对象
           super(Bullet,self).__init__()
           self.screen=screen
           #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
           self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                ai_settings.bullet_height)  #从空白开始创建一个矩形
           self.rect.centerx=ship.rect.centerx  #将子弹的centerx设置为飞船的rect.centerx
           self.rect.top=ship.rect.top #将子弹的top设置为飞船的rect.top,让子弹看起来像是从飞船中射出的
           #存储用小数表示的子弹位置
           self.y=float(self.rect.y)

           self.color=ai_settings.bullet_color     #子弹颜色
           self.speed_factor=ai_settings.bullet_speed_factor    #子弹速度

     def update(self):
           """向上移动子弹"""
           #更新表示子弹位置的小数值
           self.y-=self.speed_factor
           #更新表示子弹的rect的位置
           self.rect.y=self.y

     def draw_bullet(self):
           """在屏幕上绘制子弹"""
           pygame.draw.rect(self.screen,self.color,self.rect)
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,):
             super().__init__()
             self.screen=screen

             self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
             	          ai_settings.bullet_height)
             self.rect.centerx=ship.rect.centerx
             self.rect.top=ship.rect.top

             self.y=float(self.rect.y)

             self.color=ai_settings.bullet_color
             self.speed_factor=ai_settings.bullet_speed_factor

        def update(self):
             self.y -= self.speed_factor
             self.rect.y=self.y

        def draw_bullet(self):
             pygame.draw.rect(self.screen,self.color,self.rect)