# -*- coding:utf-8 -*-
import allure
from appium.webdriver.common.mobileby import MobileBy
from ..page.base import BasePage

class EditContactPage(BasePage):

    @allure.step("edit_contact")
    def edit_contact(self,name,phonenum,address):
        self.send_keys(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']",name)

        self.send_keys(MobileBy.XPATH,"//*[@text='手机号']",phonenum)


        self.click(MobileBy.XPATH,"//*[@text='地址']")
        self.send_keys(MobileBy.XPATH,"//*[@text='请输入公司地址，例如“腾讯大厦”']",address)
        self.click(MobileBy.XPATH, "//*[@text='确定']")

        self.click(MobileBy.XPATH, "//*[@text='保存']")
        from ..page.add_contact_page import AddContactPage
        return AddContactPage(self.driver)
