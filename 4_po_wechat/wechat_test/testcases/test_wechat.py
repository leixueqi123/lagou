# -*- coding:utf-8 -*-
import random
import string
import time
import allure

from ..pages.main_page import MainPage


class TestWechat:

     def setup(self):
         self.mainPage = MainPage()

     def teardown(self):
         pass

     @allure.story("test_add_member")
     def test_add_member(self):
         #PO:方法返回到其他PageObjects
         self.contactPage =  self.mainPage.goto_contact()
         #脚本里断言，判断进入"通讯录界面"
         self.contactPage.is_in_contact_page()
         #固定等待3秒，避免点击不到"通讯录"问题
         time.sleep(3)
         #PO:方法返回到其他PageObjects
         self.addMemberPage = self.contactPage.goto_add_menber()
         time.sleep(3)
         self.addMemberPage.is_in_add_member_page()

         #随机生成用户名，用户ID，手机号
         username = ''.join(random.sample(string.ascii_letters + string.digits, 6))
         memberAdd_acctid = ''.join(random.sample(string.ascii_letters + string.digits, 8))
         memberAdd_phone = random.choice(["135"])+"".join(random.choice("1234567890")for i in range(8))

         self.addMemberPage.add_member(username,memberAdd_acctid,memberAdd_phone)
         time.sleep(5)
         name_list = self.contactPage.get_list()
         time.sleep(5)

         #断言新添加用户，在通讯录界面
         if not username in name_list:
             raise AssertionError("添加联系人失败～")



