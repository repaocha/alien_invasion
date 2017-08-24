#!/usr/bin/python
# -*- coding:utf-8 -*-

#import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
     pygame.init()      #初始化背景设置
     ai_settings=Settings()
     screen=pygame.display.set_mode(
          (ai_settings.screen_width,ai_settings.screen_height))  #创建一个宽1200像素高800像素的游戏窗口
     pygame.display.set_caption("Alien Invasion")
     #设置背景色
     bg_color=(230,230,230)
     
     ship=Ship(ai_settings,screen)

     #开始游戏主循环
     while True:
     	       gf.check_events(ship)
     	       ship.update()
     	       gf.update_screen(ai_settings,screen,ship)

run_game()