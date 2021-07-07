# -*- coding:utf-8 -*-
import yaml
from selenium import webdriver

'''
基类，供其他页面page类调用

主要实现：
1、构造webdriver，cookie自动登录企业微信
'''

class SeleniumDriver(object):
    __timeout=5

    def __init__(self,base_driver=None):
        if base_driver is None:
            '''
            首次启动没有webdriver时，构造webdriver
            '''
            #方式一 复用浏览器
            # # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            # opt = webdriver.ChromeOptions()
            # opt.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=opt)
            # cookies = self.driver.get_cookies()
            # print(cookies)
            # self.driver.implicitly_wait(10)
            #方式二 cookie登录
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            import os
            file = os.path.join(os.getcwd(),'pages','data.yaml')
            print (file)
            with open(file, encoding="UTF-8") as f:
                cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        else:
            #其他类继承后SeleniumDriver，不重复构造webdriver
            self.driver = base_driver
