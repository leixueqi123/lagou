# -*- coding:utf-8 -*-
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


from .base_page import SeleniumDriver
from .contact_page import ContactPage


'''
PO模式实现思路如下：
编码第一步：构造PO
构造页面相关的类和方法
时序图里 黄色代表每个模块
每条线代表页面实现的操作
箭头的始端代表开始页面
箭头的终端代表结束页面
实现暂时实际唯恐
'''


'''
企业微信首页
'''

class MainObject(object):
    '''
    企业微信首页，页面元素的定义 抽象到此类中
    '''
    menu_index = (By.ID,"menu_index")
    menu_contacts = (By.ID, "menu_contacts")


class MainPage(SeleniumDriver):
    '''
    继承 base_page.SeleniumDriver
    企业微信首页，页面元素的操作方法 抽象到此类中
    '''

    @allure.step("点击'通讯录'")
    def goto_contact(self):
        '''
        点击"通讯录"
        :return:
        '''
        WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located(MainObject.menu_contacts)).click()
        return ContactPage(self.driver)


