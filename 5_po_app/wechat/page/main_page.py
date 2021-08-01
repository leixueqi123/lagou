# -*- coding:utf-8 -*-
import allure
from .contact_list_page import ContactlistPage
from appium.webdriver.common.mobileby import MobileBy
from ..page.base import BasePage

class MainPage(BasePage):

    @allure.step("goto_contactlist")
    def goto_contactlist(self):
        self.click(MobileBy.XPATH, "//*[@text='通讯录']")
        return ContactlistPage(self.driver)



