#!/usr/bin/python
# -*- coding:utf-8 -*-

#创建一系列整个游戏都要用到的对象

#import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
     pygame.init()      #初始化背景设置
     ai_settings=Settings()
     screen=pygame.display.set_mode(
          (ai_settings.screen_width,ai_settings.screen_height))  #创建一个宽1200像素高800像素的游戏窗口
     pygame.display.set_caption("Alien Invasion")
     #设置背景色
     bg_color=(230,230,230)
     #创建一艘飞船
     ship=Ship(ai_settings,screen)
     #创建一个用于存子弹的编组
     bullets=Group()
     #开始游戏主循环
     while True:
            gf.check_events(ai_settings,screen,ship,bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings,screen,ship,bullets)

run_game()