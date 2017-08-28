#!/usr/bin/python
# -*- coding:utf -*-

#包含一系列函数，游戏的大部分工作由它们完成

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
     #响应按键
     if event.key==pygame.K_RIGHT:   #向左移动
          ship.moving_right=True
     elif event.key==pygame.K_LEFT:  #向右移动
          ship.moving_left=True
     elif event.key==pygame.K_SPACE:  #空格键发射子弹
          fire_bullet(ai_settings,screen,ship,bullets)
     elif event.key==pygame.K_q:      #按Q退出游戏
          sys.exit()

def check_keyup_events(event,ship):
     #响应松开
     if event.key==pygame.K_RIGHT:
          ship.moving_right=False
     elif event.key==pygame.K_LEFT:
          ship.moving_left=False
def check_events(ai_settings,screen,ship,bullets):
     #监视键盘和鼠标事件
     for event in pygame.event.get():
          if event.type==pygame.QUIT:
               sys.exit()          
          elif event.type==pygame.KEYDOWN:
               check_keydown_events(event,ai_settings,screen,ship,bullets)

          elif event.type==pygame.KEYUP:
               check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
     """更新屏幕上的图像，并切换到新屏幕"""

     #每次循环都重绘屏幕
     screen.fill(ai_settings.bg_color)
      #在飞船和外星人后面重绘所有子弹
     for bullet in bullets.sprites():
          bullet.draw_bullet()
     ship.blitme()
     #alien.blitme()
     aliens.draw(screen)
     #让最近绘制的屏幕可见
     pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
     """更新子弹的位置，并删除已消失的子弹"""
     bullets.update()

     for bullet in bullets.copy():
          if bullet.rect.bottom<=0:
                bullets.remove(bullet)
 #           print(len(bullets))

     check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
     #检查是否有子弹击中了外星人
     #如果击中，删除相应的子弹和外星人
     collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)

     if len(aliens)==0:
         #删除现有的子弹并新建一群外星人
         bullets.empty()
         create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
     if len(bullets)<ai_settings.bullets_allowed:
         new_bullet=Bullet(ai_settings,screen,ship)
         bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
     """计算每行可容纳多少个外星人"""
     available_space_x=ai_settings.screen_width-2*alien_width
     number_aliens_x=int(available_space_x/(2*alien_width))
     return number_aliens_x

def get_number_rows (ai_settings,ship_height,alien_height):
     """计算屏幕可容纳多少行外星人"""
     available_space_y=(ai_settings.screen_height -
                                 (3*alien_height)-ship_height)
     number_rows=int(available_space_y/(2*alien_height))
     return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
     """创建一个外星人并将其放在当前行"""
     alien=Alien(ai_settings,screen)
     alien_width=alien.rect.width
     alien.x=alien_width+2*alien_width*alien_number
     alien.rect.x=alien.x
     alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
     aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
     """创建外星人群"""
     #创建一个外星人，并计算一行可容纳多少外星人
     #外星人间距为外星人宽度
     alien=Alien(ai_settings,screen)
     #alien_width=alien.rect.width
     #available_space_x=ai_settings.screen_width-2*alien_width
     #number_aliens_x=int(available_space_x/(2*alien_width))
     number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
     number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
     #创建外星人群,嵌套循环
     for row_number in range(number_rows):     #从零数到要创建的外星人行数
          for alien_number in range(number_aliens_x):    #创建一行外星人
              """
              alien=Alien(ai_settings,screen)
              alien.x=alien_width+2*alien_width*alien_number
              alien.rect.x=alien.x
              alien.add(alien)
              """
              create_alien(ai_settings,screen,aliens,alien_number,
                     row_number)

def check_fleet_edges(ai_settings,aliens):
     """有外星人到达边缘时采取对应的措施"""
     for alien in aliens.sprites():
          if alien.check_edges():
              change_fleet_direction(ai_settings,aliens)
              break

def change_fleet_direction(ai_settings,aliens):
     """将整群外星人下移，并改变它们的方向"""
     for alien in aliens.sprites():
          alien.rect.y+=ai_settings.fleet_drop_speed
     ai_settings.fleet_direction *=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
     """响应被外星人撞到的飞船"""
     if stats.ships_left>0:
        #将余下的飞船数减1
        stats.ships_left-=1

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
     else:
        stats.game_active=False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
     """检查是否有外星人到达屏幕底部"""
     screen_rect=screen.get_rect()
     for alien in aliens.sprites():
          if alien.rect.bottom>=screen_rect.bottom:
              ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
              break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
     """检查是否有外星人位于屏幕边缘,更新外星人群中所有外星人的位置"""
     check_fleet_edges(ai_settings,aliens)
     aliens.update()

     if pygame.sprite.spritecollideany(ship,aliens):  #检查编组是否有成员与精灵发生碰撞
         #print("Ship hit!!!")
         ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

     check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

