# -*- coding:utf-8 -*-
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .base_page import SeleniumDriver

'''
添加成员界面
'''


class AddMemberObject(object):
    '''
    "添加成员"界面，页面元素的定义 抽象到此类中
    '''
    username = (By.ID,"username")
    memberAdd_english_name = (By.ID,"memberAdd_english_name")
    memberAdd_acctid = (By.ID,"memberAdd_acctid")
    memberAdd_phone = (By.ID,"memberAdd_phone")
    username = (By.ID,"username")
    save_button = (By.CSS_SELECTOR,".js_btn_save")


class AddMemberPage(SeleniumDriver):
    '''
    继承 base_page.SeleniumDriver
    "添加成员"界面，页面元素的操作方法， 抽象到此类中
    '''

    @allure.step('输入：用户名，用户ID，手机号，点击"保存"')
    def add_member(self,username,memberAdd_acctid,memberAdd_phone):
        '''
        输入：用户名，用户ID，手机号，点击"保存"
        :param username:
        :param memberAdd_acctid:
        :param memberAdd_phone:
        :return:
        '''
        #输入用户名
        WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located(AddMemberObject.username)).send_keys(username)
        #输入用户ID
        WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located(AddMemberObject.memberAdd_acctid)).send_keys(memberAdd_acctid)
        #输入手机号
        WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located(AddMemberObject.memberAdd_phone)).send_keys(memberAdd_phone)
        #点击"保存"
        WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located(AddMemberObject.save_button)).click()

    def add_member_fail(self):
        pass

    @allure.step('判断"是否进入添加成员界面"')
    def is_in_add_member_page(self):
        if not WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.visibility_of_element_located(AddMemberObject.memberAdd_acctid)):
            raise AssertionError('点击"添加成员"，进入"添加成员页面"失败！')

