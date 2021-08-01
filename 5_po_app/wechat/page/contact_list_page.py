# -*- coding:utf-8 -*-
import  allure
import random
from .add_contact_page import AddContactPage
from appium.webdriver.common.mobileby import MobileBy
from ..page.base import BasePage



class ContactlistPage(BasePage):

    @allure.step("goto_add_contact")
    def goto_add_contact(self):
        self.swipe_find('添加成员')
        self.click(MobileBy.XPATH,"//*[@text='添加成员']")
        return AddContactPage(self.driver)



    @allure.step("delete_contact")
    def delete_contact(self):
        elements=self.find_elements(MobileBy.ID,"com.tencent.wework:id/h14")[1:]
        delete_ele = random.choice(elements)
        delete_ele.click()
        if self.find(MobileBy.ID,'com.tencent.wework:id/guk'):
            #联系人详情页，存在...操作删除成员
            self.click(MobileBy.ID,'com.tencent.wework:id/guk')
            self.click(MobileBy.ID,'com.tencent.wework:id/azd')

            self.swipe_find('删除成员')

            self.click(MobileBy.XPATH, "//*[@text='删除成员']")
            self.click(MobileBy.XPATH, "//*[@text='确定']")
            return True
        else:
            #联系人详情页，不存在...，账户本身
            print("没有可删除的成员")









