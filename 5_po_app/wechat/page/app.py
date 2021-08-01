# -*- coding:utf-8 -*-
import os
from .main_page import MainPage
from appium import webdriver
from ..page.base import BasePage
import os
import sys
from ..conftest import logging
logger = logging.getLogger()
import allure

'''
app.py 负责 app的启动，重启，关闭，进入主页等操作 ，继承BasePage
'''
class App(BasePage):

    @allure.step("start")
    def start(self):
        '''
        复用driver
        1、BasePage driver 设置一个初始值为None
        2、在app.py 文件App类继承 BasePage - start() 方法中，判断 driver 是否为None - 如果为None： 则创建一个新的driver -
        如果不为None：复用这个driver

        执行命令 shell
        mac/linux电脑：
        第一台设备：
        udid='123456' port = 4723  回车
        pytest test_contact.py

        第二台设备：
        udid='654321' port = 4725  回车
        pytest test_contact.py

        windows电脑：
        第一台设备：
        set udid='123456' port = 4723  回车
        pytest test_contact.py

        第二台设备：
        set udid='654321' port = 4725  回车
        pytest test_contact.py
         #udid = os.getenv("udid")
        #port = os.getenv("port")
        '''


        udid = sys.argv[1]
        port =  sys.argv[2]



        print (50*"*")
        print (udid)

        if self.driver == None:
            logger.info("driver is None!")
            caps ={
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true",
                "ensureWebviewHavePages": "true",
                "skipServerInstallation": "true",
                "skipDeviceInitialization": "true",
                "udid": udid,
                #Appium 1.6.3开始支持识别Toast内容，主要是基于UiAutomator2，
                #'automationName':'uiautomator2'
            }
            # 最重要的一句，client 与 server 端建立 连接的代码
            # 多设备不同的port
            self.driver = webdriver.Remote(f"http://127.0.0.1:{port}/wd/hub", caps)
            # 隐式等待 5s
            # 每次调用 find_element/s 方法的时候，都会动态的去查找这个元素
            # 如果 5s 都没有找到元素， 抛出NoSuchElementException
            self.driver.implicitly_wait(5)


        else:
            #启动driver里配置好的页面
            logger.info("driver is not None!")
            self.driver.launch_app()
        return self

    @allure.step("restart")
    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    @allure.step("stop")
    def stop(self):
        self.driver.quit()

    @allure.step("goto_main")
    def goto_main(self):
        return MainPage(self.driver)


