#!/usr/bin/python
# -*- coding:utf-8 -*-

#创建一系列整个游戏都要用到的对象

#import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
     pygame.init()      #初始化背景设置
     ai_settings=Settings()
     screen=pygame.display.set_mode(
          (ai_settings.screen_width,ai_settings.screen_height))  #创建一个宽1200像素高800像素的游戏窗口
     pygame.display.set_caption("Alien Invasion")
     #设置背景色
     bg_color=(230,230,230)
     #创建一个用于存储游戏统计信息的实例
     stats=GameStats(ai_settings)
     #创建记分牌
     sb=Scoreboard(ai_settings,screen,stats)
     #创建play按钮
     play_button=Button(ai_settings,screen,"Play")
     #创建一艘飞船
     ship=Ship(ai_settings,screen)
     #创建一个外星人
     #alien=Alien(ai_settings,screen)
     #创建一个用于存子弹的编组
     bullets=Group()
     #创建一个外星人编组
     aliens=Group()
     #创建外星人群
     gf.create_fleet(ai_settings,screen,ship,aliens)
     #开始游戏主循环
     while True:
            gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
            if stats.game_active:
                ship.update()  #调用更新飞船的方法
                gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)  #调用更新子弹的方法
                gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)     #调用更新外星人的方法

            gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) #参数顺序要一一对应

run_game()   