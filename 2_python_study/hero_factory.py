#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hero import Timo,Jinx

'''
#英雄工厂模式
'''

class HeroFactory:
    def creat_hero(self,hero_name,hero_hp,hero_power):
        if hero_name=='Timo':
            return Timo(hero_hp,hero_power)
        elif hero_name=='Jinx':
            return Jinx(hero_hp,hero_power)
        else:
            raise Exception("此英雄不在英雄工厂中。")



