# -*- coding:utf-8 -*-
from ..page.app import App
from faker import Faker

class TestContact:
    def setup_class(self):
        self.app = App()
        self.fake = Faker('zh_CN')

    def setup(self):
        self.main = self.app.start().goto_main()



    def teardown(self):
        #app的关闭，driver的销毁
        self.app.back()


    def test_add_contact(self):
        '''
        操作步骤：
        1、启动企业微信--通讯录--添加成员--输入：名称，手机号，地址--保存
        :return:
        '''
        #无法输入汉字
        #name = self.fake.name()
        #address = self.fake.address()

        name = self.fake.pystr()
        phonenum = self.fake.phone_number()
        address = self.fake.pystr()
        print (name,phonenum,address)
        #TODO Toast出现太快，查找时已经弹完了
        # result = self.main.goto_contactlist().\
        #     goto_addmember().click_addmember_menual(). \
        #     edit_member(name, phonenum,address).get_result()

        result = self.main.goto_contactlist().\
            goto_add_contact().click_add_contact_menual(). \
            edit_contact(name, phonenum,address).is_in_add_contact_menual()
        assert result == True


    def test_delete_contact(self):
        '''
        操作步骤：
        1、启动企业微信--通讯录--点击任意联系人--点击...--点击：编辑成员--删除成员
        :return:
        '''
        result = self.main.goto_contactlist().delete_contact()
        assert result == True

