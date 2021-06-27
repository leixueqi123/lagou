#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
执行文件run.py
'''

from hero_factory import HeroFactory
if __name__=="__main__":
    #构造heroFactory
    heroFactory=HeroFactory()
    #构造timo
    timo = heroFactory.creat_hero("Timo",1000,210)
    #构造jinx
    jinx = heroFactory.creat_hero("Jinx",1100,190)
    #调用fight
    timo.fight(jinx.hero_hp,jinx.hero_power,jinx.hero_name)

    #构造timo
    timo = heroFactory.creat_hero("Timo", 1300, 210)
    #构造jinx
    jinx = heroFactory.creat_hero("Jinx", 1100, 190)
    #调用fight
    timo.fight(jinx.hero_hp, jinx.hero_power, jinx.hero_name)





