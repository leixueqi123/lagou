#!/usr/bin/env python
# -*- coding: utf-8 -*-


#定义父类，Hero
class Hero:
    #类变量，hero_name
    hero_name=''
    def __init__(self,hero_hp,hero_power):
        self.hero_hp = hero_hp
        self.hero_power = hero_power

    #实类方法，方法是实类对象中的函数
    def fight(self,enemy_hp,enemy_power,enemy_name):
        '''
        :param enemy_hy:敌人的血量
        :param enemy_power:敌人的攻击力
        :return:
        '''
        hero_final_hp=self.hero_hp -enemy_power
        enemy_final_hp=enemy_hp - self.hero_power
        if hero_final_hp>enemy_final_hp:
            #通过self.类变量去调用 类中的类变量 self.hero_name
            print (f"英雄{self.hero_name}获胜")
        elif hero_final_hp<enemy_final_hp:
            print (f"敌人{enemy_name}获胜")
        else:
            print ("平局")

#定义子类，Timo，继承Hero
class Timo(Hero):
    #子类 重新赋予 父类的属性hero_name
    hero_name = 'Timo'

#定义子类，Jinx，继承Hero
class Jinx(Hero):
    #子类 重新赋予 父类的属性hero_name
    hero_name = 'Jinx'






