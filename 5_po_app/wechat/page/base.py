# -*- coding:utf-8 -*-
import allure
import time
import os

from ..conftest import logging
logger = logging.getLogger()
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy



'''
base_page.py 定义driver
包括 ：初始化driver find, click, swipe_find ,send_keys等
'''
class BasePage:

    def __init__(self, driver = None):
        self.driver = driver

    @allure.step("find")
    def find(self,by,value):
        logger.info(f"查找元素{by}{value}")
        try:
            #return 供其他方法调用
            return self.driver.find_element(by, value)
        except:
            path=os.path.join(os.getcwd(),'report')
            timestamp = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
            file_path=os.path.join(path,f"{timestamp}.png")
            with allure.step("保存图片"):
                self.driver.get_screenshot_as_file(file_path)
                time.sleep(2)
                allure.attach.file(file_path,attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"没有找到元素{by}{value}")

    @allure.step("find_elements")
    def find_elements(self,by,value):
        logger.info(f"查找元素{by}{value}")
        try:
            #return 供其他方法调用
            return self.driver.find_elements(by, value)
        except:
            path=os.path.join(os.getcwd(),'report')
            timestamp = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
            file_path=os.path.join(path,f"{timestamp}.png")
            with allure.step("保存图片"):
                self.driver.get_screenshot_as_file(file_path)
                time.sleep(2)
                allure.attach.file(file_path,attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"没有找到元素{by}{value}")



    @allure.step("click")
    def click(self,by,value):
        logger.info("点击元素")
        #self.driver.find_element(by,value).click()
        self.find(by,value).click()

    @allure.step("send_keys")
    def send_keys(self,by,value,text):
        logger.info("输入")
        #self.driver.find_element(by,value).set_text(text)
        self.find(by,value).send_keys(text)

    @allure.step("get_toast_text")
    def get_toast_text(self):
        # 获取 toast 文本
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

    @allure.step("back")
    def back(self, num=5):
        for i in range(num):
            self.driver.back()

    @allure.step("swipe_find")
    def swipe_find(self, text, num=5):
        # 设置一个最大的查找次数
        for i in range(num):
            if i == num - 1:
                raise NoSuchElementException(f"找了{num - 1} 次，未找到")
            # 方法一，不要让find_element 抛异常，在except中捕获异常，实现滑动操作
            try:
                #element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                element = self.find(MobileBy.XPATH, f"//*[@text='{text}']")
                return element
            except:
                print("未找到")
                # 如果未找到这个元素，捕获这个异常，并且 滑动 一屏
                # 滑动
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get('width')
                height = size.get('height')

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.2

                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
