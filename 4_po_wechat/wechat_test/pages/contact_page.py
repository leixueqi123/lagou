# -*- coding:utf-8 -*-
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from .base_page import SeleniumDriver
from .add_members_page import AddMemberPage


'''
"通讯录"界面
'''


class ContactObject(object):
    '''
    通讯录界面，页面元素的定义 抽象到此类中
    '''
    add_member = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    member_list = (By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')


class ContactPage(SeleniumDriver):
    '''
    继承 base_page.SeleniumDriver
    通讯录界面，页面元素的操作方法 抽象到此类中
    '''
    @allure.step('点击"添加成员"')
    def goto_add_menber(self):
        '''
        点击"添加成员"
        :return:
        '''
        #等待元素可被点击
        WebDriverWait(self.driver,5,0.5).until(expected_conditions.element_to_be_clickable(ContactObject.add_member))
        self.driver.find_element(*ContactObject.add_member).click()
        #PO:方法返回到其他PageObjects
        return AddMemberPage(self.driver)

    @allure.step('点击"获取成员列表"')
    def get_list(self):
        '''
        获取成员列表
        :return:
        '''
        name_list=[]
        eles=self.driver.find_elements_by_css_selector(ContactObject.member_list[1])
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list

    @allure.step('判断"是否进入通讯录界面"')
    def is_in_contact_page(self):
        if  WebDriverWait(self.driver, 5, 0.5).until(
                expected_conditions.visibility_of_element_located(ContactObject.add_member)):
            return True
        else:
            return False