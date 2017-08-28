#!/usr/bin/python
# -*- coding:utf-8 -*-

#初始化控制游戏外观和飞船速度的属性

class Settings():
      """存储外星人入侵的所有设置的类"""

      def __init__(self):
           """初始化游戏设置"""
           #屏幕设置
           self.screen_width=1000
           self.screen_height=600
           self.bg_color=(230,230,230)
           #飞船设置
           self.ship_speed_factor=1.5
           self.ship_limit=3
           #子弹设置
           self.bullet_speed_factor=3
           self.bullet_width=3
           self.bullet_height=15
           self.bullet_color=60,60,60
           self.bullets_allowed=10
           #外星人设置
           self.alien_speed_factor=1
           self.fleet_drop_speed=10
           #为1表示向右移，为-1表示向左移
           self.fleet_direction=1
