# -*- coding:utf-8 -*-
import allure
from .edit_contact_page import EditContactPage
from appium.webdriver.common.mobileby import MobileBy
from ..page.base import BasePage



class AddContactPage(BasePage):
    @allure.step("click_add_contact_menual")
    def click_add_contact_menual(self):
        self.click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return EditContactPage(self.driver)

    @allure.step("is_in_add_contact_menual")
    def is_in_add_contact_menual(self):
        if  self.find(MobileBy.XPATH, "//*[@text='手动输入添加']"):
            return  True
        else:
            return  False

    @allure.step("get_result")
    def get_result(self):
         result = self.get_toast_text()
         return result
